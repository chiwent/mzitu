# -*- coding: utf-8 -*-


BOT_NAME = 'mzitu'

SPIDER_MODULES = ['mzitu.spiders']
NEWSPIDER_MODULE = 'mzitu.spiders'




USER_AGENTS = [
    'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0)',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.2)',
    'Opera/9.27 (Windows NT 5.2; U; zh-cn)',
    'Opera/8.0 (Macintosh; PPC Mac OS X; U; en)',
    'Mozilla/5.0 (Macintosh; PPC Mac OS X; U; en) Opera 8.0',
    'Mozilla/5.0 (Linux; U; Android 4.0.3; zh-cn; M032 Build/IML74K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30',
    'Mozilla/5.0 (Windows; U; Windows NT 5.2) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/0.2.149.27 Safari/525.13',
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.75 Safari/535.7",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.75 Safari/535.7",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.120 Safari/535.2",
    "Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.2 (KHTML, like Gecko) Ubuntu/10.04 Chromium/15.0.874.106 Chrome/15.0.874.106 Safari/535.2",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_2) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.106 Safari/535.2",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.5; rv:8.0.1) Gecko/20100101 Firefox/8.0.1",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:9.0.1) Gecko/20100101 Firefox/9.0.1",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:9.0.1) Gecko/20100101 Firefox/9.0.1",
]


PROXIES = [
    {"ip_prot":"219.254.34.231:3128","user_passwd":""},
    {"ip_prot":"113.255.181.162:8380","user_passwd":""},
    {"ip_prot":"112.78.38.178:53281","user_passwd":""},
    {"ip_prot":"120.78.59.193:8080","user_passwd":""},
    {"ip_prot":"113.203.238.179:8080","user_passwd":""},
    {"ip_prot":"59.106.216.158:60088","user_passwd":""},
    {"ip_prot":"103.210.33.44:53281","user_passwd":""},
    {"ip_prot":"109.236.113.2:8080","user_passwd":""},
    {"ip_prot":"190.2.144.128:1080","user_passwd":""},
    {"ip_prot":"101.96.10.58:8080","user_passwd":""},
    {"ip_prot":"121.69.37.238:8118","user_passwd":""},
    {"ip_prot":"201.184.105.122:8080","user_passwd":""},
    {"ip_prot":"201.38.93.179:3128","user_passwd":""},
    {"ip_prot":"103.75.160.51:53281","user_passwd":""},
    {"ip_prot":"151.106.52.235:1080","user_passwd":""},
    {"ip_prot":"138.118.84.249:53281","user_passwd":""},
    {"ip_prot":"59.152.95.158:8080","user_passwd":""},
    {"ip_prot":"190.2.142.6:1080","user_passwd":""},
    {"ip_prot":"125.25.57.40:8080","user_passwd":""},
    {"ip_prot":"112.115.57.20:3128","user_passwd":""},
    {"ip_prot":"104.237.227.222:3128","user_passwd":""},
    {"ip_prot":"59.106.213.54:60088","user_passwd":""},
    {"ip_prot":"39.104.53.175:8080","user_passwd":""},
    {"ip_prot":"45.235.87.26:53281","user_passwd":""},
    {"ip_prot":"45.125.32.178:3128","user_passwd":""},
    {"ip_prot":"185.252.40.159:53281","user_passwd":""},
    {"ip_prot":"123.114.206.167:8118","user_passwd":""},
    {"ip_prot":"106.14.137.97:80","user_passwd":""},
    {"ip_prot":"185.252.40.136:53281","user_passwd":""},
    {"ip_prot":"165.90.95.89:53281","user_passwd":""},
    {"ip_prot":"177.8.216.106:8080","user_passwd":""},
    {"ip_prot":"119.28.203.242:8000","user_passwd":""},
    {"ip_prot":"74.210.184.16:53281","user_passwd":""},
    {"ip_prot":"122.54.105.143:53281","user_passwd":""},
    {"ip_prot":"103.206.168.177:53281","user_passwd":""},
    {"ip_prot":"103.60.173.58:8080","user_passwd":""},
    {"ip_prot":"103.204.210.112:8080","user_passwd":""},
    {"ip_prot":"114.250.25.19:80","user_passwd":""},

]

DOWNLOADER_MIDDLEWARES = {
   'mzitu.middlewares.MzituSpiderMiddleware': 500,
   'mzitu.middlewares.RandomUserAgent': 400,
   'mzitu.middlewares.RandomProxy': 750,
}





ITEM_PIPELINES = {
   'mzitu.pipelines.MzituPipeline': 300,

}

# 图片保存地址
IMAGES_STORE = 'F:\mzitu\\'


# 30 days of delay for images expiration
IMAGES_EXPIRES = 30