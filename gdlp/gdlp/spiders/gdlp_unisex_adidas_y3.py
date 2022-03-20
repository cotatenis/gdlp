from gdlp.spiders.gdlp_male_adidas import GDLPMaleAdidasSpider

class GDLPUnisexAdidasY3Spider(GDLPMaleAdidasSpider):
    name = 'gdlp-unisex-adidas-y3'
    start_urls = ["https://gdlp.com.br/calcados/adidas-y-3/g%C3%AAnero/unisex"]