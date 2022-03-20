
from gdlp.spiders.gdlp_male_adidas import GDLPMaleAdidasSpider

class GDLPKidsJordanSpider(GDLPMaleAdidasSpider):
    name = 'gdlp-kids-jordan'
    start_urls = ["https://gdlp.com.br/calcados/air-jordan/g%C3%AAnero/kids"]