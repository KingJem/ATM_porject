#!/usr/bin/env python 
# encoding: utf-8    
"""
@version: v1.0
@author: King
@contact: qqqqivy@gmail.com
@file: src.py.py
@time: 2019/4/12 16:55
"""
from interface import user, shop, pay
from lib import common

user_info = {
    "name": None

}


def register():
    while True:
        print("正在注册")
        name = input("请输入账户>>>")
        pwd1 = input("请输入密码>>>")
        pwd2 = input("请再次确认密码>>>")
        if pwd2 == pwd1:
            flag, meg = user.register_inter_face(name, pwd2)
            if flag:
                print(meg)
                print('注册成功已为你开通15000元额度')
                break
            else:
                return print(meg)
        else:
            print("你输入的密码不一致")
            return


def login():
    while True:
        name = input("输入账户>>>:")
        pwd = input("请输入密码>>>:")
        flag, message = user.login_inferface(name, pwd)
        if flag:
            print(message)
            user_info["name"]=name
            break
        else:
            print(message)


@common.auth
def check_balance():
    meg = user.check_balance_interface(user_info["name"])
    print(meg)


@common.auth
def withdraw():
    money = input("你想要去多少钱")
    flag, meg = user.withdraw_interface(user_info["name"], money)
    if flag:
        print(meg)
    else:
        print(meg)
        repay()


@common.auth
def transfer():
    name = user_info["name"]
    to_user = input("你想要转给谁")
    money = input("你想要转多少钱")
    flag,meg = user.transfer_interface(name,money,to_user)
    print(meg)

@common.auth
def repay():
    name = user_info["name"]
    money = input("你想充值/多少钱")
    flag,mes = pay.repay_interface(name,money)
    print(mes)


@common.auth
def check_flow():
    pass


@common.auth
def shopping():
    pass


@common.auth
def show_shopping_car():
    pass


def managment():
    pass


operating_map = {
    "1": register,
    "2": login,
    "3": check_balance,
    "4": withdraw,
    "5": transfer,
    "6": repay,
    "7": check_flow,
    "8": shopping,
    "9": show_shopping_car,
    "10": managment
}


def run():
    while True:
        print("请输入你要进进行的操作>>>：")
        print("""
                   1、注册
                   2、登录
                   3、查看余额
                   4、取款
                   5、转账
                   6、充值/还款
                   7、查看账单
                   8、购物
                   9、查看购物车
                   9、管理账户
                   0、退出
           """
              )
        choice = input("请输入你要进行的操作>>>")

        if choice == "10":
            break
        elif choice.isdigit() and choice in operating_map:
            operating_map[choice]()
        else:
            print('你的输入有误请重新输入')
