from scrapy.utils.project import get_project_settings
import os
from scrapy.crawler import CrawlerRunner
from gdlp.spiders import (
    GDLPMaleAdidasSpider,
    GDLPFemaleAdidasSpider,
    GDLPUnisexAdidasSpider,
    GDLPKidsAdidasSpider,
    GDLPMaleAdidasConsortiumSpider,
    GDLPUnisexAdidasConsortiumSpider,
    GDLPMaleAdidasY3Spider,
    GDLPUnisexAdidasY3Spider,
    GDLPMaleJordanSpider, 
    GDLPKidsJordanSpider,
    GDLPUnisexJordanSpider,
    GDLPMaleNikeSpider,
    GDLPFemaleNikeSpider,
    GDLPUnisexNikeSpider,
    GDLPKidsNikeSpider
)
from scrapy.utils.log import configure_logging
from config import settings
from typer import Typer
from twisted.internet import reactor
import os

app = Typer()

@app.command()
def start_crawl(brand: str = ""):
    if brand not in settings.get("store.brands"):
        raise ValueError(f"{brand} is not a valid store.")
    spider = {
        'gdlp-male-adidas' : GDLPMaleAdidasSpider,
        'gdlp-female-adidas' : GDLPFemaleAdidasSpider,
        'gdlp-unisex-adidas' : GDLPUnisexAdidasSpider,
        'gdlp-kids-adidas' : GDLPKidsAdidasSpider,
        'gdlp-male-adidas-consortium' : GDLPMaleAdidasConsortiumSpider,
        'gdlp-unisex-adidas-consortium' : GDLPUnisexAdidasConsortiumSpider,
        'gdlp-male-adidas-y3' : GDLPMaleAdidasY3Spider,
        'gdlp-unisex-adidas-y3' : GDLPUnisexAdidasY3Spider,
        'gdlp-unisex-nike' : GDLPUnisexNikeSpider,
        'gdlp-kids-nike' : GDLPKidsNikeSpider,
        'gdlp-male-nike' : GDLPMaleNikeSpider,
        'gdlp-female-nike' : GDLPFemaleNikeSpider,
        'gdlp-male-jordan' : GDLPMaleJordanSpider,
        'gdlp-unisex-jordan' : GDLPUnisexJordanSpider,
        'gdlp-kids-jordan' : GDLPKidsJordanSpider
    }
    crawl_settings = get_project_settings()
    settings_module_path = os.environ.get("SCRAPY_ENV", "gdlp.settings")
    crawl_settings.setmodule(settings_module_path)
    configure_logging(crawl_settings)
    runner = CrawlerRunner(crawl_settings)
    d = runner.crawl(spider[brand])
    d.addBoth(lambda _: reactor.stop())
    reactor.run() 


if __name__ == "__main__":
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = settings.get("store.GOOGLE_APPLICATION_CREDENTIALS")
    app()