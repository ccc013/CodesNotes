#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2019/10/2 16:33
@Author  : luocai
@file    : netflix_movies_recommend_system.py
@concat  : 429546420@qq.com
@site    : 
@software: PyCharm Community Edition 
@desc    :

《推荐系统开发实战》章2.1 实例1：搭建电影推荐系统
"""
import os
import json
import random
import math
from collections import defaultdict


class FirstRec:
    """
        初始化函数
            file_path: 原始文件路径
            seed: 产生随机数的种子
            k: 选取的近邻用户个数
            n_items: 为每个用户推荐的电影数
    """

    def __init__(self, file_path, seed, k, n_items):
        self.file_path = file_path
        self.users_1000 = self.__select_1000_users()
        self.seed = seed
        self.k = k
        self.n_items = n_items
        self.train, self.test = self.__load_and_split_data()

    # 获取所有用户并随机选择 1000 个
    def __select_1000_users(self):
        print("随机选择1000个用户！")
        if os.path.exists('netflix_data/train.json') and os.path.exists('netflix_data/test.json'):
            return list()
        else:
            users = set()
            # 获取所有用户
            for file in os.listdir(self.file_path):
                one_path = "{}/{}".format(self.file_path, file)
                print('{}'.format(one_path))
                with open(one_path, 'r') as fp:
                    for line in fp.readlines():
                        if line.strip().endswith(":"):
                            continue
                        userID, *_ = line.split(',')
                        users.add(userID)
            # 随机选择 1000 个
            users_1000 = random.sample(list(users), 1000)
            print('random choose 1000 users: ', users_1000)
            return users_1000

    # 加载数据，并拆分为训练集和测试集
    def __load_and_split_data(self):
        train = dict()
        test = dict()
        if os.path.exists('netflix_data/train.json') and os.path.exists('netflix_data/test.json'):
            print("从文件中加载训练集和测试集")
            train = json.load(open('netflix_data/train.json'))
            test = json.load(open('netflix_data/test.json'))
            print('从文件中加载数据完成')
        else:
            # 设置产生随机数的种子，保证每次实验产生的随机结果一致
            random.seed(self.seed)
            for file in os.listdir(self.file_path):
                one_path = "{}/{}".format(self.file_path, file)
                print('{}'.format(one_path))
                with open(one_path, 'r') as fp:
                    movieID = fp.readline().split(':')[0]
                    for line in fp.readlines():
                        if line.strip().endswith(":"):
                            continue
                        userID, rate, _ = line.split(',')
                        # 判断用户是否在所选择的1000个用户中
                        if userID in self.users_1000:
                            if random.randint(1, 50) == 1:
                                test.setdefault(userID, {})[movieID] = int(rate)
                            else:
                                train.setdefault(userID, {})[movieID] = int(rate)
            print("加载数据到 netflix_data/train.json 和 netflix_data/test.json")
            json.dump(train, open('netflix_data/train.json', 'w'), indent=4, separators=(',', ':'))
            json.dump(test, open('netflix_data/test.json', 'w'), indent=4, separators=(',', ':'))
            print("数据加载完成")
        return train, test

    '''
        计算皮尔逊相关系数
            rating1:用户1的评分记录，形式如{"movieid1":rate1,"movieid2":rate2,...}
            rating2:用户2的评分记录，形式如{"movieid1":rate1,"movieid2":rate2,...}
    '''

    def pearson(self, rating1, rating2):
        sum_xy = 0
        sum_x = 0
        sum_y = 0
        sum_x2 = 0
        sum_y2 = 0
        num = 0
        for key in rating1.keys():
            if key in rating2.keys():
                num += 1
                x = rating1[key]
                y = rating2[key]
                sum_xy += x * y
                sum_x += x
                sum_y += y
                sum_x2 += math.pow(x, 2)
                sum_y2 += math.pow(y, 2)
        if num == 0:
            return 0
        # 皮尔逊相关系数分母
        denominator = math.sqrt(sum_x2 - math.pow(sum_x, 2) / num) * math.sqrt(sum_y2 - math.pow(sum_y, 2) / num)
        if denominator == 0:
            return 0
        else:
            return (sum_xy - (sum_x * sum_y) / num) / denominator

    '''
        用户 userID 进行电影推荐
            userID: 用户ID
    '''

    def recommend(self, userID):
        neightborUser = dict()
        for user in self.train.keys():
            if userID != user:
                distance = self.pearson(self.train[userID], self.train[user])
                neightborUser[user] = distance
        # 字典排序
        newNU = sorted(neightborUser.items(), key=lambda k: k[1], reverse=True)

        movies = defaultdict(float)
        for (sim_user, sim) in newNU[:self.k]:
            for movieID in self.train[sim_user].keys():
                # 推荐的电影的得分是用户相似度乘以用户的评分的求和
                try:
                    movies[movieID] += sim * self.train[sim_user][movieID]
                except KeyError as ke:
                    print('userID: {}, moviedID: {}, error: {}'.format(sim_user, movieID, ke))
                    raise
        # 再次排序
        new_movies = sorted(movies.items(), key=lambda k: k[1], reverse=True)
        return new_movies

    '''
        推荐系统效果评估函数
            num: 随机抽取 num 个用户计算准确率
    '''

    def evaluate(self, num=30):
        print('开始计算准确率')
        precisions = list()
        random.seed(10)
        for userID in random.sample(self.test.keys(), num):
            hit = 0
            result = self.recommend(userID)[:self.n_items]
            for item, rate in result:
                if item in self.test[userID]:
                    hit += 1
            precisions.append(hit / self.n_items)
        return sum(precisions) / len(precisions)


if __name__ == '__main__':
    file_path = r"E:\recommend_systems_datas\data\netflix\training_set"
    seed = 30
    k = 15
    n_items = 20
    f_rec = FirstRec(file_path, seed, k, n_items)
    # 测试计算皮尔逊相关系数
    # r = f_rec.pearson(f_rec.train["2135038"], f_rec.train["2082397"])
    # print("2135038 和 2082397 的皮尔逊相关系数为: {}".format(r))
    # 为用户 2135038 推荐电影
    result = f_rec.recommend("2135038")
    print("为用户ID 为: 2135038 的用户推荐的电影为: ", result)
    print("算法的推荐准确率是: {}".format(f_rec.evaluate()))
