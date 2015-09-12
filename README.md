#山东CMCC-EDU一键登录脚本（可绕过白名单）

#安装
安装requests库
pip install --user requests

#使用
更改username、password（一键登录）
登录信息储存在
/home/vinson/.cmcc_info.json（更改）
登录
python cmcc_edu.py login
注销
python cmcc_edu.py logout
