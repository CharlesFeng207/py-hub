from scrapy.spiders import SitemapSpider

class MySpider(SitemapSpider):
    name = "sm"
    sitemap_urls = ['https://www.qiushibaike.com/8hr/page/3/']
    sitemap_rules = [
        ('/users/', 'parse_usr'),
    ]

    def parse_usr(self, response):
        print(response)
        pass # ... scrape product ...