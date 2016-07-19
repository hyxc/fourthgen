#!/usr/bin/python
# -*- coding: utf-8 -*-
 
import pycurl
import StringIO
import json
 
#登录salt-api,获取token
def api_login():
    global token
    url='https://10.211.55.100:8000/login'
    ch=pycurl.Curl()    #创建一个pycurl对象的方法
    ch.setopt(ch.URL, url)     #设置要访问的url
    info = StringIO.StringIO()     
    ch.setopt(ch.WRITEFUNCTION, info.write)
    ch.setopt(ch.POST, True)
    #如果是https就要开启这两行
    ch.setopt(ch.SSL_VERIFYPEER, 0)
    ch.setopt(ch.SSL_VERIFYHOST, 2)
    ch.setopt(ch.HTTPHEADER, ['Accept: application/x-yaml'])
    ch.setopt(ch.POSTFIELDS, 'username=hyxc&password=123456aa&eauth=pam')
    #要包头信息
    #ch.setopt(ch.HEADER, True)
    #不要包头信息
    ch.setopt(ch.HEADER,False)
    ch.perform()
    html = info.getvalue()
    #提取token
    token = html.split("\n")[-3].replace("\n", '')
    token = token.split(' ')[3]
    info.close()
    ch.close()
 
def api_key(fun='key.list_all', match='', arg_num=0):
    api_login()
    url='https://10.211.55.100:8000/'
    ch=pycurl.Curl()
    ch.setopt(ch.URL, url)
    info = StringIO.StringIO()
    ch.setopt(ch.WRITEFUNCTION, info.write)
    ch.setopt(ch.POST, True)
    ch.setopt(ch.SSL_VERIFYPEER, 0)
    ch.setopt(ch.SSL_VERIFYHOST, 2)
    ch.setopt(ch.HTTPHEADER, ['Accept: application/json', "X-Auth-Token: %s" %(token)])
    if arg_num == 0:
        ch.setopt(ch.POSTFIELDS, "client=wheel&fun=%s" %(fun))
    elif arg_num == 1:
        ch.setopt(ch.POSTFIELDS, "client=wheel&fun=%s&match=%s" %(fun, match))
    else:
        pass
    ch.setopt(ch.HEADER,False)
    ch.perform()
    html = info.getvalue()
    info.close()
    ch.close()
    return html

def api_exec(target, fun, expr_form='', arg='', arg_num=0):
    api_login()
    url='https://10.211.55.100:8000/'
    ch=pycurl.Curl()
    ch.setopt(ch.URL, url)
    info = StringIO.StringIO()
    ch.setopt(ch.WRITEFUNCTION, info.write)
    ch.setopt(ch.POST, True)
    ch.setopt(ch.SSL_VERIFYPEER, 0)
    ch.setopt(ch.SSL_VERIFYHOST, 2)
    ch.setopt(ch.HTTPHEADER, ['Accept: application/x-yaml', "X-Auth-Token: %s" %(token)])
    if arg_num == 0:
        ch.setopt(ch.POSTFIELDS, "client=local&tgt=%s&fun=%s" %(target, fun))
    elif arg_num == 1:
        ch.setopt(ch.POSTFIELDS, "client=local&tgt=%s&fun=%s&arg=%s" %(target, fun, arg))    
    elif arg_num == 2:
        ch.setopt(ch.POSTFIELDS, "client=local&tgt=%s&expr_form=%s&fun=%s&arg=%s" %(target, expr_form, fun, arg))
    else:
        pass
    ch.setopt(ch.HEADER,False)
    ch.perform()
    html = info.getvalue()
    info.close()
    ch.close()
#    return json.dumps(html)
    return html
 
#测试时用的,做为模块使用时请注释下面两行
#api_login()
#print api_key()
#print api_exec('*', 'test.ping')
#print api_exec('*', 'cmd.run', arg='ifconfig', arg_num=1)
#print api_key_check('key.list_all')
