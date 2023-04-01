# -*- coding: utf-8 -*-

# Scrapy settings for huizespider project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'huizespider'

SPIDER_MODULES = ['huizespider.spiders']
NEWSPIDER_MODULE = 'huizespider.spiders'

LOG_LEVEL = "WARNING"

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'huizespider (+http://www.yourdomain.com)'

USER_AGENT = 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}
# DEFAULT_REQUEST_HEADERS = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
#     "Cookie": 'Hm_lvt_b7dc461be4b3f1b75d87c1f2c7922b77=1588564267; Hm_lvt_c66b712e1cd824cd55156dbf5089342b=1588564267; Hm_lvt_27ca7fb7008b01737e4fc53e00aa3b35=1588564270; _ga=GA1.2.648842059.1588564270; _bl_uid=hmk179UwrIIyF157qfkto3wdjbO8; introductionUrl=; _qxc_token_=d0bb6dbb-018c-4406-a61e-19d6e6807dea; union.flowtoken=cf04f942-9a9d-42d7-9677-d2c3e2571bb2; SSO-ACCESS-TOKEN=f2dd8e9d-a4f9-48cc-a57c-a5cc94efa4b1; userId=4Oicpe/JV9A=; Product_History=101868%3A104316%2C101804%3A104175%2C101862%3A104302%2C101832%3A104245; UtmCookieKey={"UtmSource":"","UtmMedium":"","UtmTerm":"","UtmContent":"","UtmCampaign":"","UtmUrl":"https://www.huize.com/","UtmSE":"","Keywords":"","CampaignCode":"","UrlSource":"https%3a%2f%2fwww.huize.com%2fapps%2fcps%2findex%2fproduct%2fdetail%3fprodId%3d101868%26planId%3d104316"}; UtmCookieKeyEncode=%7b%22UtmSource%22%3a%22%22%2c%22UtmMedium%22%3a%22%22%2c%22UtmTerm%22%3a%22%22%2c%22UtmContent%22%3a%22%22%2c%22UtmCampaign%22%3a%22%22%2c%22UtmUrl%22%3a%22https%3a%2f%2fwww.huize.com%2f%22%2c%22UtmSE%22%3a%22%22%2c%22Keywords%22%3a%22%22%2c%22CampaignCode%22%3a%22%22%2c%22UrlSource%22%3a%22https%253a%252f%252fwww.huize.com%252fapps%252fcps%252findex%252fproduct%252fdetail%253fprodId%253d101868%2526planId%253d104316%22%7d; acw_tc=2f6a1fcc15886062438296046eda1de7d09678f7b523d17174a9d7068ca159; hz_guest_key=4aR1J9IkvHZYmyfDOt6_1588564270918_7_4Oicpe/JV9A%3D_0; _gat=1; hz_visit_key=ywDpeHGfHZBQ74zx6F_1588606243106_4_1588606243106; hz_view_key=4aR1J9IkvHZYmyfDOt613LfkD253HZ1ixgpvyIj_1588607297937_https%253A%252F%252Fwww.huize.com%252Fapps%252Fcps%252Findex%252Fproduct%252Fdetail%253FprodId%253D101868%2526planId%253D104316; Hm_lpvt_c66b712e1cd824cd55156dbf5089342b=1588607298; Hm_lpvt_b7dc461be4b3f1b75d87c1f2c7922b77=1588607298; Hm_lpvt_27ca7fb7008b01737e4fc53e00aa3b35=1588607298',
# }


# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'huizespider.middlewares.HuizespiderSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'huizespider.middlewares.HuizespiderDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'huizespider.pipelines.HuizespiderPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
