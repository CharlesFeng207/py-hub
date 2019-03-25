# coding:utf8

from common import req_utils
from lxml import etree


def do(urlbase, urlpage):
    url = urlbase + urlpage
    print(url)

    selector = req_utils.get_xpath_selector(url)

    r = selector.xpath('//*[@id="tj_left_box"]/div/div[1]/h1/a/text()')
    print(r)

    # if any(map(lambda x: "暗黑" in str(x), r)):
    #     print("here!")
    #     return

    # find next
    r = selector.xpath('//*[@id="pageNum"]/span/a[text()="下一页"]/@href')

    if len(r) > 0:
        do(urlbase, str(r[0]))
    else:
        print("completed!")


print(req_utils.get_my_ip())
do("http://psp.duowan.com/0804/", "m_73013382452.html")





