from gdlp.spiders.gdlp_male_adidas import GDLPMaleAdidasSpider

class GDLPKidsAdidasSpider(GDLPMaleAdidasSpider):
    name = 'gdlp-kids-adidas'
    start_urls = ["https://gdlp.com.br/calcados/adidas/g%C3%AAnero/infantil"]