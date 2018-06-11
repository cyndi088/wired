# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WiredItem(scrapy.Item):
    author = scrapy.Field()                 # resp['primary']['items'][0]['contributors']['author'][0]['name']
    category = scrapy.Field()               # resp['primary']['items'][0]['categories']['sections'][0]['name']
    published_date = scrapy.Field()         # resp['primary']['items'][0]['dateFormats']['m.d.y']
    published_time = scrapy.Field()         # resp['primary']['items'][0]['dateFormats']['g:i a']
    # published_stamp = scrapy.Field()        # resp['primary']['items'][0]['dateFormats']['c']
    title = scrapy.Field()                  # resp['primary']['items'][0]['hed']
    # img_id = scrapy.Field()                 # resp['primary']['items'][0]['photos']['tout'][0]['id']
    # img_filename = scrapy.Field             # resp['primary']['items'][0]['photos']['tout'][0]['filename']
    img_url = scrapy.Field()                # https://media.wired.com/photos/img_url/master/w_582,c_limit/img_filename
    img_caption = scrapy.Field()            # resp['primary']['items'][0]['photos']['tout'][0]['caption']
    img_credit = scrapy.Field()             # resp['primary']['items'][0]['photos']['tout'][0]['credit']
    content = scrapy.Field()                # resp['primary']['items'][0]['body']
    stamp_time = scrapy.Field()
