# coding:utf8

from lxml import etree
from .settings import Settings
import requests
import logging


def get_page_code(url, decoding=None):

    proxies = {}

    if Settings.socks_proxy is not None:
        proxies["http"] = proxies["https"] = Settings.get_full_socks_proxy()
    else:
        if Settings.http_proxy is not None:
            proxies["http"] = Settings.http_proxy
        if Settings.https_proxy is not None:
            proxies["https"] = Settings.https_proxy

    cookies = {}
    if Settings.cookies is not None:
        cookies = {obj["name"]: obj["value"] for obj in Settings.cookies}

    response = requests.get(url, headers=Settings.headers,  proxies=proxies, cookies=cookies)
    if response.status_code != 200:
        logging.error("%s response status_code:%s" % (url, response.status_code))

    if decoding is None:
        return response.text
    else:
        return response.content.decode(decoding)


def get_xpath_selector(url, decoding=None):
    content = get_page_code(url, decoding)
    selector = etree.HTML(content)
    return selector


def get_my_ip():
    selector = get_xpath_selector("https://www.ip.cn/")
    ip = selector.xpath('//*[@id="result"]/div/p[1]/code/text()')[0]
    location = selector.xpath('//*[@id="result"]/div/p[2]/code/text()')[0]
    return ip + " " + location


