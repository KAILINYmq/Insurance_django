# -*- coding: utf-8 -*-
import json
from pymongo import MongoClient
import scrapy


class HuizezabbSpider(scrapy.Spider):
    name = 'huizezabb'
    allowed_domains = ['huize.com']
    start_urls = ['https://www.huize.com/product/detail-101832.html?DProtectPlanId=104245']

    def parse(self, response):
        item = {
            'name': '',  # 保单名称
            'lable': list(),  # 保单标签
            'equity': list(),  # 用户拥有权力
            'notice': list(),  # 投保须知

            'policyholderExemption': list(),  # 投保人保费豁免
            'additionalInsureAgeLimit': list(),  # 投保人保费豁免缴费年限
            'vesterSex': list(),  # 投保人性别
            'sex': list(),  # 被保险人性别
            'province': list(),  # 投保地区
            'leastamount': list(),  # 基本保额
            'insurantDateLimit': list(),  # 保障期限
            'insureAgeLimit': list(),  # 缴费年限
            'paymentType': list(),  # 缴费类型
            'seniorUniversityEdu': list(),  # 高中大学教育年金保额
            'seriousIllness': list(),  # 重大疾病保险保额
            'hospitalAllowance': list(),  # 长期住院津贴保额
            'accidentalInjury': list(),  # 长期意外伤害医疗保险保额
            'regular': list(),  # 臻爱定期寿险保额
            'additionalRiskPeriod': list(),  # 高中大学教育年金保障期限

            'protect_interest': list(),  # 保障权益
            'image_url': list()  # 介绍图片

        }
        div_list = response.xpath('//div[@class="detail-ensure-body"]')

        """ 
        保单名称 

        """
        item['name'] = div_list.xpath(
            'div[@id="trialWrap"]/div[@class="trial-area"]/div/h2/text()').extract_first().strip()

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
                temp = temp+j.strip().replace('\n', '').replace('\t', '')
            item['notice'][index] = temp

        """
        介绍图片
        
        """
        image_li = div_list.xpath('div/div/img/@src')
        for i in image_li:
            item['image_url'].append('https:' + i.extract())

        yield scrapy.Request(
            url='https://www.huize.com/product/detail-101832.html?DProtectPlanId=104245&getRules=true',
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
        # 投保人保费豁免
        for i in data[1]['dictionaryList']:
            item['policyholderExemption'].append(i['value'])

        # 投保人保费豁免缴费年限
        for i in data[2]['dictionaryList']:
            item['additionalInsureAgeLimit'].append(i['value'])
        item['additionalInsureAgeLimit'].append('5年')
        item['additionalInsureAgeLimit'].append('10年')

        # 投保人性别
        for i in data[3]['dictionaryList']:
            item['vesterSex'].append(i['value'])

        # 被保险人性别
        for i in data[5]['dictionaryList']:
            item['sex'].append(i['value'])

        # 投保地区
        for i in data[6]['dictionaryList']:
            item['province'].append(i['byname'])

        # 基本保额
        for i in data[7]['dictionaryList']:
            item['leastamount'].append({
                            "value": i['value'],
                            "min": i['min'],
                            "max": i['max'],
                            "step": i['step'],
                        })

        # 保障期限
        for i in data[8]['dictionaryList']:
            item['insurantDateLimit'].append(i['value'])

        # 缴费年限
        for i in data[9]['dictionaryList']:
            item['insureAgeLimit'].append(i['value']+'年')

        # 缴费类型
        for i in data[10]['dictionaryList']:
            item['paymentType'].append(i['value'])

        # 高中大学教育年金保额
        for i in data[12]['dictionaryList']:
            item['seniorUniversityEdu'].append(i)

        # 重大疾病保险保额
        for i in data[12]['dictionaryList']:
            item['seriousIllness'].append(i)

        # 长期住院津贴保额
        for i in data[13]['dictionaryList']:
            item['hospitalAllowance'].append(i)

        # 长期意外伤害医疗保险保额
        for i in data[14]['dictionaryList']:
            item['accidentalInjury'].append(i)

        # 臻爱定期寿险保额
        for i in data[15]['dictionaryList']:
            item['regular'].append(i)

        # 高中大学教育年金保障期限
        for i in data[16]['dictionaryList']:
            item['additionalRiskPeriod'].append(i['value'])

        # 保障权益
        protect_interest_data = data_list['restrictRules'][0]['protectTrialItemList']
        for i in protect_interest_data:
            item['protect_interest'].append({'name': i['name'],
                                             'description': i['description'].
                                            replace('<br />', '').replace('\r', '').replace('\n', '')})

        # 建立和mongodb的连接
        client = MongoClient(host="121.43.189.184", port=27017)

        # 选择要操作的数据库和集合
        collection = client["insurance_django"]["insurance_data_zabb"]
        collection.update_one({"name": "珍爱宝贝教育年金保险计划"}, {"$set": item})

