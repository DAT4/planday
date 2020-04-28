import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from config import *

class Automat:
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.driver.get('https://bastardcafe.planday.dk')
        self.driver.find_element_by_id('Username').send_keys(USERNAME)
        self.driver.find_element_by_id('Password').send_keys(PASSWORD)
        self.driver.find_element_by_xpath('/html/body/div/div/div[2]/div/div/div[2]/form/button[3]').click()
        self.driver.get('https://bastardcafe.planday.dk/Pages/PortalPage.aspx?PageId=102009&nav=menu')

    def cannot_work(self,month):
        element = self.driver.find_element_by_id('ctl00_M_CM_CM_m0_DayPickerControl_dateInput')
        element.send_keys(month+' 2020')
        time.sleep(SLEEP_TIME)
        element = self.driver.find_element_by_xpath('//*[@id="ctl00_M_CM_CM_m0_BtnEditAll"]')
        element.click()
        time.sleep(SLEEP_TIME)
        elements = self.driver.find_elements_by_class_name('rgEditRow')
        for element in elements:
            print(element.text)
            date = element.find_element_by_xpath('.//td[3]').text
            timer = element.find_elements_by_class_name('time-picker')
            if date in free_days:
                can_work = Select(element.find_element_by_class_name('skip-auto-select2'))
                can_work.select_by_value('0')
            elif date in early_days:
                can_work = Select(element.find_element_by_class_name('skip-auto-select2'))
                can_work.select_by_value('0')
                timer[0].send_keys(EARLY_END)
                timer[1].send_keys(BASTARD_CLOSE)
            elif date in late_days:
                can_work = Select(element.find_element_by_class_name('skip-auto-select2'))
                can_work.select_by_value('0')
                timer[0].send_keys(BASTARD_OPEN)
                timer[1].send_keys(LATE_START)
            elif date in allday_days:
                can_work = Select(element.find_element_by_class_name('skip-auto-select2'))
                can_work.select_by_value('-1')
        self.driver.find_element_by_id('ctl00_M_CM_CM_m0_BtnSaveAll').click()
