#CMCC-EDU绕过白名单登录脚本

###安装
requests库
pip install --user requests

###使用
1.更改sd_cmcc_edu.py里面的username和password

2.登录的信息save到path
更改/home/vinson/.cmcc_info.json(default)

3.登录
python cmcc_edu.py login

4.注销
python cmcc_edu.py logout
