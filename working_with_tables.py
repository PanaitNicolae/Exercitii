from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
action = ActionChains(driver)


def close_driver(original_function):
    def wrapper_function():
        print(original_function())
        driver.close()
    return wrapper_function


def go_to_all_releases():
    driver.get("https://www.python.org/")

    download_button_path = "//li[@id = 'downloads']"
    all_releases_button_path = "//li[@id='downloads']//ul[@class='subnav menu']//a[contains(text(), 'All releases')]"

    download_button = driver.find_element_by_xpath(download_button_path)
    all_releases_button = driver.find_element_by_xpath(all_releases_button_path)
    action.move_to_element(download_button).perform()
    time.sleep(0.75)
    all_releases_button.click()


@close_driver
def get_last_version():
    go_to_all_releases()
    table_first_line_path = "//div[@class='row active-release-list-widget']//ol[@class='list-row-container menu']//li[1]"
    last_version_path = table_first_line_path + "//span[@class='release-version']"
    last_version = driver.find_element_by_xpath(last_version_path).text
    return last_version


@close_driver
def get_all_released_versions():
    go_to_all_releases()
    table_path = "//div[@class='row download-list-widget']//ol[@class='list-row-container menu']"
    all_releases = driver.find_element_by_xpath(table_path).text
    return all_releases


def check_is_released(all_releases, last_version):
    if last_version in all_releases:
        print("YES")


# get_last_version()
get_all_released_versions()
# check_is_released(get_all_released_versions(), get_last_version)