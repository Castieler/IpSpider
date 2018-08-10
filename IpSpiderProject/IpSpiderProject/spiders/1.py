import scrapy
from lxml import etree
from ..items import IpspiderprojectItem
class Ip(scrapy.Spider):
    name = 'ip'
    def start_requests(self):
        start_urls = ['http://www.xicidaili.com/nn/','http://www.xicidaili.com/nt/','http://www.xicidaili.com/wn/','http://www.xicidaili.com/wt/']
        for url in start_urls:
            yield scrapy.Request(url,callback=self.parse)

    def parse(self,response):
        page_num = response.xpath("//div[@class='pagination']/a/text()").extract()[-2]
        if page_num.isdigit():
            for i in range(1,int(page_num)+1):
                url = response.url+str(i)
                yield scrapy.Request(url,callback=self.next)


    def next(self,response):
        tr_list = response.xpath("//tr").extract()
        for each_tr in tr_list[1:]:
            this_item = IpspiderprojectItem()
            html = etree.HTML(each_tr)
            td_list = [i for i in html.xpath("//td[not(@class='country')]//text()") if i.strip()]
            this_item['ip'] = td_list[0]
            this_item['port'] = td_list[1]
            this_item['addr'] = td_list[2]
            this_item['type'] = td_list[3]
            this_item['time_online'] = td_list[4]
            this_item['validate_time'] = td_list[5]
            td_list_2 = html.xpath("//td[@class='country']//div/@title")
            this_item['sudu'] = td_list_2[0]
            this_item['con_time'] = td_list_2[1]
            td_list_3 = html.xpath("//td[@class='country']//text()")
            this_item['anon'] = td_list_3[0]
            print(dict(this_item))
            yield this_item

