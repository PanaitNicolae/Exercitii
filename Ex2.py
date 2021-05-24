from selenium import webdriver

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)


def decorator_function(original_function):
    def wrapper_function(n):
        original_function(n)
        driver.close()
    return wrapper_function


@decorator_function
def number_of_examples(test_number):
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
        print("Number of examples is ", examples_number, ", different than",test_number,".")

number_of_examples(5)



