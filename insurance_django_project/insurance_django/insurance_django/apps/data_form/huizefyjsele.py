from selenium import webdriver
import time
from pymongo import MongoClient
from insurance_django.settings import CHROME


# 福佑金生年金保险
def writePage(username):
    # 建立和mongodb的连接
    client = MongoClient(host="121.43.189.184", port=27017)
    # 选择要操作的数据库和集合
    collection = client["insurance_django"]["insurance_data_fyj"]

    # item = {
    #         'sex': '女',  # 性别
    #         'insurantDateLimit': '20年',  # 保障期限
    #         'paymentType': '年交',  # 缴费类型
    #         'insureAgeLimit': '5年',  # 缴费年限
    #         'premium': '10000',  # 保费
    #     }
    item = collection.find_one({"username": username})

    driver = webdriver.Chrome(executable_path=CHROME)
    url = 'https://www.huize.com/product/detail-101804.html?DProtectPlanId=104175'
    driver.maximize_window()
    driver.get(url)

    if item['sex'] == '女':
        driver.find_element_by_id('list-item-104175-sex').find_elements_by_xpath('dd/span')[1].click()
        time.sleep(1)
    if item['paymentType'] == '年交':
        driver.find_element_by_id('list-item-104175-paymentType').find_elements_by_xpath('dd/span')[1].click()
        time.sleep(1)
    if item['insurantDateLimit'] == '15年':
        driver.find_element_by_id('list-item-104175-insurantDateLimit').find_elements_by_xpath('dd/span')[1].click()
        time.sleep(1)
    if item['insurantDateLimit'] == '20年':
        driver.find_element_by_id('list-item-104175-insurantDateLimit').find_elements_by_xpath('dd/span')[2].click()
        time.sleep(1)
    if item['insureAgeLimit'] == '5年':
        driver.find_element_by_id('list-item-104175-insureAgeLimit').find_elements_by_xpath('dd/span')[1].click()
        time.sleep(1)
    driver.find_element_by_id('list-item-104175-premium').find_elements_by_xpath('dd/div/div/span')[0].click()
    time.sleep(1)
    driver.find_element_by_id('list-item-104175-premium').find_element_by_xpath('dd/div/div/div/input').send_keys(item['premium'])
    time.sleep(1)
    driver.find_element_by_id('list-item-104175-premium').find_element_by_xpath('dd/div/div/div/div/a[2]').click()
    time.sleep(1)

    # 保费入库
    insurance_money = driver.find_element_by_id('list-item-104175-').find_element_by_xpath('dd/span/span/i').text
    collection.update_one({"username": username}, {"$set": {"insurance_money": insurance_money}})
