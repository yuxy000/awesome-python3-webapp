#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

"""
---------------------------------
@Time     : 2018/3/14 10:58
@Author   : yuxy
@File     : sql_test.py
@Project  : awesome-python3-webapp
----------------------------------
"""
import sys
import orm
from models import User
import asyncio


async def test(loop):
    print('enter')

    await orm.create_pool(loop=loop, user='root', password='5720', db='awesome')
    u = User(name='Test12', email='test12@example.com', passwd='123456789012', image='about:blank')

    await u.save()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(test(loop))
    loop.close()
    if loop.is_closed():
        sys.exit(0)
