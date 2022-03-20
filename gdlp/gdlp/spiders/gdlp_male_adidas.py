from scrapy.http.request import Request
from scrapy import Spider
from scrapy.linkextractors import LinkExtractor
from gdlp.items import GDLPItem
from scrapy.loader import ItemLoader
import json
from scrapy.utils.project import get_project_settings
import re
from typing import List, Dict
from parsel import Selector
import undetected_chromedriver as uc
from scrapy import signals
from time import sleep
from w3lib.html import remove_tags
class GDLPMaleAdidasSpider(Spider):
    settings = get_project_settings()
    name = 'gdlp-male-adidas'
    version = settings.get("VERSION")
    allowed_domains = ['gdlp.com.br']
    start_urls = [
         #masculino
        'https://gdlp.com.br/calcados/adidas/g%C3%AAnero/masculino'
    ]
    @classmethod
    def from_crawler(cls, crawler, *args, **kwargs):
        spider = super(GDLPMaleAdidasSpider, cls).from_crawler(crawler, *args, **kwargs)
        crawler.signals.connect(spider.spider_opened, signal=signals.spider_opened)
        crawler.signals.connect(spider.spider_closed, signal=signals.spider_closed)
        return spider
    
    def spider_opened(self, spider):
        options = uc.ChromeOptions()
        options.add_argument('--no-first-run --no-service-autorun --password-store=basic')
        options.add_argument('--headless')
        self.browser = uc.Chrome(options=options)
    
    def spider_closed(self, spider):
        self.browser.close()

    def start_requests(self):
        for url in self.start_urls:
            yield Request(
                url=url, 
                callback=self.results_page, 
            )

    def results_page(self, response):
        self.logger.debug(response.url)
        product_details = LinkExtractor(restrict_xpaths="//li[@class='item last']/a")
        for link in product_details.extract_links(response=response):
            self.browser.get(link.url)
            selector = Selector(text=self.browser.page_source)
            sizes_and_stock = self.parse_sizes_and_stock(selector=selector)
            product_info = self.parse_product_labels(selector=selector, url=link.url)
            if product_info:
                sku = remove_tags(selector.xpath("//th[contains(text(), 'SKU no Fornecedor')]/..//td").get())
                images = selector.xpath("//div[contains(@id,'MagicToolboxSelectors')]//a/@href").getall()
                image_uris = [f"{self.settings.get('IMAGES_STORE')}{sku}_{filename.split('/')[-1]}" for filename in images]
                product_container = selector.xpath("//div[starts-with(@class, 'product-view')]")
                reference_first_image = f"{sku}_{images[0].split('/')[-1]}"
                i = ItemLoader(item=GDLPItem(), selector=product_container)
                i.add_xpath("product", "//div[starts-with(@class, 'product-name')]/span")
                i.add_value("url", link.url)
                i.add_xpath("description", "//div[starts-with(@class, 'short-description')]/div")
                i.add_value("product_info", product_info)
                i.add_xpath("sku", "//th[contains(text(), 'SKU no Fornecedor')]/..//td")
                i.add_value("image_uris", image_uris)
                i.add_value("image_urls", images)
                i.add_value("reference_first_image", reference_first_image)
                i.add_value("genre", self.name.split("-")[1])
                i.add_value("spider_version", self.version)
                i.add_value("spider", self.name)
                i.add_value("sizes_and_stock", sizes_and_stock)
                yield i.load_item()
            else:
                self.logger.error(f"Não foi possível processar corretamente a url {link.url}")
        
        pagination = LinkExtractor(restrict_xpaths=("//div[@class='pages']//li/a"))
        for link in pagination.extract_links(response):
            yield Request(url=link.url, callback=self.results_page)

    def parse_sizes_and_stock(self, selector) -> List[Dict[str, bool]]:
        container_of_sizes_and_stock = []
        sizes = selector.xpath("//ul[@id='configurable_swatch_magework_numeracao']//li/@class").getall()
        #identify sizes without stock
        sizes_without_stock = [re.search(r"\d+", d).group(0) for d in sizes if re.search(".+(not-available)", d)]
        if sizes_without_stock:
            for size in sizes_without_stock:
                container_of_sizes_and_stock.append({
                    'size' : size,
                    'in_stock' : False
                })
        #identify sizes with stock
        try:
            sizes_with_stock = [re.search(r"\d+", d).group(0) for d in sizes if not re.search(".+(not-available)", d)]
        except AttributeError:
            #página informando tênis com tamanho m, g, p
            pass
        else:
            if sizes_with_stock:
                for size in sizes_with_stock:
                    container_of_sizes_and_stock.append({
                        'size' : size,
                        'in_stock' : True
                    })
        return container_of_sizes_and_stock

    def parse_product_labels(self, selector, url) -> List:
        """Process content inside several script tags to get information 
        about stock availability and shoes sizes. 

        Parameters
        ----------
        selector : Selector
        Returns
        -------
        [list]
            list of objects
        """
        # parse script
        o = selector.xpath("//script[contains(text(), 'window.dataLayer = window.dataLayer')]").get()
        if o:
            rindex = o.rfind('window.dataLayer.push')
            ob = o[:rindex].strip()[:-2]
            lindex = ob.find("window.dataLayer.push")
            ob = ob[lindex:]
            _index = ob.find("(")+1
            ob = ob[_index:]
            ob = json.loads(ob)
            return ob
        else:
            sleep(2)
            new_selector = Selector(self.browser.page_source)
            o = new_selector.xpath("//script[contains(text(), 'window.dataLayer = window.dataLayer')]").get()
            if o:
                rindex = o.rfind('window.dataLayer.push')
                ob = o[:rindex].strip()[:-2]
                lindex = ob.find("window.dataLayer.push")
                ob = ob[lindex:]
                _index = ob.find("(")+1
                ob = ob[_index:]
                ob = json.loads(ob)
                return ob
            else:
                return None