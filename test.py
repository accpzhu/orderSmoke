from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome('F://PycharmProjects//orderSmoke//resource//chromedriver.exe') # Get local session of Chrome
browser.get("http://www.xinshangmeng.com/xsm2/")
print (browser.title)

usernameElem=browser.find_element_by_id("username")

passwordelem=browser.find_element_by_id("password")

usernameElem.send_keys("120101104700");
passwordelem.send_keys("liusanli1")

browser.find_element_by_id("btn-login").click()


#browser.find_element_by_link_text("修改订单").click()

time.sleep(5)


try:
    browser.find_element_by_link_text("修改订单").click()
except NoSuchElementException:
    print('No Element')
#finally:
#    browser.close()



'''


try:
    browser.find_element_by_id('hello')
except NoSuchElementException:
    print('No Element')
finally:
    browser.close()

try:
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "myDynamicElement")))
finally:
    driver.quit()
'''
