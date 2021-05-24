from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
action = ActionChains(driver)


def decorator_function(original_function):
    def wrapper_function():
        print(original_function())
        driver.close()
    return wrapper_function


@decorator_function
def last_release_function():
    driver.get("https://www.python.org/")

    download_button_path = "//li[@id = 'downloads']"
    all_releases_button_path = "//li[@id='downloads']//ul[@class='subnav menu']//a[contains(text(), 'All releases')]"
    table_first_line_path = "//div[@class='row download-list-widget']//ol[@class='list-row-container menu']//li[1]"
    release_version_path = table_first_line_path + "//span[@class='release-number']//a"
    release_date_path = table_first_line_path + "//span[@class='release-date']"

    download_button = driver.find_element_by_xpath(download_button_path)
    all_releases_button = driver.find_element_by_xpath(all_releases_button_path)

    action.move_to_element(download_button).perform()
    time.sleep(0.5)
    all_releases_button.click()

    release_version = driver.find_element_by_xpath(release_version_path).text
    release_date = driver.find_element_by_xpath(release_date_path).text
    return release_version + " " + release_date


last_release_function()
