#проверка возможности отмены выхода из системы

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

    #Отменяем выход
    yes_button = browser.find_element_by_xpath('/html/body/div[2]/div/div[3]/div/div/div[2]')
    yes_button.click()

    #Ищем на страницу логин, чтобы понять, что мы не вышли
    login = browser.find_element_by_class_name("user-block__fullname")
    login_text =login.text
    assert "Белкина" == login_text, "Был произведен выход из приложения"

except:
    print("Элемент не найден")
    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()