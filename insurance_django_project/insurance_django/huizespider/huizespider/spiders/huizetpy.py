# -*- coding: utf-8 -*-
import scrapy
import json
import re
from pymongo import MongoClient

class HuizetpySpider(scrapy.Spider):
    name = 'huizetpy'
    allowed_domains = ['huize.com']
    start_urls = ['https://www.huize.com/apps/cps/index/product/detail?prodId=101868&planId=104316']

    def parse(self, response):
        yield scrapy.Request(
            url='https://www.huize.com/apps/cps/index/product/detail?prodId=101868&planId=104316',
            callback=self.parse_twice,
        )

    def parse_twice(self, response):
        item = {
            'name': '',  # 保单名称
            'lable': list(),  # 保单标签
            'equity': list(),  # 用户拥有权力
            'notice': list(),  # 投保须知

            'sex': list(),  # 性别
            'insurantJob': list(),  # 承保职业
            'insurantDateLimit': list(),  # 保障期限
            'paymentType': list(),  # 缴费类型
            'insureAgeLimit': list(),  # 缴费年限
            'premium': list(),  # 年交保费
            'isInsure': list(),  # 荣耀金万能账户

            'protect_interest': list(),  # 保障权益
            'image_url': list()  # 介绍图片

        }

        div_list = response.xpath('//div[@class="detail-primary"]')

        """ 
        保单名称 

        """
        item['name'] = div_list.xpath(
            '//h2[@class="product-title f26"]/text()').extract_first().strip()

        """ 
        保单标签 

        """
        for i in div_list.xpath('//div[@class="detail-ensure-body"]/div[1]//ul/li/text()').extract():
            if i.strip().replace('\n', ''): item['lable'].append(i.strip().replace('\n', ''))

        """ 
        用户拥有权力 

        """
        equity_li = div_list.xpath('//div[4]/ul//li/dl')
        for i, j in enumerate(equity_li.xpath('dt/text()').extract()):
            item['equity'].append('{}:{}'.format(j.strip(), equity_li.xpath('dd/text()').extract()[i].strip()))

        """ 
        投保须知 

        """
        notice_li = div_list.xpath('//div[4]/div/div/ol/li')
        for i in notice_li:
            item['notice'].append(i.xpath('.//text()').extract())
        for index, i in enumerate(item['notice']):
            temp = ''
            for j in item['notice'][index]:
                temp = temp + j.strip().replace('\n', '').replace('\t', '')
            item['notice'][index] = temp

        """
        介绍图片

        """
        image_li = div_list.xpath('div/div/div/img/@src')
        for i in image_li:
            item['image_url'].append(i.extract())

        yield scrapy.Request(
            url='https://www.huize.com/apps/cps/product/getTrial?callback=jQuery18209275240988152709_1588572271314&uid=10000000&prodId=101868&planId=104316&_=1588572271363',
            callback=self.parse_option,
            meta={"item": item}
        )

    def parse_option(self, response):
        """
        抓取保单选项
        """

        item = response.meta['item']
        str_json = re.compile("&& jQuery18209275240988152709_1588572271314\((.*)\);").findall(response.text)
        data_list = json.loads(str_json[0], encoding='utf-8')
        data = data_list['data']['restrictGenes']
        # 性别
        for i in data[1]['dictionaryList']:
            item['sex'].append(i['value'])

        # 承保职业
        for i in data[2]['dictionaryList']:
            item['insurantJob'].append(i['value'])

        # 保障期限
        for i in data[3]['dictionaryList']:
            item['insurantDateLimit'].append(i['value'])

        # 缴费类型
        for i in data[4]['dictionaryList']:
            item['paymentType'].append(i['value'])

        # 缴费年限
        for i in data[5]['dictionaryList']:
            item['insureAgeLimit'].append(i['value'])

        # 年交保费
        for i in data[6]['dictionaryList']:
            item['premium'].append({'value': i['value'],
                                    'min': i['min'],
                                    'max': i['max'],
                                    'step': i['step']})

        # 荣耀金万能账户
        for i in data[7]['dictionaryList']:
            item['isInsure'].append(i['value'])

        # 保障权益
        protect_interest_data = data_list['data']['protectTrialItemList']
        for i in protect_interest_data:
            try:
                item['protect_interest'].append({'name': i['name'],
                                                 'fullPremium': i['fullPremium'],
                                                 'description': i['description']})
            except Exception as e:
                pass
        del item['protect_interest'][len(item['protect_interest']) - 1]

        # 建立和mongodb的连接
        client = MongoClient(host="121.43.189.184", port=27017)

        # 选择要操作的数据库和集合
        collection = client["insurance_django"]["insurance_data_tpy"]
        collection.update_one({"name": "太平财富智赢年金保险+荣耀金账户终身寿险（万能型）"}, {"$set": item})
