from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains



PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
action = ActionChains(driver)

driver.get("https://www.python.org/")

download_button = driver.find_element(By.XPATH, "//li[@id = 'downloads']//a[text() = 'Downloads']")
all_releases_button = driver.find_element(By.XPATH, "//li[@id='downloads']//ul[@class='subnav menu']//a[contains(text(), 'All releases')]")

table_first_line_path = "//div[@class='row download-list-widget']//ol[@class='list-row-container menu']//li[1]"
release_version_path = table_first_line_path + "//span[@class='release-number']//a"
release_date_path = table_first_line_path + "//span[@class='release-date']"

action.move_to_element(download_button).perform()
all_releases_button.click()

release_version = driver.find_element(By.XPATH, release_version_path).text
release_date = driver.find_element(By.XPATH, release_date_path).text
print("Last Python version is: ", release_version, "and was released on: ", release_date)

# print("!!Python last relase info!!")
# print("Version: ", driver.find_element(By.XPATH,"//div[@class='row active-release-list-widget']//ol[@class='list-row-container menu']/li[1]/span[1]").text)
# print("Maintenance status: ", driver.find_element(By.XPATH, "//div[@class='row active-release-list-widget']//ol[@class='list-row-container menu']/li[1]/span[2]").text)
# print("First released: ", driver.find_element(By.XPATH, "//div[@class='row active-release-list-widget']//ol[@class='list-row-container menu']/li[1]/span[3]").text)
# print("End of support: ", driver.find_element(By.XPATH, "//div[@class='row active-release-list-widget']//ol[@class='list-row-container menu']/li[1]/span[4]").text)
# print("Release schedule: ", driver.find_element(By.XPATH, "//div[@class='row active-release-list-widget']//ol[@class='list-row-container menu']/li[1]/span[5]").text)
time.sleep(2)
driver.close()
