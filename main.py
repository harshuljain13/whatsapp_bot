__author__ = 'h_hack'

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


def main():
    contact_name = "Mainframe buddies"
    try:
        driver = webdriver.Firefox()
        driver.get("https://web.whatsapp.com/")
        time.sleep(30)
        search_element = driver.find_element_by_class_name("input-search")
        search_element.send_keys(contact_name)
        search_element.send_keys(Keys.ENTER)
        chat_body_ele = driver.find_elements_by_class_name("ellipsify")
        for c_b_e in chat_body_ele:
            check_cbe = contact_name in c_b_e.get_attribute("title")
            if check_cbe:
                c_b_e.click()
                input_elements = driver.find_elements_by_class_name("input")
                text_element = input_elements[1]
                text_element.send_keys(" Happy diwali Saikat")
                text_element.clear()
                check_cbe = False
                break
    except Exception:
        print "some problem"

if __name__ == '__main__':
    main()
