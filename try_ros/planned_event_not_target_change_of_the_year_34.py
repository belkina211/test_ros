from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

try:
    #ссылка на вход и драйвер
    link="http://web01/Energy_test/Account/Login"
    browser = webdriver.Opera()
    browser.get(link)
    browser.maximize_window()

    #ввод логина
    lg_element = browser.find_element_by_id("UserName")
    lg_element.send_keys("bel_ngdo")

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

    #Переходим на вклдаку "Классификатор", отмечаем все
    prog_5y_button = browser.find_element_by_id("prog-5y")
    prog_5y_button.click()
    time.sleep(3)
    usActions_button = browser.find_element_by_id("usActions")
    usActions_button.click()
    time.sleep(3)
    check_all_button = browser.find_element_by_id("CheckAll")
    check_all_button.click()
    time.sleep(3)

    #Переходим на вкладку "Мероприятия"
    actions5y_button = browser.find_element_by_id("actions-5y")
    actions5y_button.click()

    #Выбираем в комбобоксе "Отобразить мероприятия с годом начала" значение 2020
    showEvents_combo = browser.find_element_by_id("showEventsYearsStartBox")
    showEvents_combo.click()
    time.sleep(3)
    pr20_button = browser.find_element_by_xpath('html/body/div[2]/div[1]/div[1]/div/table/tbody/tr[6]/td/div/div[2]/div[2]/span')
    pr20_button.click()
    time.sleep(3)
    apply_selection_button = browser.find_element_by_id("btn-apply-selection")
    apply_selection_button.click()
    time.sleep(5)

    #Пробуем создать мероприятие
    browser.find_element_by_xpath("//*[text()='1.1 Реализация энергосберегающего потенциала на механизированном фонде скважин']").click()
    time.sleep(10)
    newEvent = browser.find_element_by_id("NewEvent")
    newEvent.click()
    time.sleep(3)

    #В окне создания выбираем "нецелевое", создаем
    necel_radio = browser.find_element_by_xpath("/html/body/div[3]/div/div[2]/div[2]/div/label[2]")
    necel_radio.click()
    time.sleep(3)

    #устанавливаем другой год начала
    effectYear_combo = browser.find_element_by_xpath("/html/body/div[3]/div/div[2]/div[5]/div[2]/div/div")
    time.sleep(5)
    effectYear_combo.click()
    year_2019 = browser.find_element_by_id("Year2021")
    time.sleep(5)
    year_2019.click()
    time.sleep(5)
    effectYear_combo.click()

    #устаналиваем начала финансирвоания на февраль
    effectMon_combo = browser.find_element_by_xpath("/html/body/div[3]/div/div[2]/div[6]/div[2]/div/div")
    effectMon_combo.click()
    time.sleep(3)
    feb_mon = browser.find_element_by_id("Mon2")
    feb_mon.click()
    time.sleep(3)
    effectMon_combo.click()
    time.sleep(3)
    
    #Провереям, что месяц поменялся
    endingMon_combo = browser.find_element_by_xpath("/html/body/div[3]/div/div[2]/div[7]/div[2]/div/div")
    endingMon_combo_text = endingMon_combo.text

    assert (endingMon_combo_text=="Февраль"),"Неверный текст кнопки"

except:
    print("Элемент не найден")
    

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
