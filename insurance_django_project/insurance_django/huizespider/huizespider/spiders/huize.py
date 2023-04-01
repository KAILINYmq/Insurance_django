# -*- coding: utf-8 -*-
import json
from pymongo import MongoClient
import scrapy


class HuizeSpider(scrapy.Spider):
    name = 'huize'
    allowed_domains = ['huize.com']
    start_urls = ['https://www.huize.com/product/detail-101804.html?DProtectPlanId=104175']

    def parse(self, response):
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
            'premium': list(),  # 保费
            'coverageAreaName': list(),  # 投保地区

            'protect_interest': list(),  # 保障权益
            'image_url': list()  # 介绍图片

        }
        div_list = response.xpath('//div[@class="detail-ensure-body"]')

        """ 
        保单名称 
        
        """
        item['name'] = div_list.xpath('div[@id="trialWrap"]/div[@class="trial-area"]/div/h2/text()').extract_first().strip()

        """ 
        保单标签 
        
        """
        for i in div_list.xpath('div[@id="trialWrap"]/div[@class="trial-area"]/ul//li/text()').extract():
            item['lable'].append(i)

        """ 
        用户拥有权力 
        
        """
        equity_li = div_list.xpath('div[2]/ul//li/dl')
        for i, j in enumerate(equity_li.xpath('dt/text()').extract()):
            item['equity'].append('{}:{}'.format(j.strip(), equity_li.xpath('dd/text()').extract()[i].strip()))

        """ 
        投保须知 
        
        """
        notice_li = div_list.xpath('div[3]/div/ol/li')
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
        image_li = div_list.xpath('div/div/img/@src')
        for i in image_li:
            item['image_url'].append('https:' + i.extract())

        yield scrapy.Request(
            url='https://www.huize.com/product/detail-101804.html?DProtectPlanId=104175&getRules=true',
            callback=self.parse_option,
            meta={"item": item}
        )

    def parse_option(self, response):
        """
        抓取保单选项
        """

        item = response.meta['item']
        data_list = json.loads(response.body.decode())
        data = data_list['restrictRules'][0]['restrictGenes']
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
        item['insureAgeLimit'].append('3年')
        item['insureAgeLimit'].append('5年')

        # 保费
        for i in data[6]['dictionaryList']:
            item['premium'].append({'value': i['value'],
                                        'min': i['min'],
                                        'max': i['max'],
                                        'step': i['step']})

        # 投保地区
        for i in data[7]['dictionaryList']:
            item['coverageAreaName'].append(i['value'])

        # 保障权益
        protect_interest_data = data_list['restrictRules'][0]['protectTrialItemList']
        for i in protect_interest_data:
            try:
                item['protect_interest'].append({'name': i['name'],
                                                 'fullPremium': i['fullPremium'],
                                                 'description': i['description']})
            except Exception as e:
                pass
        del item['protect_interest'][len(item['protect_interest'])-1]

        # 建立和mongodb的连接
        client = MongoClient(host="121.43.189.184", port=27017)

        # 选择要操作的数据库和集合
        collection = client["insurance_django"]["insurance_data_fyj"]
        collection.update_one({"name": "福佑金生年金保险"}, {"$set": item})
