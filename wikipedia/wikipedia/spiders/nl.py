from hashlib import new
from urllib import request
from parso import parse
from pyparsing import col
import scrapy


class NlSpider(scrapy.Spider):
    name = 'nl'
    # allowed_domains = ['https://nl.wikipedia.org/wiki/Lijst_van_Nederlandse_plaatsen_met_stadsrechten']
    start_urls = [
        "https://nl.wikipedia.org/wiki/Lijst_van_Nederlandse_plaatsen_met_stadsrechten"]

    def parse(self, response):
        """
        we get href information for each city.
        """
        table = response.xpath(
            '//*[@id="mw-content-text"]/div[1]/table[1]/tbody/tr')
        for city in table:
            href = city.css('a::attr(href)').get()
            new_url = response.urljoin(href)
            yield scrapy.Request(new_url, callback=self.population)

    def population(self, response):
        cityname = response.css('div.mw-parser-output b::text').get()
        population_rows = response.xpath(
            '//*[@id="mw-content-text"]/div[1]/table[1]').css('tbody tr ')

        for row in population_rows:
            """
            used 'for' because of it is table 
            """
            if row.css('td a::attr(title)').get() == 'Provincies van Nederland':
                region = row.css('td:nth-child(2) a ::text').get()
            if row.css('td ::text').get() == 'Inwoners ' or row.css('td ::text').get() == 'Inwoners':
                population = (
                    row.css('td:nth-child(2) ::text').get().rstrip('\n').replace('.', ''))
                yield {'country': 'Netherlands', 'city': cityname, 'region': region, 'population': population}
