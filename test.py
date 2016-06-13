# encoding=utf-8
from selenium import webdriver

driver = webdriver.PhantomJS()
driver.get('https://mm.taobao.com/self/model_info.htm?user_id=687471686&is_coment=false')
print(driver.page_source)
