# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.action_chains import ActionChains
import unittest, time, re

class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_untitled_test_case(self):
        driver = self.driver
        driver.get("http://web01/Energy_test/Actions/Edit?id=1025004")
        driver.find_element(By.CSS_SELECTOR, ".tabs__control-item:nth-child(2) > span").click()
        element = self.driver.find_element(By.ID, "c_4_1_TabSheet336")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click_and_hold().perform()
        driver.find_element_by_id("TabSheet336_table_container").click()
        driver.find_element_by_xpath("//div[@id='TabSheet336_table_container_selection_border']/div").click()
        # ERROR: Caught exception [ERROR: Unsupported command [doubleClick | //div[@id='TabSheet336_table_container_selection_border']/div | ]]
        driver.find_element_by_xpath("//div[@id='overlay_14']/textarea").clear()
        driver.find_element_by_xpath("//div[@id='overlay_14']/textarea").send_keys("10")
        driver.find_element_by_id("btnSave").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
