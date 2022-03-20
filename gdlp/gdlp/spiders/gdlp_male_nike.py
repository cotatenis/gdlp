
from gdlp.spiders.gdlp_male_adidas import GDLPMaleAdidasSpider

class GDLPMaleNikeSpider(GDLPMaleAdidasSpider):
    name = 'gdlp-male-nike'
    start_urls = ["https://gdlp.com.br/calcados/nike/g%C3%AAnero/masculino"]