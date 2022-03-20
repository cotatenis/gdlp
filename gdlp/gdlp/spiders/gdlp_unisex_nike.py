from gdlp.spiders.gdlp_male_adidas import GDLPMaleAdidasSpider

class GDLPUnisexNikeSpider(GDLPMaleAdidasSpider):
    name = 'gdlp-unisex-nike'
    start_urls = ["https://gdlp.com.br/calcados/nike/g%C3%AAnero/unisex"]