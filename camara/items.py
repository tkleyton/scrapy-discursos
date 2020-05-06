# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CamaraItem(scrapy.Item):
    # define the fields for your item here like:
    data = scrapy.Field()
    sessao = scrapy.Field()
    fase = scrapy.Field()
    sumario = scrapy.Field()
    orador = scrapy.Field()
    hora = scrapy.Field()
    discurso = scrapy.Field()
    link = scrapy.Field()
    partido = scrapy.Field()
