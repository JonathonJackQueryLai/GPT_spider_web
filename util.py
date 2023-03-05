#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/3/4 9:21
# @Author  : Jonathon
# @File    : util.py
# @Software: PyCharm
# @ Motto : 客又至，当如何

import pymysql
import threading
import configparser
import pandas as pd

from sqlalchemy import create_engine

conf = configparser.ConfigParser()
conf.read('config.ini')
user = conf.get("mysql", "user")
password = conf.get("mysql", "password")
port = conf.get("mysql", "port")
database = conf.get("mysql", "database")
host = conf.get("mysql", "host")


class DatabaseConnection:
    __instance = None
    __lock = threading.Lock()

    @staticmethod
    def getInstance():
        """静态方法获取单例实例"""
        with DatabaseConnection.__lock:
            if DatabaseConnection.__instance is None:
                DatabaseConnection()
        return DatabaseConnection.__instance

    def __init__(self, user, password, port, database, host):
        """私有构造函数，避免外部实例化"""
        with DatabaseConnection.__lock:
            if DatabaseConnection.__instance is not None:
                raise Exception("This class is a singleton!")
            self.__host = host
            self.__user = user
            self.__password = password
            self.__database = database
            self.__port = int(port)
            self.__connection = pymysql.connect(
                host=self.__host,
                user=self.__user,
                password=self.__password,
                database=self.__database,
                port=self.__port,
            )
            # yconnect = create_engine('mysql+pymysql://用户名:密码@主机地址:端口/数据库名称?charset=utf8')
            s = f'mysql+pymysql://{self.__user}:{self.__password}@{self.__host}:{self.__port}/{self.__database}?charset=utf8'
            self.__create_engine = create_engine(s)
            DatabaseConnection.__instance = self

    def getConnection(self):
        """获取数据库连接"""
        return self.__connection

    def getCreateEngine(self):
        """获取数据库引擎"""
        return self.__create_engine.connect()


class Pymysql_demo:
    def __init__(self, user, password, port, database, host):
        self.__host = host
        self.__user = user
        self.__password = password
        self.__database = database
        self.__port = int(port)
        self.__connection = pymysql.connect(
            host=self.__host,
            user=self.__user,
            password=self.__password,
            database=self.__database,
            port=self.__port,
        )
        self.__cursor = self.__connection.cursor()

    def sql_exec(self, sql_string):
        self.__cursor.execute(sql_string)
        self.__connection.commit()
        result = self.__cursor.fetchall()
        print(result)


# connection = DatabaseConnection(user, password, port, database, host).getInstance().getConnection()
connection1 = Pymysql_demo(user, password, port, database, host)

# engine = DatabaseConnection(user, password, port, database, host).getInstance().getCreateEngine()


#
# def sql_exec(sql_string):
#     with connection1.cursor() as cur:
#         cur.execute(sql_string)
# if __name__ == '__main__':
#
#
#     cursor.execute("SELECT * FROM q_ans")
#     result = cursor.fetchall()
#     print(result)
