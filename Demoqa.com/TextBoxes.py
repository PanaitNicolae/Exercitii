from selenium import webdriver
import time

thisdict = {
  "Full Name": "First Test",
  "Email": "abcd@abc.com",
  "Current Address": "Prahova",
  "Permanent Address": "Prahova"
}

driver = webdriver.Chrome()


def navigate_to(url = "https://demoqa.com/text-box"):
    driver.get(url)
      
def click_submit():
    submit_btn_xpath = "//button[@id='submit']"
    submit_btn = driver.find_element_by_xpath(submit_btn_xpath)
    submit_btn.click()

def complete_textboxes(form_dict = thisdict):    
    generic_xpath = "//div[contains(@id, 'wrapper')]"
    labels_xpath = generic_xpath + "//label"
    input_xpath = "//div[contains(@id, 'wrapper') and .//label[text()='{}']]//input | //div[contains(@id, 'wrapper') and .//label[text()='{}']]//textarea" 
    elements = driver.find_elements_by_xpath(labels_xpath)
    available_labels = []
    for i in range(len(elements)):
       available_labels.append(elements[i].text)
    print(available_labels) 
    
    for i in form_dict.keys():
        if i in available_labels:
            input_text = driver.find_element_by_xpath(input_xpath.format(i, i))
            input_text.send_keys(form_dict[i])
                
     
navigate_to()
complete_textboxes(thisdict) 
click_submit()    
