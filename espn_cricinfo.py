from tutorial.items import TutorialItem
import scrapy
joined_urls = []

class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls=[
                'http://www.espncricinfo.com/'
              ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        link = response.css('source img::attr(data-default-src)').extract_first()
        joined_urls.append(link)
        yield TutorialItem(file_urls=joined_urls)
        
    def url_join(self, urls):
        joined_urls = []
        for url in urls:
            joined_urls.append(url) 
        return joined_urls