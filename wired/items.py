# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WiredItem(scrapy.Item):
    article_id = scrapy.Field()             # resp['primary']['items'][i]['id']
    author = scrapy.Field()                 # resp['primary']['items'][i]['contributors']['author'][0]['name']
    category = scrapy.Field()               # resp['primary']['items'][i]['categories']['sections'][0]['name']
    published_date = scrapy.Field()         # resp['primary']['items'][i]['dateFormats']['m.d.y']
    published_time = scrapy.Field()         # resp['primary']['items'][i]['dateFormats']['g:i a']
    # published_stamp = scrapy.Field()        # resp['primary']['items'][i]['dateFormats']['c']
    title = scrapy.Field()                  # resp['primary']['items'][i]['hed']
    # img_id = scrapy.Field()                 # resp['primary']['items'][i]['photos']['tout'][0]['id']
    # img_filename = scrapy.Field             # resp['primary']['items'][i]['photos']['tout'][0]['filename']
    img_url = scrapy.Field()                # https://media.wired.com/photos/img_url/master/w_582,c_limit/img_filename
    img_caption = scrapy.Field()            # resp['primary']['items'][i]['photos']['tout'][0]['caption']
    img_credit = scrapy.Field()             # resp['primary']['items'][i]['photos']['tout'][0]['credit']
    content = scrapy.Field()                # resp['primary']['items'][i]['body']
    stamp_time = scrapy.Field()
