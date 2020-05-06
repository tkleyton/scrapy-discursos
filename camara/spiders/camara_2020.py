# -*- coding: utf-8 -*-
import scrapy
import re
from urllib.parse import unquote
from datetime import datetime
from ..items import CamaraItem


class CamaraSpider(scrapy.Spider):
    name = 'camara'
    allowed_domains = ['camara.leg.br']
    start_urls = ['https://www.camara.leg.br/internet/sitaqweb/resultadoPesquisaDiscursos.asp?txIndexacao=&CurrentPage=1&BasePesq=plenario&txOrador=&txPartido=&dtInicio=01/01/2020&dtFim=31/12/2020&txUF=&txSessao=&listaTipoSessao=&listaTipoInterv=&inFalaPres=&listaTipoFala=&listaFaseSessao=&txAparteante=&listaEtapa=&CampoOrdenacao=dtSessao&TipoOrdenacao=DESC&PageSize=1000&txTexto=&txSumario=']

    custom_settings={ 'FEED_URI': "camara_%(time)s.csv",
                       'FEED_FORMAT': 'csv'}

    def parse(self, response):
        links = response.xpath("//a[contains(@href, 'TextoHTML')]/@href").getall()
        links = [re.sub(r"\s", "", link) for link in links]

        for link in links:
            yield scrapy.Request(
                response.urljoin(link),
                callback=self.parse_pages
            )
        
        NEXT_PAGE_SELECTOR = '//a[@title="Próxima Página"]/@href'
        next_page = response.xpath(NEXT_PAGE_SELECTOR).extract_first()
        if next_page:
            yield scrapy.Request(
            response.urljoin(next_page),
            callback=self.parse
            )

    def parse_pages(self, response):
        item = CamaraItem()
        item['discurso'] = ' '.join(response.xpath('//p[@align="justify"]/descendant::*/text()').getall()).replace('\n', ' ').replace('\r', '')
        sumario = response.xpath('//div[@id="txSumarioID"]/text()').get()
        if sumario:
            item['sumario'] = sumario.replace('\n', ' ').replace('\r', '')
        item['sessao'] = re.search(re.compile('nuSessao=(.{,10})&'), response.url).group(1)
        item['fase'] = re.search(re.compile('sgFaseSessao=(.{,5})&'), response.url).group(1)
        item['hora'] = re.search(re.compile('dtHorarioQuarto=(.{,5})&'), response.url).group(1)
        item['data'] = re.search(re.compile('Data=(.{,11})&'), response.url).group(1)
        orador = re.match(re.compile(r' ?"?[OA] SRA?. ([\w\s]+) +\('), item['discurso'])
        if orador:
            item['orador'] = orador.group(1).strip().title()
        item['partido'] = unquote(re.search(re.compile('txApelido=[\w%\(\))]*,(.*)&txFase'), response.url).group(1)).strip()
        item['link'] = response.url
        yield item

