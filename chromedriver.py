from selenium import webdriver
import time
import os
import datetime

# Google search

chromedriver_path = 'D:/chromedrivers/74.0.3729.6/chromedriver.exe'
url = 'http://www.google.com/xhtml'
search_string = 'ChromeDriver'
file_name = str(datetime.datetime.now().strftime('%Y-%m-%d %H%M%S')) + " " + "Test.txt"
save_path = os.path.join("Webscrape", file_name)

driver = webdriver.Chrome(chromedriver_path)
driver.get(url)
time.sleep(1)

search_box = driver.find_element_by_name('q')
search_box.send_keys(search_string)
#search_box.submit() # Standard search

time.sleep(1) # 1 second wait for the results to pop up

lucky_button = driver.find_element_by_name('btnI')
lucky_button.click()

html_content = driver.page_source

time.sleep(2)
driver.quit()
