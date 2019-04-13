#!/usr/bin/env python 
# encoding: utf-8    
"""
@version: v1.0
@author: King
@contact: qqqqivy@gmail.com
@file: common.py
@time: 2019/4/12 16:56
"""

import logging.config
from conf import setting
import hashlib
from core import src


# 用户认证装饰器
def auth(func):
    from core import src
    def inner(*args, **kwargs):
        # 调用被装饰函数前需要做的操作
        if src.user_info['name']:
            res = func(*args, **kwargs)
            # 调用被装饰函数后需要做的操作
            return res
        else:
            src.login()

    return inner
