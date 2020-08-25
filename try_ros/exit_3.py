#проверка возможности выход из системы

from selenium import webdriver
import time

try:
    #ссылка на вход и драйвер
    link="http://web01/Energy_test/Account/Login"
    browser = webdriver.Opera()
    browser.get(link)

    #ввод логина
    lg_element = browser.find_element_by_id("UserName")
    lg_element.send_keys("bel_pnpo")

    #ввод пароля
    ps_element = browser.find_element_by_id("Password")
    ps_element.send_keys("Qwerty12345")

    #нажимаем кнопку "Вход"
    enter_button = browser.find_element_by_id("btnSignIn")
    enter_button.click()

    #Выходим со страницы
    exit_button = browser.find_element_by_id("LogOffLnk")
    exit_button.click()

    #Подтверждение выхода
    yes_button = browser.find_element_by_xpath('/html/body/div[2]/div/div[3]/div/div/div[1]')
    yes_button.click()

    #Ищем надписи  "Логин" и "Пароль"
    login_label = browser.find_element_by_xpath('/html/body/div[1]/div/form/div/div[1]/div/div/label')
    password_label = browser.find_element_by_xpath('/html/body/div[1]/div/form/div/div[2]/div/div/label')
    login_label_text = login_label.text
    password_label_text = password_label.text
    assert ("Логин"==login_label_text) & (password_label_text=="Пароль"), "Выход не осуществлен (тест 3)"

except: #NoSuchElementException
    print("Третий тест не пройден")
       

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
