from selenium import webdriver

########
#  1   #
########

chrome_driver = webdriver.Chrome(executable_path='C:\\Users\\egilron\\DevopsExperts\\LessonPython3.6\\resources\\chromedriver.exe')
firefox_driver = webdriver.Firefox(executable_path='C:\\Users\\egilron\\DevopsExperts\\LessonPython3.6\\resources\\geckodriver.exe')

chrome_driver.get('https://www.walla.co.il')
firefox_driver.get('http://www.ynet.co.il')

########
#  2   #
########
chrome_title = chrome_driver.title
chrome_driver.refresh()
chrome_name = chrome_driver.name
print("chrome title:", chrome_title, "chrome site name:", chrome_name)

#######
#  3  #
#######
# It seems that the elements have the same locators

#######
#  4  #
#######
chrome_driver.get("https://translate.google.com/")
text_area = chrome_driver.find_element_by_id("source")
text_area.send_keys("עברית")

######
# 5  #
######
chrome_driver.get("https://www.youtube.com")
text_area = chrome_driver.find_element_by_id("search")
text_area.send_keys("flairs - better than prince")
search_button = chrome_driver.find_element_by_id("search-icon-legacy")
search_button.click()

######
#  6 #
######

