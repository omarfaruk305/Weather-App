import scrapy



class TRwikipedia(scrapy.Spider):

    name = "TRwikipedia"

    start_urls=["https://tr.wikipedia.org/wiki/T%C3%BCrkiye'deki_illerin_n%C3%BCfuslar%C4%B1_(2020)"]

    def parse(self,response):

        result = response.css('table.wikitable tr')

        for i in result :
            data = i.css('td ::text').getall()
            if len(data)!= 0 :
                yield {'city':data[0],'region':data[2],'population':data[1]}