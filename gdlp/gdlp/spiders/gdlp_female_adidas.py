from gdlp.spiders.gdlp_male_adidas import GDLPMaleAdidasSpider

class GDLPFemaleAdidasSpider(GDLPMaleAdidasSpider):
    name = 'gdlp-female-adidas'
    start_urls = ["https://gdlp.com.br/calcados/adidas/g%C3%AAnero/feminino"]
