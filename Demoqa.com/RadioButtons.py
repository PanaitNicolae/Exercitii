from Driver import *
import time

class RadioButtons(Driver):
    
    def get_available_radios(self):
        generic_xpath = "//div[@class = 'col-12 mt-4 col-md-6']"
        boxes_labels_xpath = generic_xpath + "//label"
        labels = self._driver().find_elements_by_xpath(boxes_labels_xpath)
        available_boxes = []
        for i in labels:
            available_boxes.append(i.text)
        print(available_boxes)
        return available_boxes
        
    def check_radio(self, form_dict):
        input_xpath = "//div[contains(@class,'custom-control ')]//label[text()='{}']"
        available_boxes = self.get_available_radios()
        for i in list(form_dict.keys()):
            time.sleep(3)
            if i in available_boxes:
                input_box = self._driver().find_element_by_xpath(input_xpath.format(i).format(i))
                input_box.click()
