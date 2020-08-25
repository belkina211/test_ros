#проверка возможности входа в систему с некорректными данными

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
    ps_element.send_keys("Qwerty123455")

    #нажимаем кнопку "Вход"
    button = browser.find_element_by_id("btnSignIn")
    button.click();

    #Ищем на страницу логин
    attention = browser.find_element_by_class_name("attention_reg")
    attention_text = attention.text
    assert "Неверное имя пользователя/пароль" == attention_text, "Вход осуществлен. либо отсуствует надпись о неверном имени пользователя и пароле (тест 2)"

except:
    print("Элемент не найден")

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
