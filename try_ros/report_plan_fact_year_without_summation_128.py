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

    #убираем суммирование, нажимаем кнопку применить
    mark_button = browser.find_element_by_xpath("//span[@class='fake']")
    mark_button.click()
    time.sleep(5)
    apply_button = browser.find_element_by_id("btn-apply-selection")
    apply_button.click()
    time.sleep(25)

    #сверяем название страницы
    name_page = browser.find_element_by_xpath("//b[contains(@class,'pane__item')]")
    name_page_text = name_page.text
    assert (name_page_text=="ОТЧЕТ ПЛАН/ФАКТ"),"Неверный текст кнопки"

except:
    print("Элемент не найден")
    

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем брауз
    browser.quit()
