from selenium import webdriver
from selenium.webdriver.common.by import By

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://www.python.org/")
search_bar_path = "//input[@id ='id-search-field']"
go_button_path = "//button[@id='submit']"
first_result_link_path = "//ul[@class='list-recent-events menu']/li[1]/h3/a[contains(text(), 'Decorators for Functions')]"
examples_link_path = "//div[@class='contents topic']/ul/li/a[text()='Examples']"
examples_path = "//div[@id='examples']//li"
search_bar = driver.find_element(By.XPATH, search_bar_path )
go_button = driver.find_element(By.XPATH, go_button_path)
search_bar.send_keys("decorator")
go_button.click()
driver.find_element(By.XPATH, first_result_link_path).click()
driver.find_element(By.XPATH, examples_link_path).click()
examples_number = len(driver.find_elements(By.XPATH, examples_path))

if examples_number == 5:
    print("Number of examples is 5.")
else:
    print("Number of examples is ", examples_number, ", different than 5.")
