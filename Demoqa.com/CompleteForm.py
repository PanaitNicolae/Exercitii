from Driver import *
import time
from selenium.webdriver.common.action_chains import ActionChains
from Navigate import *
from cProfile import label
import types


class CompleteForm(Driver):
    
    
    def get_labels(self):
        generic_xpath = "//div[(contains(@id, 'wrapper') or contains(@id, 'Wrapper'))]"
        elements = self._driver().find_elements_by_xpath(generic_xpath)   

        labels = []
        types = []
        input_xpath = []
        for i in elements:
            elements2_label = i.find_elements_by_xpath(".//div[.//input and .//label]//label") 
            elements2_type = i.find_elements_by_xpath(".//div[.//input and .//label]//input") 
            elements1_label = i.find_elements_by_xpath(".//label")
            elements1_type = i.find_elements_by_xpath(".//input | .//textarea")
            
            if len(elements2_label) !=0:
                for j, k in zip(elements2_label, elements2_type):
                    labels.append(j.text)
                    types.append(k.get_attribute("type"))
                    
            elif len(elements2_label) == 0:                
                for j, k in zip(elements1_label, elements1_type):
                    labels.append(j.text)
                    types.append(k.get_attribute("type"))

        print(dict(zip(labels, types)))
        return dict(zip(labels, types))

    def complete(self, data_dict):
        generic_xpath = "//div[(contains(@id, 'wrapper') or contains(@id, 'Wrapper')) and .//label[text()='{}']]//input"
        labels_types_dict = self.get_labels()
        
        for i in labels_types_dict.keys():
            element = self._driver().find_elements_by_xpath(generic_xpath.format(i))
            
            if labels_types_dict[i] == "text":
                if i == "Name":
                    element[0].send_keys(data_dict["FirstName"])
                    element[1].send_keys(data_dict["LastName"])
                
                elif i == "Email":
                    element.send_keys(data_dict[i])
                
                # elif i == ""


    def set_date(self, year, month, day):
         generic_xpath = "//div[(contains(@id, 'wrapper') or contains(@id, 'Wrapper'))]"
         select_year_xpath = generic_xpath + "//select[contains(@class, 'year')]"
         select_month_xpath = generic_xpath + "//select[contains(@class, 'month')]"
         choose_year_xpath = select_year_xpath + "//option[@value = '{}']"
         choose_month_xpath = select_month_xpath + "//option[text() = '{}']"
         choose_day_xpath = generic_xpath + "//div[@class = 'react-datepicker__month']//div[text() = '{}' and contains(@aria-label, '{}')]"
         
         date_input = self._driver().find_element_by_id("dateOfBirthInput")
         date_input.click()
         
         select_year = self._driver().find_element_by_xpath(select_year_xpath)
         select_year.click()
         
         choose_year = self._driver().find_element_by_xpath(choose_year_xpath.format(year))
         choose_year.click()
         
         select_month = self._driver().find_element_by_xpath(select_month_xpath)
         select_month.click()
         
         choose_month = self._driver().find_element_by_xpath(choose_month_xpath.format(month))
         choose_month.click()
         
         choose_day = self._driver().find_element_by_xpath(choose_day_xpath.format(day, month))
         choose_day.click()
         
         
    def upload(self):
        upload_button_xpath = "//input[@id='uploadPicture']"
        upload = self._driver().find_element_by_xpath(upload_button_xpath)
        
        pic_path = "C:\ROBOT_COMPLET.jpeg"
        upload.send_keys(pic_path)
        
