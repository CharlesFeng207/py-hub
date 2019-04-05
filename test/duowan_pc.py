# coding:utf8

from common import req_utils, browser_utils
from common.logger_init import LoggerInit
from lxml import etree
import logging
import multiprocessing
from multiprocessing import Lock
import time
from common.settings import Settings


def do(url):
    logging.info(url)

    content = req_utils.get_page_code(url, 'utf-8')
    selector = etree.HTML(content)

    try:
        r = selector.xpath('//*[@id="main"]/div/dl/dd/h4/a/text()')
    except:
        logging.fatal("Parse %s failed" % url)
        logging.info(content)
        browser_utils.save_screenshot(pagecode=content)
        return

    logging.info(r)


    # if any(map(lambda x: "暗黑" in str(x), r)):
    #     print("here!")
    #     return

    # find next
    r = selector.xpath("//*[@id='yw0']/a[text()='>>']/@href")

    # time.sleep(1)

    if len(r) > 0 and str(r[0]) != url:
        do(str(r[0]))
    else:
        logging.info("completed!")

#
# if __name__ == '__main__':
#     Settings.socks_proxy = "127.0.0.1:1086"


LoggerInit.init(level=logging.INFO, filemode="a")
logging.info(req_utils.get_my_ip())
# browser_utils.save_screenshot("https://www.ip.cn/")

if __name__ == '__main__':
    p1 = multiprocessing.Process(target=do, args=("http://tvgdb.duowan.com/pc?page=200",))
    p1.start()
    # p1.daemon=True
    # p1.join()

    do("http://tvgdb.duowan.com/pc")
