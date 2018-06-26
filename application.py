#!/usr/bin/env python
#coding:utf-8
"""
  Author:  pirogue --<p1r06u3@gmail.com>
  Purpose: 应用配置文件
  Created: 2017/4/8
  Site:    http://pirogue.org
"""


import os
import logging


settings = dict(
    # 设置Debug开关
    debug = True,
    # 设置templates路径
    template_path = os.path.join(os.path.dirname(__file__), "templates"),
    # 设置静态文件解析路径
    # static_path = os.path.join(os.path.dirname(__file__), "assets"),
    # 设置cookie密钥
    cookie_secret = "1234567890qwertyuiopasdnghjklzxcvbnm1234567890qwrtyu",
    login_url = "/login",
)


# web日志配置
logfile = os.path.join(os.path.dirname(__file__), "logs", "app.log")
handler = logging.FileHandler(logfile)
logger = logging.getLogger()

logger.addHandler(handler)
logger.setLevel(logging.NOTSET)

