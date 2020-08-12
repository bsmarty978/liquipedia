import scrapy


class UpcomingSpider(scrapy.Spider):
    name = 'upcoming'
    allowed_domains = ['liquipedia.net']
    start_urls = ['https://liquipedia.net/rainbowsix/Portal:Tournaments']

    def parse(self, response):
        sections = response.xpath("//div[@class = 'divRow']") 
        for row in sections:
            page_url = f'https://liquipedia.net{row.xpath(".//b/a/@href").get()}'
            #info_data = leuge_info(page_url)
            yield{
                'title': row.xpath(".//b/a/text()").get(),
                'link': page_url,
                'date': row.xpath(".//div[@class = 'divCell EventDetails-Left-55 Header']/text()").get(),
                'location': row.xpath(".//div[@class = 'divCell EventDetails-Left-60 Header']/text()").get(),
                'price': row.xpath(".//div[@class = 'divCell EventDetails-Right-45 Header']/text()").get(),
            }
    

        
