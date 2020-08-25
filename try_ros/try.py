from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


link="http://web01/Energy_test/Action1y?id=1025634&month=1"
browser = webdriver.Opera()
browser.get(link)
browser.maximize_window()
#ввод логина
lg_element = browser.find_element_by_id("UserName")
lg_element.send_keys("bel_pnpo")

#ввод пароля
ps_element = browser.find_element_by_id("Password")
ps_element.send_keys("Qwerty12345")

#нажимаем кнопку "Вход"
button = browser.find_element_by_id("btnSignIn")
button.click()
time.sleep(5)

el = browser.find_element_by_css_selector('div.iconTabSheet95_0.PPTSPicture')
el.click()

el_tab = browser.find_element_by_id("c_31_4_TabSheet95")
el_tab.click()
actionChains = ActionChains(driver)
actionChains.double_click(el_tab).perform()

