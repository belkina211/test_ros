from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import os.path


try:
    #ссылка на вход и драйвер
    link="http://web01/Energy_test/Account/Login"
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
    button.click();

    #Выбираем программу 2020-2024
    combo_prog_name = browser.find_element_by_id("combo_prog_name")
    combo_prog_name.click()
    time.sleep(5)
    prog20_button = browser.find_element_by_xpath("/html/body/div[1]/div[1]/div[1]/div/ul/li[6]/span")
    prog20_button.click()
    time.sleep(5)

    #это нужно только для хрома, иначе не пойдет
    combo_prog_name = browser.find_element_by_id("combo_prog_name")
    combo_prog_name.click()
    time.sleep(5)
    prog20_button = browser.find_element_by_xpath("/html/body/div[1]/div[1]/div[1]/div/ul/li[6]/span")
    prog20_button.click()
    time.sleep(5)

    #Переходим на вклдаку "Отчет план/факт"
    monitoring_button = browser.find_element_by_id("monitoring")
    monitoring_button.click()
    time.sleep(3)
    planfact_button = browser.find_element_by_id("plan-fact")
    planfact_button.click()
    time.sleep(5)

    #выбираем один месяц
    combo_months = browser.find_element_by_xpath("//div[@id='TreeDropDown24']//div[@class='ControlCover']")
    combo_months.click()
    time.sleep(3) 
    jan = browser.find_element_by_xpath("//tr[@id='TLVNodeRowMONTHS:1.2020']//span[@class='PPTLVNodeText'][contains(text(),'2020')]")
    jan.click()
    time.sleep(3) 
    y2020 = browser.find_element_by_xpath("//tr[@id='TLVNodeRowYEARS:2020']//span[@class='PPTLVNodeText'][contains(text(),'2020')]")
    y2020.click()
    time.sleep(3)

    #Нажимаем кнопку применить
    apply_button = browser.find_element_by_id("btn-apply-selection")
    apply_button.click()
    apply_button = browser.find_element_by_id("btn-apply-selection")
    apply_button.click()
    time.sleep(25)

    #пробуем скачать отчет
    dowlading_button = browser.find_element_by_xpath('//*[@id="ExpPdfBut"]')
    dowlading_button.click()
    time.sleep(20)
    file_path = "C:/Users/belkina/Downloads/План_Факт_20-24_АНП.pdf"
    os.path.exists(file_path)

except:
    print("Элемент не найден")
    

finally:
    os.remove(file_path)
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
