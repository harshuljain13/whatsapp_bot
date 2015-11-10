__author__ = 'h_hack'

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def main():
    try:
        driver = webdriver.Firefox()
        driver.get("https://web.whatsapp.com/")
        time.sleep(60)
        search_element = driver.find_element_by_class_name("input-search")
        search_element.send_keys("Mainframe buddies")
        search_element.send_keys(Keys.ENTER)
        select_element = driver.find_elements_by_class_name("chatlist")
        print select_element
        select_element[0].click()
        input_elements = driver.find_elements_by_class_name("input")
        text_element = input_elements[1]
        text_element.send_keys(" Happy diwali Saikat")
        text_element.send_keys(Keys.ENTER)
        #time.sleep(60)
        #driver.close()

    except:
        print "no element found"





if __name__=='__main__':
    main()
