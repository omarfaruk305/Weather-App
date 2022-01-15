from attr import dataclass
import scrapy


class UsaSpider(scrapy.Spider):
    name = 'usa'
    # allowed_domains = ['https://en.wikipedia.org/wiki/List_of_United_States_cities_by_population']
    start_urls = ['https://en.wikipedia.org/wiki/List_of_United_States_cities_by_population']


    def parse(self,response):
        city=response.xpath('//*[@id="mw-content-text"]/div[1]/table[5]/tbody/tr')
        for i in city :
            data=i.css('a ::attr(title)').getall()
            pop=i.xpath('td[3]/text()').get()
            # yield {'city': data[0],'region':data[1]}
            if len(data)!= 0 :
                data1 = data[0].split(",")
                city = data1[0]
                region = data[1]
                population = pop.split("\n")  
                population=population[0].split(",")
                population="".join(population)
                if population.isnumeric():
                    population=int(population)   
                yield {'city':city,'region':region, 'population' :population} 
      

