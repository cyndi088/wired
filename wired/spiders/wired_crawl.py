# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
import json
from datetime import datetime
from scrapy.utils.project import get_project_settings
from pymongo import MongoClient


class WiredCrawlSpider(scrapy.Spider):
    name = 'wired_crawl'
    allowed_domains = ['www.wired.com']
    start_urls = ['http://www.wired.com/']

    def parse(self, response):
        base_url = response.url
        urls = base_url + 'most-recent/page/%d/?output=json'
        for page in range(1, 10):
            request = Request(urls % page, callback=self.parse_list)
            yield request
        # request = Request(urls % 1, callback=self.parse_list)
        # yield request

    def parse_list(self, response):
        settings = get_project_settings()
        self.client = MongoClient(host=settings['MONGO_HOST'], port=settings['MONGO_PORT'], username=settings['MONGO_USER'], password=settings['MONGO_PSW'])
        self.db = self.client[settings['MONGO_DB']]
        self.coll = self.db[settings['MONGO_COLL']]
        resp = json.loads(response.text)
        for i in range(len(resp['primary']['items'])):
            if self.coll.find_one({"title": self.text_format(resp['primary']['items'][i]['hed'])}) == None:
                item = {}
                # 抓取时间
                item['stamp_time'] = datetime.now()
                # 作者
                if 'author' in resp['primary']['items'][i]['contributors']:
                    item['author'] = resp['primary']['items'][i]['contributors']['author'][0]['name']
                else:
                    item['author'] = ''
                # 分类
                if 'sections' in resp['primary']['items'][i]['categories']:
                    item['category'] = resp['primary']['items'][i]['categories']['sections'][0]['name']
                else:
                    item['category'] = ''
                # 发布日期
                if 'm.d.y' in resp['primary']['items'][i]['dateFormats']:
                    item['published_date'] = resp['primary']['items'][i]['dateFormats']['m.d.y']
                else:
                    item['published_date'] = ''
                # 发布时间
                if 'g:i a' in resp['primary']['items'][i]['dateFormats']:
                    item['published_time'] = resp['primary']['items'][i]['dateFormats']['g:i a']
                else:
                    item['published_time'] = ''
                # 发布时间戳
                # if 'c' in resp['primary']['items'][i]['dateFormats']:
                #     item['published_stamp'] = self.time_stamp(resp['primary']['items'][i]['dateFormats']['c'])
                # else:
                #     item['published_stamp'] = ''
                # 文章标题
                if 'hed' in resp['primary']['items'][i]:
                    item['title'] = self.text_format(resp['primary']['items'][i]['hed'])
                else:
                    item['title'] = ''
                # 图片
                if 'tout' in resp['primary']['items'][i]['photos']:
                    img_id = resp['primary']['items'][i]['photos']['tout'][0]['id']
                    img_filename = resp['primary']['items'][i]['photos']['tout'][0]['filename']
                    # 图片URL
                    item['img_url'] = 'https://media.wired.com/photos/' + img_id + '/master/w_582,c_limit/' + img_filename
                    # 图片注释
                    if 'caption' in resp['primary']['items'][i]['photos']['tout'][0]:
                        item['img_caption'] = resp['primary']['items'][i]['photos']['tout'][0]['caption']
                    else:
                        item['img_caption'] = ''
                    # 图片来源
                    if 'credit' in resp['primary']['items'][i]['photos']['tout'][0]:
                        item['img_credit'] = resp['primary']['items'][i]['photos']['tout'][0]['credit']
                    else:
                        item['img_credit'] = ''
                else:
                    item['img_url'] = ''
                # 文章内容
                if resp['primary']['items'][i]['body'] != '':
                    item['content'] = resp['primary']['items'][i]['body']
                    yield item
                else:
                    item['content'] = ''
                    yield item
            else:
                break
                # continue

    @staticmethod
    def text_format(text):
        if text is None:
            return None
        return text.replace('\n', '').replace('\t', '').replace('<em>', '').replace('</em>', '').replace('&#39;', "'").replace('&amp;', '&').strip()

    # @staticmethod
    # def time_stamp(str):
    #     dt = datetime.strptime(str, '%Y-%m-%dT%H:%M:%S.%fZ')
    #     unixtime = dt.timestamp()
    #     return unixtime