
from gdlp.spiders.gdlp_male_adidas import GDLPMaleAdidasSpider

class GDLPMaleJordanSpider(GDLPMaleAdidasSpider):
    name = 'gdlp-male-jordan'
    start_urls = ["https://gdlp.com.br/calcados/air-jordan/g%C3%AAnero/masculino"]