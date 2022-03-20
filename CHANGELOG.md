# Change Log
Arquivo para documentação das mudanças realizadas ao longo do projeto. O formato desse arquivo é baseado no [Keep a Changelog](http://keepachangelog.com/)
e o presente projeto adota o [Semantic Versioning](http://semver.org/).

## [0.7.1] - 2021-11-22
### [COT-315](https://ecoanalytics.atlassian.net/browse/COT-315) 

## [0.7.0] - 2021-11-01
### [COT-304](https://ecoanalytics.atlassian.net/browse/COT-304) 
#### Adicionado
- Adicionado as spiders [`GDLPUnisexNikeSpider`, `GDLPKidsNikeSpider`, `GDLPMaleNikeSpider`, `GDLPFemaleNikeSpider`, `GDLPMaleJordanSpider`, `GDLPUnisexJordanSpider`, `GDLPKidsJordanSpider`]
- Adicionado o atributo `sku` ao objeto `GDLPItem`.
#### Alterado
- Alterado a função `process_item` para que itens que não possuem sku sejam dropados pelo pipeline.

## [0.6.0] - 2021-10-22
### [COT-246](https://ecoanalytics.atlassian.net/browse/COT-246) 
#### Adicionado
- Adicionado `undetected-chromedriver` como dependência ao projeto.
#### Removido
- Removido `scrapy-selenium` como dependência ao projeto.

## [0.5.1] - 2021-10-17
### [COT-246](https://ecoanalytics.atlassian.net/browse/COT-246) 
#### Adicionado
- Adicionado proteção para evitar AttributeError durante a coleta.
#### Removido
- Retirado a persistência de imagens na dimensão 800x600.

## [0.5.0] - 2021-10-13
### [COT-244](https://ecoanalytics.atlassian.net/browse/COT-244) 
#### Adicionado
- Adicionado `scrapy-selenium` como dependência ao projeto.
- Adicionado o atributo `sizes_and_stock` ao objeto `GDLPItem`
- Adicionado um novo monitor `ItemCountMonitor`.

## [0.4.0] - 2021-10-10
### [COT-204](https://ecoanalytics.atlassian.net/browse/COT-204) 
#### Adicionado
- Adicionado a feature `reference_first_image` ao objeto `GDLPItem`.
#### Alterado
- Alterado o parâmetro `IMAGES_THUMBS` para coletar imagens no padrão 400x400.
- Alterado o padrão de nomenclatura das imagens salvas, adicionando o SKU como prefixo.

## [0.3.2] - 2021-10-04
### [COT-164](https://ecoanalytics.atlassian.net/browse/COT-164) 
#### Alterado
- [Sentry ISSUE](https://sentry.io/share/issue/e71b835e6eff4da388479d4c0fee56ed/)

## [0.3.1] - 2021-10-04
### [COT-154](https://ecoanalytics.atlassian.net/browse/COT-147) 
#### Adicionado
- Adicionado monitoramento via [sentry](https://sentry.io/)
- Adicionado novos monitores: `FinishReasonMonitor`, `UnwantedHTTPCodesMonitor`, `ErrorCountMonitor`

## [0.6.0] - 2021-10-22
### [COT-264](https://ecoanalytics.atlassian.net/browse/COT-264) 
#### Adicionado
- Adicionado [undetected_chromedriver](https://github.com/ultrafunkamsterdam/undetected-chromedriver)
#### Removido
- Removido [scrapy-selenium](https://github.com/clemfromspace/scrapy-selenium)

## [0.3.0] - 2021-10-03
### [COT-147](https://ecoanalytics.atlassian.net/browse/COT-147) 
#### Adicionado
- Adicionado monitoramento via [spidermon](https://github.com/scrapinghub/spidermon)

## [0.2.0] - 2021-09-22
### [COT-109](https://ecoanalytics.atlassian.net/browse/COT-109) 
#### Retirado
- Removido o pacote `scrapy-fieldstats` do projeto.
#### Adicionado
- Adicionado o pacote `Pillow` do projeto.
- Adicionado a classe `GDLPImagePipeline` ao pipeline de processamento.
- Adicionado a persistência de imagens ao bucket `gs://cotatenis-images`
- Adicionado o **field** `image_uris` a classe `GDLPItem`.
#### Alterado
- Modificado o parâmetro `LOG_LEVEL` para `INFO`
