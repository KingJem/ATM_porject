#!/usr/bin/env python 
# encoding: utf-8    
"""
@version: v1.0
@author: King
@contact: qqqqivy@gmail.com
@file: start.py.py
@time: 2019/4/12 16:47
"""
from core import src
import os
import sys

## 设置项目根目录
PATH = os.path.dirname(__file__)

# 添加到环境变量中去
sys.path.append(PATH)
"""
额度 15000或自定义
实现购物商城，买东西加入 购物车，调用信用卡接口结账
可以提现，手续费5%
每月22号出账单，每月10号为还款日，过期未还，按欠款总额 万分之5 每日计息
支持多账户登录
支持账户间转账
记录每月日常消费流水
提供还款接口
ATM记录操作日志 
提供管理接口，包括添加账户、用户额度，冻结账户等。。。
用户认证用装饰器
"""
import os
import sys
from core import src

BATH_DIR = os.path.dirname(__file__)
sys.path.append(BATH_DIR)

if __name__ == '__main__':
    src.run()
