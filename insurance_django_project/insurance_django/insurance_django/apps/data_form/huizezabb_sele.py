from selenium import webdriver
import time
from pymongo import MongoClient
from insurance_django.settings import CHROME


# 珍爱宝贝教育年金保险计划
def writepage_zabb(username):
    # 建立和mongodb的连接
    client = MongoClient(host="121.43.189.184", port=27017)
    # 选择要操作的数据库和集合
    collection = client["insurance_django"]["insurance_data_zabb"]

    # item = {
    #     'policyholderExemption',
    #     'vesterSex',
    #     'sex',
    #     'province',
    #     'leastamount',
    #     'seriousIllness',
    #     'hospitalAllowance',
    #     'accidentalInjury',
    #     'regular'
    # }
    item = collection.find_one({"username": username})

    driver = webdriver.Chrome(executable_path=CHROME)
    driver.maximize_window()
    driver.get("https://www.huize.com/product/detail-101832.html?DProtectPlanId=104245")
    time.sleep(3)
    if item['policyholderExemption'] == "含":
        driver.find_element_by_xpath('//div[@id="trialAreasGenes"]/div/dl[2]/dd/span[2]').click()
        time.sleep(1)

    if item['vesterSex'] == "女":
        driver.find_element_by_xpath('//div[@id="trialAreasGenes"]/div/dl[4]/dd/span[2]').click()
        time.sleep(1)

    if item['sex'] == "女":
        driver.find_element_by_xpath('//div[@id="trialAreasGenes"]/div/dl[6]/dd/span[2]').click()
        time.sleep(1)

    # 投保地区
    driver.find_element_by_xpath('//div[@id="trialAreasGenes"]/div/dl[7]/dd/div/div[1]').click()
    time.sleep(1)

    city_list = ["北京市","福建省","广东省","河南省","湖北省","湖南省","江苏省","江西省","辽宁省","山东省","陕西省","上海市","四川省","天津市","浙江省","重庆市"]

    driver.find_element_by_xpath('//div[@id="trialAreasGenes"]/div/dl[7]/dd/div/div[2]/ul/li['+ str(city_list.index(item['province'])+1) +']').click()
    time.sleep(1)

    # 基本保额
    if int(item['leastamount'].split('万')[0]) < 6:
        driver.find_element_by_xpath('//div[@id="trialAreasGenes"]/div/dl[8]/dd/span['+item['leastamount'].split('万')[0]+']').click()
        time.sleep(1)
    else:
        driver.find_element_by_xpath('//div[@id="trialAreasGenes"]/div/dl[8]/dd/div/div[1]/span').click()
        time.sleep(1)
        driver.find_element_by_xpath('//div[@id="trialAreasGenes"]/div/dl[8]/dd/div//ul/li[' + str(int(item['leastamount'].split('万')[0])-5) +']').click()
        time.sleep(1)

    # 缴费年限
    if item['insureAgeLimit'] == '10年':
        driver.find_element_by_xpath('//div[@id="trialAreasGenes"]/div/dl[10]/dd/span[2]').click()
        time.sleep(1)

        # 高中大学教育年金保额
        if item['seniorUniversityEdu'] != "不投保":
            if int(item['seniorUniversityEdu'][:-2]) < 6:
                driver.find_element_by_xpath('//div[@id="trialAreasGenes"]/div/dl[12]/dd/span['+ str(int(item['seniorUniversityEdu'][:-2])+1) +']').click()
                time.sleep(1)
            else:
                driver.find_element_by_xpath('//div[@id="trialAreasGenes"]/div/dl[12]/dd/div/div[1]/span').click()
                time.sleep(1)
                driver.find_element_by_xpath('//div[@id="trialAreasGenes"]/div/dl[12]/dd/div//ul/li[' + str(int(item['seniorUniversityEdu'][:-2])-4) +']').click()
                time.sleep(1)

    # 重大疾病保险保额
    if item['seriousIllness'] != "不投保":
        if int(item['seriousIllness'][:-2]) < 5:
            driver.find_element_by_xpath('//div[@id="trialAreasGenes"]/div/dl[13]/dd/span['+str(int(item['seriousIllness'][:-2])+1)+']').click()
            time.sleep(1)
        else:
            driver.find_element_by_xpath('//div[@id="trialAreasGenes"]/div/dl[13]/dd/div/div[1]/span').click()
            time.sleep(1)
            driver.find_element_by_xpath('//div[@id="trialAreasGenes"]/div/dl[13]/dd/div//ul/li[' + str(int(item['seriousIllness'][:-2])-4) +']').click()
            time.sleep(1)

    # 长期住院津贴保额
    if item['hospitalAllowance'] != "不投保":
        num = int(item['hospitalAllowance'].split('元')[0])/50
        driver.find_element_by_xpath('//div[@id="trialAreasGenes"]/div/dl[14]/dd/span['+ str(int(num)+1) +']').click()
        time.sleep(1)

    # 长期意外伤害医疗保险保额
    if item['accidentalInjury'] != "不投保":
        num = int(item['accidentalInjury'].split('元')[0])/5000
        driver.find_element_by_xpath('//div[@id="trialAreasGenes"]/div/dl[15]/dd/span['+ str(int(num)+1) +']').click()
        time.sleep(1)

    # # 臻爱定期寿险保额
    if item['regular'] != "不投保":
        num = int(item['regular'].split('万')[0])/5
        if num < 5:
            driver.find_element_by_xpath("//div[@id='trialAreasGenes']/div/dl[16]/dd/span["+ str(int(num)+1)+ "]").click()
            time.sleep(1)
        else:
            driver.find_element_by_xpath('//div[@id="trialAreasGenes"]/div/dl[16]/dd/div//div[1]/span').click()
            time.sleep(1)
            driver.find_element_by_xpath('//div[@id="trialAreasGenes"]/div/dl[16]/dd/div//div[2]/ul/li['+ str(int(num)-4) +']').click()
            time.sleep(1)

    # 保费入库
    insurance_money = driver.find_element_by_id('list-item-104245-').find_element_by_xpath('dd/span/span/i').text
    collection.update_one({"username": username}, {"$set": {"insurance_money": insurance_money}})
