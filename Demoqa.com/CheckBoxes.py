from Driver import *
import time
class CheckBoxes(Driver):   

    def click_extend_button(self):
        extend_btn_xpath = "//button[contains(@title, 'Expand all')]"
        extend_btn = self._driver().find_element_by_xpath(extend_btn_xpath)
        extend_btn.click()
    
    def get_avilable_boxes(self):
        generic_xpath = "//div[contains(@class, 'check-box-tree')]"
        labels_xpath = generic_xpath + "//label"
        elements = self._driver().find_elements_by_xpath(labels_xpath)
        available_labels = []
        for i in range(len(elements)):
           available_labels.append(elements[i].text)
        return available_labels
    
    def check_boxes(self, form_dict):    
        input_xpath = "//div[contains(@class, 'check-box-tree')]//span[text()='{}']"
        available_labels = self.get_avilable_boxes()
        for i in form_dict.keys():
            time.sleep(3)
            if i in available_labels:
                input_box = self._driver().find_element_by_xpath(input_xpath.format(i))
                if form_dict[i] == "Check" and self.is_selected(i) == 0:
                    input_box.click()
                elif form_dict[i] == "Unchecked" and self.is_selected(i):
                    input_box.click()

        
    def is_selected(self, label_name):
        element_path = "//label[span[text()='{}']]//input"
        element = self._driver().find_element_by_xpath(element_path.format(label_name))
        if element.is_selected():
            return 1
        else:
             return 0        
        
        
