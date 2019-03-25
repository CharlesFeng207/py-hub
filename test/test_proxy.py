# coding:utf8

from common import req_utils, browser_utils
from common.settings import Settings


print("start")

print("origin " + req_utils.get_my_ip())

proxy_api = "http://webapi.http.zhimacangku.com/getip?num=1&type=1&pro=&city=0&yys=0&port=11&pack=40324&ts=0&ys=0&cs=0&lb=1&sb=0&pb=4&mr=1&regions="

proxy_ip = req_utils.get_xpath_selector(proxy_api).strip()
print("proxy " + proxy_ip)

if "您的该套餐已过期" not in proxy_ip:
    Settings.https_proxy = proxy_ip
    print("now " + req_utils.get_my_ip())

browser_utils.save_screenshot("https://www.ip.cn/")

print("end")



