import scrapy

class TestIPSpider(scrapy.Spider):
    name = 'testIP'

    def start_requests(self):
        self.log("start test, ip is %s" % self.ip)
        urls = [
            'https://www.ipqualityscore.com/free-ip-lookup-proxy-vpn-test/lookup/%s' % self.ip,
            'https://www.ipqualityscore.com/device-fingerprinting',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]

        filename = 'test-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)