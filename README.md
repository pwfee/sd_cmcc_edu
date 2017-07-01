# CMCC-EDU绕过白名单登录脚本

#### update:
2015-10-19 山东亲测可用
通过UA=G3WLAN模拟随E行客户端实现绕过白名单

### 安装
requests库
pip install --user requests

### 使用
1.更改sd_cmcc_edu.py里面的username和password

2.登录的信息save到path
更改/home/vinson/.cmcc_info.json(default)

3.登录
python cmcc_edu.py login

4.注销
python cmcc_edu.py logout



