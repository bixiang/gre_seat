#coding: utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import send_email
from lxml import etree
# import requests
import time
import sys
import os
#UnicodeEncodeError: 'ascii' codec can't encode characters in position 0-10: ordinal not in range(128)
reload(sys)
sys.setdefaultencoding("utf-8")

test_date = '2017-08-25'

driver = webdriver.Chrome('/home/bixiang/Desktop/chromedriver')
driver.get("https://gre.etest.net.cn/login.do")
time.sleep(1)
elem = driver.find_element_by_name("neeaId")
elem.send_keys(u'*******')
elem = driver.find_element_by_name("password")
elem.send_keys(u'*******')
time.sleep(8)
login = driver.find_element_by_xpath('//*[@id="loginForm"]/div[5]/input')    
ActionChains(driver).click(login).perform()
time.sleep(3)
regis_test = driver.find_element_by_xpath('//*[@id="westContainer"]/ul/li[13]/a')    
ActionChains(driver).click(regis_test).perform()
time.sleep(3)
result0 = driver.find_element_by_xpath('//*[@id="huabei"]')    
ActionChains(driver).click(result0).perform()   
time.sleep(3)  
result1 = driver.find_element_by_xpath('//*[@id="huabeiProvinces"]')  
ActionChains(driver).click(result1).perform()   
time.sleep(3)
result2 = driver.find_element_by_xpath('//*[@id="BEIJING"]')    
ActionChains(driver).click(result2).perform()
time.sleep(3)
result3 = driver.find_element_by_xpath('//*[@id="BEIJING_BEIJING"]')
ActionChains(driver).click(result3).perform()
time.sleep(3)
result4 = driver.find_element_by_xpath('//*[@id="cities_Next"]')    
ActionChains(driver).click(result4).perform()
#先定位到下拉框
time.sleep(3)
m = driver.find_element_by_id("yearMonth")
#再点击下拉框下的选项
m.find_element_by_xpath("//option[@value='%s']"%test_date).click()              
time.sleep(3)
result5 = driver.find_element_by_xpath("//*[@id='testDate_Next']").click()
ActionChains(driver).click(result5).perform()
time.sleep(5)

while True:
	page = driver.page_source
	selector = etree.HTML(page)
	pList = selector.xpath('//*[@id="sitesTable0"]/tbody/tr')
	for item in pList:
		# print item.xpath('string(.)')[0]
		if item.xpath('td[4]/text()') and item.xpath('td[4]/text()')[0] != '暂满':
			school_code = item.xpath('td[1]/a/text()')[0]
			school_name = item.xpath('td[2]/text()')[0]
			# print school_code,school_name
			result6 = driver.find_element_by_xpath('''//*[@id='order_"%s"']'''%school_code).click()
			ActionChains(driver).click(result6).perform()
			send_email.sendEmail(school_name, "%s有考位啦！"%test_date)
			sys.exit(0) 

		else:
			continue
	result7 = driver.find_element_by_xpath('//*[@id="sites_BackDate"]').click()
	ActionChains(driver).click(result7).perform()
	time.sleep(90)
	result8 = driver.find_element_by_xpath('//*[@id="testDate_Next"]').click()
	ActionChains(driver).click(result8).perform()





# url = '''https://gre.etest.net.cn/testSites.do?p=testSites&m=ajax&adminDate=2017-08-25&neeaID=71418860&cities=BEIJING_BEIJING%3B&citiesNames=%25E5%258C%2597%25E4%25BA%25AC%3B&whichFirst=AS&isFilter=1&opt=new'''
# session = requests.Session()
# s = session.get(url)
# print s 
  
# school_list = a[0]["dates"][0]["sites"]
# for s in school_list:
# 	if s["realSeats"] != 0:
# 		print s["siteCode"]
