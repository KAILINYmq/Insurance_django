from selenium import webdriver
import time
from pymongo import MongoClient
from insurance_django.settings import CHROME


# 太平财富智赢年金保险+荣耀金账户终身寿险
def select_click(username):
    # 建立和mongodb的连接
    client = MongoClient(host="121.43.189.184", port=27017)
    # 选择要操作的数据库和集合
    collection = client["insurance_django"]["insurance_data_tpy"]

    # item = {
    #     'sex': '',
    #     'insureAgeLimit': '',
    #     'premium': '',
    #     'isInsure': ''
    # }
    item = collection.find_one({"username": username})

    driver = webdriver.Chrome(executable_path=CHROME)
    driver.maximize_window()
    driver.get("https://www.huize.com/apps/cps/index/product/detail?prodId=101868&planId=104316")
    driver.get("https://www.huize.com/apps/cps/index/product/detail?prodId=101868&planId=104316")

    # 填写时间
    # d = driver.find_element_by_id('trial-panel').find_element_by_xpath('div/dl[2]/dd/input')
    # driver.execute_script('arguments[0].removeAttribute(\"readonly\")', d)
    # d.clear()
    # d.send_keys(item['time'])

    if item['sex'] == "男":
        driver.find_element_by_xpath('//a[@trial-item-val="男"]').click()
        time.sleep(1)

    if item['insureAgeLimit'] == "3":
        driver.find_element_by_xpath('//a[@trial-item-val="3年"]').click()
        time.sleep(1)

    driver.find_element_by_xpath('//div[@class="input-select"]').click()
    time.sleep(1)
    driver.find_element_by_xpath('//div[@class="others-content"]/input').send_keys(int(item['premium']))
    time.sleep(1)
    driver.find_element_by_xpath('//div[@class="mt15"]/a[2]').click()
    time.sleep(1)
    if item['isInsure'] == "不含" and int(item['premium']) > 9000:
        driver.find_element_by_xpath('//a[@trial-item-val="不含"]').click()
        time.sleep(1)

    # 保费入库
    insurance_money = driver.find_element_by_class_name('product-price').find_element_by_xpath('span/i').text
    collection.update_one({"username": username}, {"$set": {"insurance_money": insurance_money}})
