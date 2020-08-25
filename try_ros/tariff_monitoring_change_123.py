from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

def send_tariff():
    try:
        time.sleep(5)
        element = browser.find_element(By.ID, "c_2_5_TabSheet80")
        actions = ActionChains(browser)
        actions.move_to_element(element).double_click().perform()
        browser.find_element(By.CSS_SELECTOR, ".PPTSEditor").send_keys("5")
        return True
    except:
        return False

def delete_tariff():
    try:
        time.sleep(5)
        element = browser.find_element(By.ID, "c_2_5_TabSheet80")
        actions = ActionChains(browser)
        actions.move_to_element(element).double_click().perform()
        browser.find_element(By.CSS_SELECTOR, ".PPTSEditor").send_keys("")
        return True
    except:
        return False

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

    #Переходим на вклдаку "Тарифы"
    monitoring_button = browser.find_element_by_id("monitoring")
    monitoring_button.click()
    time.sleep(3)
    tariffs1y_button = browser.find_element_by_id("tariffs-1y")
    tariffs1y_button.click()
    time.sleep(5)

    #пробуем заполнить тариф
    ok=False
    for i in range(20):
        ok=send_tariff()
        if ok==True: break    
        browser.refresh()
        time.sleep(5)
    time.sleep(5)
    save_button = browser.find_element_by_id("btnSave")
    save_button.click()
    time.sleep(15)

    #пробуем удалить тариф
    ok=False
    for i in range(20):
        ok=delete_tariff()
        if ok==True: break    
        browser.refresh()
        time.sleep(5)
    time.sleep(5)
    save_button = browser.find_element_by_id("btnSave")
    save_button.click()
    time.sleep(15)

except:
    print("Элемент не найден")
    

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
