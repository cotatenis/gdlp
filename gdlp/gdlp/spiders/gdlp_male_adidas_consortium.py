from gdlp.spiders.gdlp_male_adidas import GDLPMaleAdidasSpider

class GDLPMaleAdidasConsortiumSpider(GDLPMaleAdidasSpider):
    name = 'gdlp-male-adidas-consortium'
    start_urls = ["https://gdlp.com.br/calcados/adidas-consortium/g%C3%AAnero/masculino"]