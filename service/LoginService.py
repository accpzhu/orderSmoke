# -*- coding=utf-8 -*-
from model import User
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time
import ConfigParser
import  os
class LoginService(object):
    def login(self,user,url,driverPath):
        browser = webdriver.Chrome(driverPath)
        browser.get(url)
        usernameElem = browser.find_element_by_id("username")
        passwordelem = browser.find_element_by_id("password")
        usernameElem.send_keys(user.username)
        passwordelem.send_keys(user.password)
        browser.find_element_by_id("btn-login").click()

        time.sleep(5)
        try:
            browser.find_element_by_link_text("修改订单").click()
        except NoSuchElementException:
            print('No Element')
        # finally:
        #    browser.close()

        # browser.find_element_by_link_text("修改订单").click()





