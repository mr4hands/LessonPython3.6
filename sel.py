from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(executable_path='C:\\Users\\egilron\\DevopsExperts\\LessonPython3.6\\resources\\chromedriver.exe')
driver.get("https://translate.google.com/")
print(driver.current_url)
print(driver.title)

text_area = driver.find_element_by_id("source")
text_area.send_keys("for real")

espaniol = driver.find_elements_by_id("sugg-item-es")
espaniol[1].click()

tl_more = driver.find_element_by_class_name("tlid-open-target-language-list")
tl_more.click()
lang_items = driver.find_elements_by_class_name("language_list_item_wrapper")

select_lang = driver.find_element_by_id("tl_list-search-box")
tl_more.click()
# select_lang.send_keys("Persian")
# select_lang.send_keys(Keys.ENTER)



for item in lang_items:
    tl_more.click()
    item.click()
