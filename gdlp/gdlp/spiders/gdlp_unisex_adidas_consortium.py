from gdlp.spiders.gdlp_male_adidas import GDLPMaleAdidasSpider

class GDLPUnisexAdidasConsortiumSpider(GDLPMaleAdidasSpider):
    name = 'gdlp-unisex-adidas-consortium'
    start_urls = ["https://gdlp.com.br/calcados/adidas-consortium/g%C3%AAnero/unisex"]