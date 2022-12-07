import scrapy
from sp_product_scraper.items import ArtikelItem

class SchaeferPetersProduktSpider(scrapy.Spider):
    name = 'productspider'
    start_urls = ['https://shop.schaefer-peters.com/de/Schrauben/Holzschrauben/']
    

    def parse(self, response):
        produkte = response.xpath('//div[contains(@class, "subcat-list-item")]//a[contains(@id, "moreSubCat")]/@href').getall()
        if produkte:
            for produktURL in produkte:
                yield scrapy.Request(produktURL, callback=self.parse_artikel)

        
       
    def parse_artikel(self, response):
        artikel_liste = response.xpath('//tr[contains(@class, "sp-product-item")]/td/a[@class="title"]/@href').getall()
        if artikel_liste:
            for artikel in artikel_liste:
                yield scrapy.Request(artikel, callback=self.parse_artikelinfo, )
        
       
    def parse_artikelinfo(self, response):
        artikel_name = response.xpath('//div[@class="information"]//h1/text()')
        if artikel_name:
            item = ArtikelItem()
            item['a_no'] = response.xpath('//div[contains(@class,"article-number")]/span/text()').get()
            item['b_name'] = artikel_name.get()
            item['b_name_two'] = response.xpath('//div[@class="information"]//span/text()').get()
            item['c_werkstoff'] = ": ".join(response.xpath('//div[@class="custom-attributes"]/div[@class="row"][1]/div/span//text()').getall())
            item['d_ean'] = ": ".join(response.xpath('//div[@class="custom-attributes"]/div[@class="row"][3]/div/span//text()').getall())
            #item['e_gewicht'] = ": ".join(response.xpath('//div[@class="custom-attributes"]/div[@class="row"][4]/div/span//text()').re('[a-zA-Z0-9]+\s'))
           
            item['e_gewicht'] = "".join(response.xpath('//div[@class="custom-attributes"]/div[@class="row"][4]/div/span/strong/text()').re('[a-zA-Z0-9 .]+')) + ": " + " ".join(response.xpath('//div[@class="custom-attributes"]/div[@class="row"][4]/div/span/text()').re('\S+')) #x,xx kg
            #item['f_ve'] = ": ".join(response.xpath('//div[@class="custom-attributes"]/div[@class="row"][5]/div/span//text()').re('[a-zA-Z0-9]+'))
           
            item['f_ve'] = "".join(response.xpath('//div[@class="custom-attributes"]/div[@class="row"][5]/div/span/strong/text()').re('[a-zA-Z0-9 .]+')) + ": " + " ".join(response.xpath('//div[@class="custom-attributes"]/div[@class="row"][5]/div/span/text()').re('\S+'))
           
            item['g_info'] = "  ".join(response.xpath('//div[@class="tab-pane active"]//span/text()').getall())
            yield item
