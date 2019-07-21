# -*- coding: utf-8 -*-

import time
import sys
from selenium import webdriver
import uuid

#load chrome driver as our webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='C:\\Users\\egilron\\DevopsExperts\\LessonPython3.6\\resources\\chromedriver.exe')

#get url from url.txt file
try:
    url = open("resources/url.txt",'r').read()
except IOError as e:
    print('there was a problem reading url.txt: ', e)

#open url
driver.get(url)

#find the sign in | sign up button and execute the js function click() (It is unclickable because of the nagishut strip
sign_in_button = driver.find_element_by_xpath('//*[@id="ember591"]/div/ul[1]/li[3]')
driver.execute_script("arguments[0].click()",sign_in_button)

#Click on sign-up
sign_up_button = driver.find_element_by_class_name('text-btn')
sign_up_button.click()

#find the web-elements to create account
all_fields = driver.find_element_by_class_name("oldschool").find_elements_by_class_name("ember-text-field")
for field in all_fields:
    if field.get_attribute("type") == "text":
        field.send_keys("erez")
    elif field.get_attribute("type") == "email":
        # create a random mail (sorry buy-me :) )
        field.send_keys(uuid.uuid4().hex + '@mailinator.com')
    elif field.get_attribute("type") == "password":
        field.send_keys("Aa12345678")


#find and click on agree to terms
all_checkboxes = driver.find_elements_by_class_name("ember-checkbox")
for checkbox in all_checkboxes:
    if not checkbox.is_selected():
        driver.execute_script("arguments[0].click()",checkbox)

#submit form
all_checkboxes[0].submit()

#sleep 1 second so the signup pop-up disappear
time.sleep(1)

'''
Function to select an element from drop down menu
id - the id of the drop down web element
index - the index of the item to choose from chosen drop down menu
'''
def select_from_dropdown_element(dropdown_element, index):
    dropdown_element.click()
    drop_down_items = driver.find_elements_by_class_name("active-result")
    try:
        drop_down_items[index].click()
    except IndexError:
        print('there is no web element with index: ',index)
        sys.exit(404)



#choose the item from drop down menus
select_from_dropdown_element(driver.find_element_by_id('ember664_chosen'),2)
select_from_dropdown_element(driver.find_element_by_id('ember679_chosen'),5)
select_from_dropdown_element(driver.find_element_by_id('ember689_chosen'),1)

#click on תמצאו לי מתנה
driver.find_element_by_id("ember724").click()

driver.implicitly_wait(5)

#chooose a business and enter 150 shekels to the gift card value
driver.find_element_by_id("ember1204").click()
amount_text_area = driver.find_element_by_id("ember1250")
amount_text_area.send_keys("150")

driver.find_element_by_class_name("moneyForm").find_element_by_class_name("btn").click()

#save the gift form webElement for reference
send_gift_form = driver.find_element_by_class_name("step-form-wrapper")

#get all radio button under למי לשלוח
forWho_radio_buttons = send_gift_form.find_element_by_class_name("forWho").find_elements_by_class_name("text")

#find למישהו אחר and click on it
for radio_button in forWho_radio_buttons:
    if radio_button.text == "למישהו אחר":
        radio_button.click()


#fill in the מישהו אחר details and all the rest
ui_card = driver.find_element_by_class_name("ui-grid")
ui_inputs = ui_card.find_elements_by_class_name("ui-input")
for ui_input in ui_inputs:
    if ui_input.find_element_by_class_name("label").text == "למי המתנה?":
        input_element = ui_input.find_element(By.CSS_SELECTOR, "input")
        input_element.clear()
        input_element.send_keys("daniel")
    elif ui_input.find_element_by_class_name("label").text == "ממי המתנה?":
        input_element = ui_input.find_element(By.CSS_SELECTOR, "input")
        input_element.clear()
        input_element.send_keys("erez :)")

#enter a reason
ui_card.find_element_by_class_name("ui-textarea").send_keys("for being A Okay")

#select occasion from drop down
select_from_dropdown_element(ui_card.find_element_by_class_name("ui-select"),4)

#upload an image by finding the upload image element in media-fields div
upload_image_element = driver.find_element_by_class_name("media-fields").find_element_by_class_name("ember-text-field")
if upload_image_element.get_attribute("accept") == "image/*":
    upload_image_element.send_keys("C:\\Users\\egilron\\DevopsExperts\\LessonPython3.6\\resources\\Untitled.png")

#click on the send-now radio-button
driver.find_element_by_class_name("send-now").click()

#get the webElement that holds all the send methods
send_methods_element = driver.find_element_by_class_name("send-methods")

#choose email (envelope icon), fill the form and click send
send_methods_element.find_element_by_class_name("icon-envelope").click()

send_methods_element.find_element_by_class_name("ember-text-field").send_keys(uuid.uuid4().hex + '@mailinator.com')
send_methods_element.find_element_by_class_name("btn-save").click()

#submit form
send_methods_element.submit()


