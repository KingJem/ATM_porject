#!/usr/bin/env python 
# encoding: utf-8    
"""
@version: v1.0
@author: King
@contact: qqqqivy@gmail.com
@file: user.py.py
@time: 2019/4/12 16:55
"""
from db import db_handler

def register_inter_face(name,pwd2):
    user_dict = db_handler.get_user_dic(name)
    if user_dict:
       return False, "你输入的账号已经存在请登录"
    else:
        user_dict = {
            "name": name, "pwd": pwd2, "balance": 15000, "flow": [], "shopping_car": {}, "status": None, "time": None
        }
        db_handler.save(user_dict)
        return True, "注册成功"







def login_inferface(name, pwd):
    user_dict = db_handler.get_user_dic(name)
    #{'name': 'jin', 'pwd': '123', 'balance': 1500, 'flow': [], 'shopping_car': {}, 'status': None, 'time': None}
    print(user_dict)
    print(name)
    print(user_dict["pwd"])
    if not user_dict:
        return False, "你输入的账户不存在"
    elif pwd == user_dict["pwd"]:
        return True, "登录成功"
    else:
        return False, "密码错误"



def check_balance_interface(name):
    user_dict = db_handler.get_user_dic(name)
    return user_dict["balance"]

def withdraw_interface(name,with_money):
    user_dict = db_handler.get_user_dic(name)
    real_money = user_dict["balance"]
    if int(with_money) >= int(real_money):
        real_money -= with_money
        user_dict["balance"] = real_money
        db_handler.save(user_dict)
        return True,"ATM 正在工作，请拿好你的钱 "

    else:
        return  False,"你账户里面的余额不做，请充值"

def transfer_interface(name,money,to_user):
    user_dict = db_handler.get_user_dic(name)
    to_user_dict = db_handler.get_user_dic(to_user)
    print(user_dict)
    real_money = int(user_dict["balance"])
    if not to_user_dict:
        return False,"你要转账的用户不存在"
    elif real_money >= int(money):
        user_dict["balance"] -= int(money)
        to_user_dict["balance"] += int(money)
        db_handler.save(user_dict)
        db_handler.save(to_user_dict)
        return True, "转账成功"
    else:
        return  False, "尊敬的用户你的账户余额不足，请充值"

