from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
import datetime

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

    download_button_xpath = "//li[@id = 'downloads']"
    all_releases_button_xpath = "//li[@id='downloads']//ul[@class='subnav menu']//a[contains(text(), 'All releases')]"

    download_button = driver.find_element_by_xpath(download_button_xpath)
    all_releases_button = driver.find_element_by_xpath(all_releases_button_xpath)
    action.move_to_element(download_button).perform()
    time.sleep(1)
    all_releases_button.click()


def get_last_version():
    table_first_line_xpath = "//div[@class='row active-release-list-widget']//ol[@class='list-row-container menu']//li[1]"
    last_version_xpath = table_first_line_xpath + "//span[@class='release-version']"
    last_version = driver.find_element_by_xpath(last_version_xpath).text
    return last_version


def get_all_released_versions():
    table_xpath = "//div[@class='row download-list-widget']//ol[@class='list-row-container menu']//li//span[@class='release-number']"
    all_releases = [i.text.split()[1] for i in driver.find_elements_by_xpath(table_xpath)]
    return all_releases


def check_is_released(all_releases, last_version):
    for i in all_releases:
        if last_version in i:
            print(f"There is at least 1 release for version {last_version}!")
            return 1
    print(f"There is no release for version {last_version}")
    return 0


def get_last_version_date():
    version_date_xpath = "//div[@class='row active-release-list-widget']//ol[@class='list-row-container menu']//li[1]//span[@class='release-start']"
    format_str = "%Y-%m-%d"
    version_date = datetime.datetime.strptime(driver.find_element_by_xpath(version_date_xpath).text, format_str)
    return version_date


def get_last_release_date():
    release_date_xpath = "//div[@class='row download-list-widget']//ol[@class='list-row-container menu']//li[1]//span[@class='release-date']"
    format_str = "%B %d, %Y"
    release_date = datetime.datetime.strptime(driver.find_element_by_xpath(release_date_xpath).text, format_str)
    return release_date


def verify_release_version_date(release_date, version_date):
    if release_date > version_date:
        print("The last release took place after the version was first released!")
    else:
        raise Exception("Release before version first release!!!!")



go_to_all_releases()
check_is_released(get_all_released_versions(), get_last_version())
verify_release_version_date(get_last_release_date(),get_last_version_date())
driver.close()

