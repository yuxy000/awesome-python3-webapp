#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

"""
---------------------------------
@Time     : 2018/3/14 15:34
@Author   : yuxy
@File     : config_default.py
@Project  : awesome-python3-webapp
----------------------------------
"""
configs = {
    'debug': True,
    'db': {
        'host': '127.0.0.1',
        'port': 3306,
        'user': 'root',
        'password': '5720',
        'db': 'awesome'
    },
    'session': {
        'secret': 'Awesome'
    }
}
