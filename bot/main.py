import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import xlrd

text_ad = "Quotemykaam.com - One stop solution for all your daily service needs \n" \
          "Trusted vendors, Great  offers, Service guarantee"

image_li = ['/home/h_hack/Desktop/quotemykaam/4.jpg']
contact_name_list = ['Kamal']

##...............interfacing excel.................................................
wb = xlrd.open_workbook('/home/h_hack/Desktop/quotemykaam/data.xls')
for s in wb.sheets():
    for row in range(s.nrows):
        contact_name_list.append(str(s.cell(row, 0).value) + " " + str(s.cell(row, 1).value))


##................getting driver and web page......................................


def make_base():
    try:

        driver = webdriver.Firefox()
        driver.get("https://web.whatsapp.com/")
        time.sleep(30)
        return driver
    except:
        print "base problem"


##................. finding the contact and sending the text and image.............


def find_send(web_driver, contact_name, img):
    try:
        driver = web_driver
        contact = contact_name
        image_ad = img
        search_element = driver.find_element_by_class_name("input-search")
        search_element.clear()
        search_element.send_keys(contact)
        search_element.send_keys(Keys.ENTER)
        chat_body_ele = driver.find_elements_by_class_name("ellipsify")
        for c_b_e in chat_body_ele:
            check_cbe = contact in c_b_e.get_attribute("title")
            if check_cbe:
                c_b_e.click()
                input_elements = driver.find_elements_by_class_name("input")
                text_element = input_elements[1]
                text_element.send_keys(text_ad)
                text_element.send_keys(Keys.ENTER)
                text_element.clear()
                attach_element = driver.find_element_by_class_name("icon-clip")
                attach_element.click()
                image_element = driver.find_element_by_xpath(
                    "//input[contains(@data-reactid,'.0.$main.5.0.2.$conversation-header.0.1.$=10.0:2')]")
                driver.execute_script("arguments[0].style.display='block';", image_element)
                image_element.send_keys(image_ad)
                d_ctl = driver.find_element_by_class_name("drawer-media")
                d_ctl.click()
                send_ele = driver.find_element_by_class_name("btn-l")
                send_ele.click()
                time.sleep(2)
                break
    except:
        print "some problem"
        #return


def main():
    i = 0
    web_driver = make_base()
    #while True:
    while i < len(image_li):
        img = image_li[0]
        count = 0
        while count < len(contact_name_list):
            contact_name = contact_name_list[count]
            find_send(web_driver, contact_name, img)
            count += 1
        time.sleep(12000)
        i += 1
    web_driver.close()


if __name__ == '__main__':
    main()
