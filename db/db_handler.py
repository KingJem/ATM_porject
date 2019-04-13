#!/usr/bin/env python 
# encoding: utf-8    
"""
@version: v1.0
@author: King
@contact: qqqqivy@gmail.com
@file: db_handler.py
@time: 2019/4/12 16:55
"""
from conf import setting
from interface import pay
from interface import shop
from interface import user
from start import BATH_DIR
import os
import sys
import json
from conf import setting


# 存放用户输入的数据
def save(user_dict):
    file_path = os.path.join(BATH_DIR, )
    # status 0 冻结 1 正常
    # thaw 格式是时间格式，里面存的是什么时候能解冻

    with open('%s/%s.json' % (setting.DB_PATH, user_dict['name']), 'w', encoding='utf-8') as f:
        res = json.dumps(user_dict)
        f.write(res)
        f.flush()


def get_user_dic(name):
    user_path = '%s/%s.json' % (setting.DB_PATH, name)
    if not os.path.exists(user_path):
        return
    with open(user_path, 'r', encoding='utf-8') as f:
        user_dict = json.load(f)
        return user_dict
