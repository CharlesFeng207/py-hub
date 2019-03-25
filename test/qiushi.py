# coding:utf8
import os, re, urllib, locale, sys
from bs4 import BeautifulSoup
from urllib import request, error
from timeit import default_timer as timer
import json
from time import sleep
import random
import datetime

class QiushiCraw:

    # init and define some variables
    def __init__(self):
        # set user agent
        self.user_agent = 'Mozilla2/4.0 (compatible; MSIE 5.1235; Windows NT)'

        # set headers
        self.headers = {'User-Agent': self.user_agent}

        # set target
        self.target = r'http://www.qiushibaike.com/8hr/page/{}/?s=4980751'

        self.folder = "/root/QiushiCrawerOutput"

        if not os.path.exists(self.folder):
            os.makedirs(self.folder)

    def GetLst(self, pageIndexes):
        while len(pageIndexes) > 0:
            if self.Get(pageIndexes[0]):
                del pageIndexes[0]
            sleep(random.randrange(5, 10))

    def Get(self, pageIndex):

        print('start to collect page ' + str(pageIndex) + " " + str(datetime.datetime.now()))

        pageCode = self.__getPageCode(pageIndex)

        if not pageCode:
            print("pageCode not found 3")
            return False

        # with open('{}/PageCode{}.txt'.format(self.folder, pageIndex), "w+", encoding="utf-8") as code_file:
        #     code_file.write(pageCode)

        itemLst = self.__colcInfo(pageCode)

        self.__save(itemLst, str(pageIndex))
        return len(itemLst) > 0

    def __save(self, itemLst, name):
        with open('{}/{}.txt'.format(self.folder, name), "w+", encoding="utf-8", errors="ignore") as out_file:
            for item in itemLst:
                # s = json.dumps(item, ensure_ascii=False)
                s = json.dumps(item).encode("utf-8", "ignore").decode("unicode-escape")

                try:
                    out_file.write(s)
                    # print(s)
                    # raise Exception("asd")
                except Exception as e:
                    print("error!")
                    with open('{}/error.txt'.format(self.folder), "w+", errors="ignore") as err_file:
                        err_file.write(repr(s))
                        err_file.write(str(e))
                        print(repr(s))
                pass
            pass
        pass


    # collect infomation
    def __colcInfo(self, pageCode):

        soup = BeautifulSoup(pageCode, features="html.parser")
        userResult = soup.findAll('div', {'class': "author clearfix"})

        itemLst = []

        for user in userResult:
            contentResult = user.findNext('div', {'class': "content"})
            item = {'user': user.text, 'content': contentResult.text}

            itemLst.append(item)

        print('collected ' + str(len(itemLst)))

        return itemLst

    # get page code by index
    def __getPageCode(self, pageIndex):
        try:
            url = self.target.format(pageIndex)
            req = urllib.request.Request(url, headers=self.headers)
            response = urllib.request.urlopen(req)

            try:
                p = response.read().decode('utf-8')
                return p
            except Exception as e:
                print(url)
                with open('{}/pageError.txt'.format(self.folder), "w+", errors="ignore") as err_file:
                    err_file.write(url)
                return None

        except error.HTTPError as e:
            if hasattr(e, "reason"):
                print("connect error,the reason is ")
                return None


crawer = QiushiCraw()
crawer.GetLst(list(range(3000, 5000)))
