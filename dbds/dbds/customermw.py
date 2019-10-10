from scrapy.http.request import Request
import random

class ProxyDownloaderMiddleware(object):
    proxy_ip = '218.95.37.227'
    proxy_port = '3128'
    proxies = ['http://{}:{}'.format(proxy_ip, proxy_port)]

    def process_request(self, request:Request, spider):
        request.meta['proxy'] = random.choice(self.proxies)
        print('[URL]', request.url)