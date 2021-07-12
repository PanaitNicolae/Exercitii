from Driver import *
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
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
        generic_xpath = "//div[(contains(@id, 'wrapper') or contains(@id, 'Wrapper')) and .//label[text()='{}']]"
        labels_types_dict = self.get_labels()
        
        for i in data_dict.keys():
            element = self._driver().find_elements_by_xpath((generic_xpath + "//input").format(i))

            if "Date" in i:
                ymd_list = data_dict[i].split()
                self.set_date(ymd_list[0], ymd_list[1], ymd_list[2])   
                
            elif i == "State and City":
                self.select_state_city(data_dict[i][0], data_dict[i][1])
                
            elif labels_types_dict[i] == "text":
                if len(element) == 2:
                    element[0].send_keys(data_dict[i][0])
                    element[1].send_keys(data_dict[i][1])
                else:
                    element[0].send_keys(data_dict[i])
            
            elif labels_types_dict[i] == "radio":
                if data_dict[i] == True:
                    self.check_radio(i)
            
            elif labels_types_dict[i] == "checkbox":
                if data_dict[i] == True:
                    self.check_box(i)
                    
            elif labels_types_dict[i] == "textarea":
                element2 = self._driver().find_element_by_xpath((generic_xpath + "//textarea").format(i))
                element2.send_keys(data_dict[i])
                


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
         
    
    def select_state_city(self, state, city):
        state_xpath = "//div[@id='state']//input"
        city_xpath = "//div[@id='city']//input"
        choose_state_xpath = "//div[@id='state']//div[contains(text(), '{}')]"
        choose_city_xpath = "//div[@id='city']//div[contains(text(), '{}')]"
        action = ActionChains(self._driver())
        
        self._driver().execute_script("window.scrollTo(0, 520)") 
        
        state_element = self._driver().find_element_by_xpath(state_xpath)
        action.click(state_element).perform()
        time.sleep(0.2)
        
        try:
            choose_state = self._driver().find_element_by_xpath(choose_state_xpath.format(state))
            choose_state.click()
        except:
            raise Exception("Wrong state!")
        
        city_element = self._driver().find_element_by_xpath(city_xpath)
        action.click(city_element).perform()
        time.sleep(0.2)
        
        try:
            choose_city = self._driver().find_element_by_xpath(choose_city_xpath.format(city))
            choose_city.click()
        except:
            raise Exception("Wrong City!")
        
    def check_radio(self, label):
        generic_xpath = "//div[(contains(@id, 'wrapper') or contains(@id, 'Wrapper'))]//div[./label[text()='{}']]//input"
        action = ActionChains(self._driver())  
        radio = self._driver().find_element_by_xpath(generic_xpath.format(label))
        action.click(radio).perform()
        
    def check_box(self, label):
        generic_xpath = "//div[(contains(@id, 'wrapper') or contains(@id, 'Wrapper'))]//div[./label[text()='{}']]//input"
        action = ActionChains(self._driver())  
        box = self._driver().find_element_by_xpath(generic_xpath.format(label))
        action.click(box).perform() 
    
    def upload(self):
        upload_button_xpath = "//input[@id='uploadPicture']"
        upload = self._driver().find_element_by_xpath(upload_button_xpath)
        
        pic_path = "C:\ROBOT_COMPLET.jpeg"
        upload.send_keys(pic_path)
        
