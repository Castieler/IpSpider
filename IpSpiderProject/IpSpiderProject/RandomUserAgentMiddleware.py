from .settings import USER_AGENT_LIST

import random
class RandomUserAgentMiddleware(object):
    def process_request(self, request, spider):
        ua  = random.choice(USER_AGENT_LIST)
        if ua:
            request.headers.setdefault('User-Agent', ua)
            request.headers.setdefault('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8')
            request.headers.setdefault('Accept-Encoding', 'gzip, deflate')
            request.headers.setdefault('Accept-Language', 'zh-CN,zh;q=0.9')
            request.headers.setdefault('Cache-Control', 'max-age=0')
            request.headers.setdefault('Connection', 'keep-alive')
            request.headers.setdefault('Connection', 'keep-alive')
            request.headers.setdefault('Upgrade-Insecure-Requests', '1')
            request.headers.setdefault('Host', 'www.xicidaili.com')