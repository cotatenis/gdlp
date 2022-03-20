
from gdlp.spiders.gdlp_male_adidas import GDLPMaleAdidasSpider

class GDLPUnisexJordanSpider(GDLPMaleAdidasSpider):
    name = 'gdlp-unisex-jordan'
    start_urls = ["https://gdlp.com.br/calcados/air-jordan/g%C3%AAnero/unisex"]