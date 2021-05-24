from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://www.python.org/")
search_bar_path = "//input[@id ='id-search-field']"
go_button_path = "//button[@id='submit']"
first_result_link_path = "//ul[@class='list-recent-events menu']/li[1]/h3/a[contains(text(), 'Decorators for Functions')]"
examples_link_path = "//div[@class='contents topic']/ul/li/a[text()='Examples']"

search_bar = driver.find_element(By.XPATH, search_bar_path )
go_button = driver.find_element(By.XPATH, go_button_path)
search_bar.send_keys("decorator")
go_button.click()
driver.find_element(By.XPATH, first_result_link_path).click()
driver.find_element(By.XPATH, examples_link_path).click()

# search = driver.find_element(By.XPATH, "//ul[@class='list-recent-events menu']/li[1]/h3/a").click()
# # driver.get(search)
# search = driver.find_element(By.XPATH, "//div[@class='contents topic']/ul/li/a[text()='Examples']").get_attribute("href")
# driver.get(search)
# # driver.close()


