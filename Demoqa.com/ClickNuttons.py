from Driver import *
import time
from selenium.webdriver.common.action_chains import ActionChains
class ClickButtons(Driver):
    
    def get_btn_name(self):
        generic_xpath = "//div[contains(@class,'col-12 mt-4 col-md-6')]"
        boxes_labels_xpath = generic_xpath + "//button"
        labels = self._driver().find_elements_by_xpath(boxes_labels_xpath)
        available_boxes = []
        for i in labels:
            available_boxes.append(i.text)
        return available_boxes
        
    def click_btn(self, form_dict):
        input_xpath = "//div[contains(@class, 'col-12 mt-4 col-md-6')]//button[text()='{}']"
        action = ActionChains(self._driver())
        available_boxes = self.get_btn_name()
        for i in list(form_dict.keys()):
            print(i)
            time.sleep(3)
            if i in available_boxes:
                input_box = self._driver().find_element_by_xpath(input_xpath.format(i))
                if form_dict[i] == "+1":
                    action.click(input_box).perform()
                elif form_dict[i] == "2":
                    action.double_click(input_box).perform()
                elif form_dict[i] == "-1":
                    action.context_click(input_box).perform()
                    
