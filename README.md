
░█████╗░░█████╗░████████╗░█████╗░████████╗███████╗███╗░░██╗██╗░██████╗
██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗╚══██╔══╝██╔════╝████╗░██║██║██╔════╝
██║░░╚═╝██║░░██║░░░██║░░░███████║░░░██║░░░█████╗░░██╔██╗██║██║╚█████╗░
██║░░██╗██║░░██║░░░██║░░░██╔══██║░░░██║░░░██╔══╝░░██║╚████║██║░╚═══██╗
╚█████╔╝╚█████╔╝░░░██║░░░██║░░██║░░░██║░░░███████╗██║░╚███║██║██████╔╝
░╚════╝░░╚════╝░░░░╚═╝░░░╚═╝░░╚═╝░░░╚═╝░░░╚══════╝╚═╝░░╚══╝╚═╝╚═════╝░


--------------------------------------------------------------------------

# Web crawler

url: [https://gdlp.com.br/](https://gdlp.com.br/)

# 1. Configuration
Before you run this project and for the proper running of this program you need to set up some variables inside `gdlp/gdlp/settings.py`.

## 1.1 SENTRY
This project utilizes [SENTRY](https://sentry.io/) for error tracking.

- `SPIDERMON_SENTRY_DSN`
- `SPIDERMON_SENTRY_PROJECT_NAME`
- `SPIDERMON_SENTRY_ENVIRONMENT_TYPE`

## 1.2 GOOGLE CLOUD PLATFORM

- `GCS_PROJECT_ID` 
- `GCP_CREDENTIALS`
- `GCP_STORAGE`
- `GCP_STORAGE_CRAWLER_STATS`
- `IMAGES_STORE`

## 1.3 DISCORD
- `DISCORD_WEBHOOK_URL`
- `DISCORD_THUMBNAIL_URL`
- `SPIDERMON_DISCORD_WEBHOOK_URL`


# 2. Implemented Brands
- gdlp-male-adidas [`GDLPMaleAdidasSpider`]
- gdlp-female-adidas [`GDLPFemaleAdidasSpider`]
- gdlp-unisex-adidas [`GDLPUnisexAdidasSpider`]
- gdlp-kids-adidas [`GDLPKidsAdidasSpider`]
- gdlp-male-adidas-consortium [`GDLPMaleAdidasConsortiumSpider`]
- gdlp-unisex-adidas-consortium [`GDLPUnisexAdidasConsortiumSpider`]
- gdlp-male-adidas-y3 [`GDLPMaleAdidasY3Spider`]
- gdlp-unisex-adidas-y3 [`GDLPUnisexAdidasY3Spider`]
- gdlp-unisex-nike [`GDLPUnisexNikeSpider`]
- gdlp-kids-nike [`GDLPKidsNikeSpider`] 
- gdlp-male-nike [`GDLPMaleNikeSpider`]
- gdlp-female-nike [`GDLPFemaleNikeSpider`]
- gdlp-male-jordan [`GDLPMaleJordanSpider`]
- gdlp-unisex-jordan [`GDLPUnisexJordanSpider`]
- gdlp-kids-jordan [`GDLPKidsJordanSpider`]

# 3. Build

```shell
cd gdlp
make docker-build-production
```

# 4. Publish

```shell
make docker-publish-production
```

# 5. Use
- The parameter `brand` could receive one of the following values: [`gdlp-male-adidas`, `gdlp-female-adidas`, `gdlp-unisex-adidas`, `gdlp-kids-adidas`, `gdlp-male-adidas-consortium`, `gdlp-unisex-adidas-consortium`, `gdlp-male-adidas-y3`, `gdlp-unisex-adidas-y3`, `gdlp-unisex-nike`, `gdlp-kids-nike`, `gdlp-male-nike`, `gdlp-female-nike`, `gdlp-male-jordan`, `gdlp-unisex-jordan`, `gdlp-kids-jordan`].

```shell
docker run --shm-size="2g" gcr.io/cotatenis/cotatenis-crawl-gdlp:0.7.1 --brand=gdlp-male-adidas
```
