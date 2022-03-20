from gdlp.spiders.gdlp_male_adidas import GDLPMaleAdidasSpider

class GDLPFemaleNikeSpider(GDLPMaleAdidasSpider):
    name = 'gdlp-female-nike'
    start_urls = ["https://gdlp.com.br/calcados/nike/g%C3%AAnero/feminino"]
