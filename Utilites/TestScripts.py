
import re
status_description_pre = 'Supplier ID: 12:6095640413A; Retailer ID: 14:006929681100\nasdbdajk a '
if 'ID' in status_description_pre:
    client_uid = status_description_pre.split('ID')[1]
    client_uid = client_uid.split('Retailer')[0]
    client_uid = re.sub('[^A-Za-z0-9]+', '', client_uid)
    retailer_uid = status_description_pre.split('ID')[2]
    if '\n' in retailer_uid:
        retailer_uid = retailer_uid.split('\n')[0]
    retailer_uid = re.sub('[^A-Za-z0-9]+', '', retailer_uid)
    print("Retailer UID: " + str(retailer_uid))
    print(client_uid)

# from selenium import webdriver
# from Utilites import AppConstants
# import time
# driver = webdriver.Chrome(AppConstants.BROWSER_DRIVER)
# driver.implicitly_wait(200)
# driver.get("https://www.toggl.com/app/timer")
# email = driver.find_element_by_id('login-email')
# email.send_keys('kpandya@spscommerce.com')
# password = driver.find_element_by_id('login-password')
# password.send_keys('Pashiben@007')
# driver.find_element_by_xpath('//*[@id="login-button"]').click()
# time.sleep(10)
# driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div/div/div[2]/div[1]/div[1]/a').click()
# description = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div[4]/div/div/div/div[1]/div/div[2]/div[2]/div[1]/div/form/input')
# #description.click()
# driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div[4]/div/div/div/div[1]/div/div[2]/div[1]').click()
# print('Hello')
#
# description.send_keys('FICS-167318 Prod Issue 2/19/2019')
# driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div[4]/div/div/div/div[1]/div/div[3]/span/span').click()
# driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div[4]/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div[2]/div[1]/div/div/div/div[3]/a').click()
# driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div[4]/div/div/div/div[1]/div/div[6]/div[3]').click()