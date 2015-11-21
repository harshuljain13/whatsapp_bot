import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def main():
    contact_name = "Kamal"
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
                for i in range(1, 2):
                    text_element.send_keys("Live with this punishment now, It can run anytime :D")
                    text_element.send_keys(Keys.ENTER)
                    text_element.clear()
                attach_element = driver.find_element_by_class_name("icon-clip")
                attach_element.click()
                image_element = driver.find_element_by_xpath(
                    "//input[contains(@data-reactid,'.0.$main.5.0.2.$conversation-header.0.1.$=10.0:2')]")
                print image_element.get_attribute("type")
                string1 = "/home/h_hack/Desktop/1.jpg"
                driver.execute_script("arguments[0].style.display='block';", image_element)
                image_element.send_keys(string1)
                d_ctl = driver.find_element_by_class_name("drawer-media")
                d_ctl.click()
                send_ele = driver.find_element_by_class_name("btn-l")
                send_ele.click()
                break
    except:
        print "some problem"


if __name__ == '__main__':
    main()
