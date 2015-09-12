#!/usr/bin/env python
#-*- coding:utf-8 -*-
from __future__ import unicode_literals
import requests
headers = {'Accept-Charset': 'gb2312','Content-Type': 'application/x-www-form-urlencoded','User-Agent': 'G3WLAN','Host': '211.137.185.106:8443','Connection': 'Keep-Alive','Accept-Encoding': 'gzip','Content-Length': '390'}
import json
import re

baidu = 'http://www.baidu.com/'
# change this to file you want to save login info
info_file = '/users/vinson/cmcc_info.json'
username = 'xxx' #用户名
password = 'xxx' #密码
# username = input("Please input your username:\n")
# password = input("Please input your password:\n")

clienttype='UE,Android,8.4.0.002'
ssid='CMCC-EDU'
LOGIN='LOGIN'  
LOGOUT='LOGOUT'  
portalurl='https://211.137.185.106:8443/g3wlan.do' # G3WLAN_Portal
def get_info(site=baidu):
    r = requests.get(site, verify=False)
    url = r.url
    if url == site:
        domain = ''
        login_info = {}
        print '已经连网，不用再登录了:-)'
    else:
        print '正在获取登录信息...'
        domain, args_url = url.split('?')
        args = args_url.split('&')
        for arg in args:
            if arg.split('=')[0] == 'wlanuserip':
                wlanuserip = arg.split('=')[1]
            elif arg.split('=')[0] == 'wlanacname':
                wlanacname = arg.split('=')[1]
            elif arg.split('=')[0] == 'wlanacip':
                wlanacip = arg.split('=')[1]
            elif arg.split('=')[0] == 'wlanparameter':
                wlanparameter = arg.split('=')[1]

        login_info = {
            'USER':username,
            'PWD':password,
            'wlanuserip':wlanuserip, 
            'wlanacname':wlanacname,
            'portalurl':portalurl,
            'macAddress':wlanparameter,
            'ssid':ssid,
            'actiontype':LOGIN,
            'clienttype':clienttype

        }
        logout_info = {
            'USER':username,
            'PWD':password,
            'wlanuserip':wlanuserip, 
            'wlanacname':wlanacname,
            'portalurl':portalurl,
            'macAddress':wlanparameter,
            'ssid':ssid,
            'actiontype':LOGOUT,
            'clienttype':clienttype
        }
        info = {'domain':domain, 'logout_info':logout_info}
        with open(info_file, 'w') as f:
            json.dump(info, f)
    return domain, login_info

    
def login(domain,info):
    if domain:
        print '正在登录...'
        url = domain.replace('input', 'login')
    # uncheck certificate,this is unsafe, as soon as CMCC-EDU 
    # certificate be valid again, you should set verify=True for
    # security
        r = requests.post(portalurl,info,headers = headers,verify=False)
        encoding = r.encoding
        content = r.content.decode(encoding)
        if '登录成功' in content:
            print '登录成功！'
            time_remains = re.findall('套餐剩余.*', content)
            if time_remains:
                print re.sub('<[^<]+?>', '', time_remains[0])
        else:
                print '登录失败！'

def logout(domain,logout_info):
    url = domain.replace('input', 'logout')
    r = requests.post(portalurl,logout_info,headers = headers,verify=False)
    if r.status_code == 200:
        print '成功下线！'

if __name__ == '__main__':
    if len(sys.argv) == 2:
        if sys.argv[1] == 'login':
            domain, login_info = get_info(baidu)
            login(domain, login_info)
        if sys.argv[1] == 'logout':
            with open(info_file, 'r') as f:
                d = json.load(f)
            domain = d['domain']
            logout_info = d['logout_info']
            logout(domain, logout_info)
    else:
        print """Invalid command. Please use
        ``python cmcc_edu.py login`` to login
        ``python cmcc_edu.py logout`` to logout"""