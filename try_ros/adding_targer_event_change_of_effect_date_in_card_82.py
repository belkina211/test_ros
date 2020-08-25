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
    prog20_button = browser.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/ul[1]/li[6]")
    prog20_button.click()
    time.sleep(5)

    #это нужно только для хрома, иначе не пойдет
    combo_prog_name = browser.find_element_by_id("combo_prog_name")
    combo_prog_name.click()
    time.sleep(5)
    prog20_button = browser.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/ul[1]/li[6]")
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

    #расскрываем раздел "Мониторинг исполнения программы"
    monitoring_button = browser.find_element_by_id("monitoring")
    monitoring_button.click()

    #Переходим на вкладку "Ежемесячный отчет"
    monit_button = browser.find_element_by_id("monit")
    monit_button.click()
    time.sleep(5)

    #Выбираем в комбобоксе "Январь", применить
    data_combo = browser.find_element_by_id("RepDatText")
    data_combo.click()
    time.sleep(3)
    jan = browser.find_element_by_id("Mon1")
    jan.click()
    apply_button = browser.find_element_by_id("btn-apply-selection")
    apply_button.click()
    time.sleep(10)

    #Пробуем создать мероприятие
    browser.find_element_by_xpath("//*[text()='1.1.1 Отопление']").click()
    newEvent = browser.find_element_by_id("NewEvent")
    newEvent.click()
    time.sleep(3);

    #В окне создания выбираем "целевое", создаем
    cel_radio = browser.find_element_by_xpath("/html/body/div[3]/div/div[2]/div[2]/div/label[1]")
    cel_radio.click()
    time.sleep(3)
    ok_button = browser.find_element_by_id("ActionParamFormOk")
    ok_button.click()
    time.sleep(3)

    #Меняем дату в карточке меропиятия
    date_change = browser.find_element_by_id("edit_factstartdate")
    date_change.click()
    time.sleep(3)

    #устаналиваем начала финансирвоания на февраль
    effectMon_combo = browser.find_element_by_id("comboEffectMonthText")
    effectMon_combo.click()
    time.sleep(3)
    feb_mon = browser.find_element_by_id("EffectMon2")
    feb_mon.click()
    time.sleep(3)
    effectMon_combo.click()
    time.sleep(3)

    #сохраняем данные 
    ok_button = browser.find_element_by_id("ActionDateParamFormOk")
    ok_button.click()
    time.sleep(3)

    #Провереям, сообщение об ошибки
    notif = browser.find_element_by_xpath("//body/div[3]/div[1]/div[2]")
    notif_text = notif.text
    assert notif_text=="Месяц окончания последнего этапа не может быть меньше месяца начала получения эффекта","Неверный текст"
   

except:
    print("Элемент не найден")
    

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

