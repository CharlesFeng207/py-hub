# coding:utf8

from common import req_utils, browser_utils
from common.settings import Settings

print("origin " + req_utils.get_my_ip_info())
Settings.socks_proxy = "95.110.230.142:12488"
print("after " + req_utils.get_my_ip_info())
