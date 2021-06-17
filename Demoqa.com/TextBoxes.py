import time
from Driver import *

class TextBoxes(Driver):   

    def click_submit(self):
        submit_btn_xpath = "//button[@id='submit']"
        submit_btn = self._driver().find_element_by_xpath(submit_btn_xpath)
        submit_btn.click()
        
        

    def find_labels(self):
        generic_xpath = "//div[contains(@id, 'wrapper')]"
        labels_xpath = generic_xpath + "//label"
        elements = self._driver().find_elements_by_xpath(labels_xpath)
        available_labels = []
        for i in range(len(elements)):
           available_labels.append(elements[i].text)

        return available_labels

    def complete_textboxes(self, form_dict):    
        input_xpath = "//div[contains(@id, 'wrapper') and .//label[text()='{}']]//input | \
                      //div[contains(@id, 'wrapper') and .//label[text()='{}']]//textarea" 
        available_labels = self.find_labels()
        for i in list(form_dict.keys()):
            if i in available_labels:
                input_text = self._driver().find_element_by_xpath(input_xpath.format(i, i))
                input_text.send_keys(form_dict[i])
            

    def get_results(self, form_dict):
        results_xpath = "//div[@id='output']//p"
        results = self.driver.find_elements_by_xpath(results_xpath)
        keys = form_dict.keys()
        values = []
        for i in results:
            result = i.text
            values.append(result.split(":")[1])
        return dict(zip(keys, values))

    def check_results(self, form_dict):
        results = self.get_results(form_dict)
        if not results == form_dict:
            raise Exception("Wrong results!")
        print("Checked!")
