#!/usr/bin/env python
#coding:utf-8
"""
  Author:  pirogue --<p1r06u3@gmail.com>
  Purpose: URL路由配置文件
  Created: 2017/4/8
  Site:    http://pirogue.org
"""

from handlers import login



url = [
    # LoginHandler url
    # (r"/login", login.LoginHandler),
    (r"/", login.BaseHandler),
    # (r"/logout", login.LogoutHandler),
]



if __name__ == '__main__':
    unittest.main()