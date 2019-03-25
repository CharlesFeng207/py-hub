# coding:utf8

from common import req_utils,browser_utils
from lxml import etree


def do(url):

    print(url)

    driver = browser_utils.get_webdriver_from_settings()
    driver.get(url)
    selector = etree.HTML(driver.page_source)

    r = selector.xpath('//*[@id="main"]/div/dl/dd/h4/a/text()')
    print(r)

    if any(map(lambda x: "暗黑" in str(x), r)):
        print("here!")
        return

    # find next

    r = selector.xpath("//*[@id='yw0']/a[text()='>>']/@href")

    if len(r) > 0 and str(r[0]) != url:
        do(str(r[0]))
    else:
        print("completed!")


print(req_utils.get_my_ip())
do("http://tvgdb.duowan.com/pc")





