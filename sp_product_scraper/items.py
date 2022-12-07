# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ArtikelItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    a_no = scrapy.Field()
    b_name = scrapy.Field()
    b_name_two = scrapy.Field()
    c_werkstoff= scrapy.Field()
    d_ean = scrapy.Field()
    e_gewicht = scrapy.Field()
    f_ve=scrapy.Field()
    g_info = scrapy.Field()
    
