from gdlp.spiders.gdlp_male_adidas import GDLPMaleAdidasSpider

class GDLPKidsNikeSpider(GDLPMaleAdidasSpider):
    name = 'gdlp-kids-nike'
    start_urls = ["https://gdlp.com.br/calcados/nike/g%C3%AAnero/kids"]
