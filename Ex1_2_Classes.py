from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains

class Driver:

    PATH = "C:\Program Files (x86)\chromedriver.exe"

    def get_driver(self):
        return webdriver.Chrome(Driver.PATH)


class Ex12(Driver):

    def last_release_function(self):
        driver = Ex12.get_driver(self)
        action = ActionChains(driver)
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

    def number_of_examples(self, test_number):
        driver = Ex12.get_driver(self)
        driver.get("https://www.python.org/")
        search_bar_path = "//input[@id ='id-search-field']"
        go_button_path = "//button[@id='submit']"
        first_result_link_path = "//ul[@class='list-recent-events menu']/li[1]//a"
        examples_link_path = "//div[@class='contents topic']/ul/li/a[text()='Examples']"
        examples_path = "//div[@id='examples']//li"

        search_bar = driver.find_element_by_xpath(search_bar_path)
        go_button = driver.find_element_by_xpath(go_button_path)

        search_bar.send_keys("decorator")
        go_button.click()
        driver.find_element_by_xpath(first_result_link_path).click()
        driver.find_element_by_xpath(examples_link_path).click()

        examples_number = len(driver.find_elements_by_xpath(examples_path))

        if examples_number == test_number:
            print("Number of examples is correct")
        else:
            print("Number of examples is ", examples_number, ", different than", test_number, ".")



ex1 = Ex12()
print(ex1.last_release_function())
ex1.number_of_examples(5)

time.sleep(3)
