import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class UpcomingmetaSpider(CrawlSpider):
    name = 'upcomingmeta'
    allowed_domains = ['liquipedia.net']
    user_agent = 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Mobile Safari/537.36'
   
    def start_requests(self):
        yield scrapy.Request(url='https://liquipedia.net/rainbowsix/Portal:Tournaments', headers={
        'User-Agent': self.user_agent
        })

    rules = (
        Rule(LinkExtractor(restrict_xpaths="//div[@class = 'divRow']//b/a"), callback='parse_item', follow=True, process_request='set_user_agent'),
    )

    def set_user_agent(self, request):
        request.headers['User-Agent']=self.user_agent
        return request

    def parse_item(self, response):
        box = response.xpath("//div[@class = 'fo-nttax-infobox wiki-bordercolor-light']")
        info_key = response.xpath("//div[@class = 'infobox-cell-2 infobox-description']")
        info_value = response.xpath("//div[@class = 'infobox-cell-2']")
        d = {}
        for (info_k,info_v) in zip(info_key,info_value):
            key = info_k.xpath(".//text()").get()
            value = info_v.xpath("normalize-space(.//text())").get()
            if value == '':
                value = info_v.xpath("normalize-space(./a/text())").get()
            d[key] = (value).strip()
        
        yield{
            'name' : box.xpath(".//div[@class = 'infobox-header wiki-backgroundcolor-light']/text()").get(),
            'league_info' : d
        }
