#!/usr/bin/env python 
# encoding: utf-8    
"""
@version: v1.0
@author: King
@contact: qqqqivy@gmail.com
@file: pay.py.py
@time: 2019/4/12 16:56
"""
from db import  db_handler


def repay_interface(name,money):
    user_dict = db_handler.get_user_dic(name)
    user_dict["balance"] += int(money)
    return  True, "充值/还款成功"


 