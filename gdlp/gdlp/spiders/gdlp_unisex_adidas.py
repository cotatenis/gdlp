from gdlp.spiders.gdlp_male_adidas import GDLPMaleAdidasSpider

class GDLPUnisexAdidasSpider(GDLPMaleAdidasSpider):
    name = 'gdlp-unisex-adidas'
    start_urls = ["https://gdlp.com.br/calcados/adidas/g%C3%AAnero/unisex"]