BOT_NAME = 'gdlp'
VERSION = '0-7-1'
SPIDER_MODULES = ['gdlp.spiders']
NEWSPIDER_MODULE = 'gdlp.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False
MAGIC_FIELDS = {
    "timestamp": "$isotime",
    "spider": "$spider:name",
    "url": "$response:url",
}
SPIDER_MIDDLEWARES = {
    "scrapy_magicfields.MagicFieldsMiddleware": 100,
}
SPIDERMON_ENABLED = True
EXTENSIONS = {
    'gdlp.extensions.SentryLogging' : -1,
    'spidermon.contrib.scrapy.extensions.Spidermon': 500,
}
ITEM_PIPELINES = {
    "gdlp.pipelines.DiscordMessenger" : 100,
    "gdlp.pipelines.GDLPImagePipeline" : 200,
    "gdlp.pipelines.GCSPipeline": 300,
    "spidermon.contrib.scrapy.pipelines.ItemValidationPipeline": 400,

}
SPIDERMON_VALIDATION_MODELS = (
    'gdlp.validators.GDLPItem',
)

SPIDERMON_SPIDER_CLOSE_MONITORS = (
'gdlp.monitors.SpiderCloseMonitorSuite',
)

SPIDERMON_VALIDATION_DROP_ITEMS_WITH_ERRORS = False
SPIDERMON_PERIODIC_MONITORS = {
'gdlp.monitors.PeriodicMonitorSuite': 30, # time in seconds
}
SPIDERMON_CUSTOM_MIN_ITEMS = {
    'gdlp-male-adidas' : 120,
    'gdlp-female-adidas' : 25,
    'gdlp-kids-adidas' : 2,
    'gdlp-male-adidas-consortium' : 3,
    'gdlp-male-adidas-y3' : 25,
    'gdlp-unisex-adidas-consortium' : 1,
    'gdlp-unisex-adidas-y3' : 1,
    'gdlp-unisex-adidas' : 40,
    'gdlp-unisex-nike' : 7,
    'gdlp-kids-nike' : 1,
    'gdlp-male-nike' : 70,
    'gdlp-female-nike' : 7,
    'gdlp-male-jordan' : 7,
    'gdlp-unisex-jordan' : 1,
    'gdlp-kids-jordan' : 1,
}
SPIDERMON_SENTRY_DSN = ""
SPIDERMON_SENTRY_PROJECT_NAME = ""
SPIDERMON_SENTRY_ENVIRONMENT_TYPE = ""
#THROTTLE
AUTOTHROTTLE_ENABLED = True
AUTOTHROTTLE_START_DELAY = 2
AUTOTHROTTLE_MAX_DELAY = 5

#GCP
GCS_PROJECT_ID = ""
GCP_CREDENTIALS = ""
GCP_STORAGE = ""
GCP_STORAGE_CRAWLER_STATS = ""
#FOR IMAGE UPLOAD
IMAGES_STORE = f''
IMAGES_THUMBS = {
    '400_400': (400, 400),
}

#DISCORD
DISCORD_WEBHOOK_URL = ""
DISCORD_THUMBNAIL_URL = ""
SPIDERMON_DISCORD_WEBHOOK_URL = ""

#LOG LEVEL
LOG_LEVEL='INFO'