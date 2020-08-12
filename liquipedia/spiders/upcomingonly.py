import scrapy


class UpcomingonlySpider(scrapy.Spider):
    name = 'upcomingonly'
    allowed_domains = ['liquipedia.net']
    start_urls = ['https://liquipedia.net/rainbowsix/Liquipedia:Tournaments']

    def parse(self, response):
        upcomings = response.xpath("(//div[@class = 'mw-parser-output']/ul)[1]/li/ul/li")
        ongoings  = response.xpath("(//div[@class = 'mw-parser-output']/ul)[2]/li/ul/li")
        up_list = []
        on_list = []
        for up in upcomings:
            up_list.append(up.xpath(".//text()").get())
        for on in ongoings:
            on_list.append(on.xpath(".//text()").get())

        yield{
            'upcoming' : up_list,
            'ongoing' : on_list
        }

