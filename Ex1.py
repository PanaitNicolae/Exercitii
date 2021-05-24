from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains



PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
action = ActionChains(driver)

driver.get("https://www.python.org/")

download_button_path = "//li[@id = 'downloads']//a[text() = 'Downloads']"
all_releases_button_path = "//li[@id='downloads']//ul[@class='subnav menu']//a[contains(text(), 'All releases')]"
table_first_line_path = "//div[@class='row download-list-widget']//ol[@class='list-row-container menu']//li[1]"
release_version_path = table_first_line_path + "//span[@class='release-number']//a"
release_date_path = table_first_line_path + "//span[@class='release-date']"

download_button = driver.find_element(By.XPATH, download_button_path)
all_releases_button = driver.find_element(By.XPATH, all_releases_button_path)

action.move_to_element(download_button).perform()
all_releases_button.click()

release_version = driver.find_element(By.XPATH, release_version_path).text
release_date = driver.find_element(By.XPATH, release_date_path).text
print("Last Python version is: ", release_version, "and was released on: ", release_date)

time.sleep(2)
driver.close()
