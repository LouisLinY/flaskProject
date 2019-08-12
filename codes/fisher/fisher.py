#! /usr/bin/env python3
# -*- coding: UTF-8 -*-
# __author__ = "Lin Yu"
# Date: 2019/8/11 15:56

from flask import Flask, make_response
# from config import DEBUG

__author__ = 'Lin Yu'

app = Flask(__name__)
app.config.from_object('config')
print(app.config['DEBUG'])  #全部要求大写，所有的配置参数都是大写的


@app.route('/hello')  #使用装饰器注册函数，route内部调用add_url_rule，装饰器可以解决代码耦合问题
def hello():
	#status code
	#content-type http headers
	#content-type=text/html
	#response
	headers = {
		'content-type': 'text/plain',  #application/json
		'location': 'http://www.baidu.com'
	}
	# response = make_response('<html></html>', 404)
	# response.headers = headers
	# return response
	return '<html></html>', 301, headers   #推荐使用
	# return 'hello, linyu'   #


#最小原型与唯一url原则
#带/和不带/的区别
#重定向

#基于类的视图（即插视图）
# app.add_url_rule('/hello', view_func=hello)

if __name__ == '__main__':          #如果该文件作为入口函数执行，如果
	#生产环境nginx+uwsgi，有uwsgi加载flask模块执行的，被uwsgi加载的模块文件
	#如果没有if判断，uwsgi一旦加载这个文件之后，app.run会被
	#if可以保证uwsgi加载时不会启动flask自带的服务器
	app.run(host="0.0.0.0", debug=app.config['DEBUG'], port=80)



