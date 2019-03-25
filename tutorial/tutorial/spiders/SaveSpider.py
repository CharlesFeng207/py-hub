import scrapy
import json


class SaveSpider(scrapy.Spider):
    name = "save"

    def start_requests(self):
        # Reading data back
        with open('cookie.json', 'r') as f:
            cookie = json.load(f)

        urls = [
            "https://www.tapd.cn/my_worktable/?from=left_tree_cloud_v2"
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse, cookies=cookie)

    def parse(self, response):
        page = response.url.split("/")[-2]
        self.log(page)
        filename = 'save-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)
