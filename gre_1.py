#coding: utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import send_email
import time
import sys
import os
#UnicodeEncodeError: 'ascii' codec can't encode characters in position 0-10: ordinal not in range(128)
reload(sys)
sys.setdefaultencoding("utf-8")

driver = webdriver.Chrome('/home/bixiang/Desktop/chromedriver')
driver.get("https://gre.etest.net.cn/login.do")
time.sleep(1)
elem = driver.find_element_by_name("neeaId")
elem.send_keys(u'******')
elem = driver.find_element_by_name("password")
elem.send_keys(u'******')
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
m.find_element_by_xpath("//option[@value='2017-08-25']").click()              
time.sleep(3)
result5 = driver.find_element_by_xpath("//*[@id='testDate_Next']").click()
ActionChains(driver).click(result5).perform()
time.sleep(5)
# print driver.page_source
# exit()

school = ['''//*[@id='order_"STN80068B"']''','''//*[@id='order_"STN80080A"']''','''//*[@id='order_"STN80098A"']''','''//*[@id='order_"STN80055A"']''','''//*[@id='order_"STN80111A"']''',
		'''//*[@id='order_"STN80111B"']''','''//*[@id='order_"STN80118A"']''','''//*[@id='order_"STN80034E"']''','''//*[@id='order_"STN80034F"']''','''//*[@id='order_"STN80058C"']''']
# school = ['''//*[@id='order_"STN80033F"']''','''//*[@id='order_"STN80034F"']''','''//*[@id='order_"STN80080A"']''']
try:
	while True:
		for s in school:
			result6 = driver.find_element_by_xpath(s).click()
			ActionChains(driver).click(result6).perform()
			time.sleep(1)   
		result7 = driver.find_element_by_xpath('//*[@id="sites_BackDate"]').click()
		ActionChains(driver).click(result7).perform()
		time.sleep(1)
		result8 = driver.find_element_by_xpath('//*[@id="testDate_Next"]').click()
		ActionChains(driver).click(result8).perform() 
except:
	print '!!!!!'
	send_email.sendEmail("gre", "8.25有考位啦！")
