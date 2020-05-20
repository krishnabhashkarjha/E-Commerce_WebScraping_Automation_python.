import threading
from selenium import webdriver
from Utilites import AppConstants


def thread1(driver):
    driver.get('http://dc4ui.p01.pro:7777/dc4custmanager/faces/eh/browsetickets.jsp')

def thread2(driver):
    driver.get('https://spscommerce.my.salesforce.com/a020g00000ULxLi')

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--start-maximized")
v_driver1 = webdriver.Chrome(AppConstants.BROWSER_DRIVER, chrome_options= chrome_options)
v_driver2 = webdriver.Chrome(AppConstants.BROWSER_DRIVER, chrome_options= chrome_options)
t1 = threading.Thread(target=thread1, args = (v_driver1,))
t2 = threading.Thread(target=thread2,  args = (v_driver2,))

t1.start()
t2.start()

t1.join()
t2.join()

