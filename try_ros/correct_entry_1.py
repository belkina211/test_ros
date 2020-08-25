#проверка возможности входа в систему с корректными данными

from selenium import webdriver
import time
import urllib

try:
    #ссылка на вход и драйвер
    browser = webdriver.Opera()
    link="http://web01/Energy_test/Account/Login"
    browser.get(link)

    #ввод логина
    lg_element = browser.find_element_by_id("UserName")
    lg_element.send_keys("bel_pnpo")

    #ввод пароля
    ps_element = browser.find_element_by_id("Password")
    ps_element.send_keys("Qwerty12345")

    #нажимаем кнопку "Вход"
    button = browser.find_element_by_id("btnSignIn")
    button.click()

    #Ищем на страницу логин
    login = browser.find_element_by_class_name("user-block__fullname")
    login_text =login.text
    assert "Белкина" == login_text, "Вход не осуществлен (тест 1)"

except:
    print("Элемент не найден")
    

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
