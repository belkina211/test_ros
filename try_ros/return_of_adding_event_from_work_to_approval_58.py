from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

def input_table():
    try:
        time.sleep(5)
        el = browser.find_element_by_css_selector('div.iconTabSheet95_0.PPTSPicture')
        el.click()
        time.sleep(5)
        element = browser.find_element(By.ID, "c_31_4_TabSheet95")
        actions = ActionChains(browser)
        actions.move_to_element(element).double_click().perform()
        browser.find_element(By.CSS_SELECTOR, ".PPTSEditor").send_keys("56")
        element = browser.find_element(By.ID, "TabSheet95_table_container")
        actions = ActionChains(browser)
        actions.move_to_element(element).release().perform()
        element = browser.find_element(By.ID, "c_32_4_TabSheet95")
        actions = ActionChains(browser)
        actions.move_to_element(element).click().perform()
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
    time.sleep(3);
    ok_button = browser.find_element_by_id("ActionParamFormOk")
    ok_button.click()
    time.sleep(7)

    #запомнляем мероприятие данными
    support_radio = browser.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/div[2]/div[1]/form/div[1]/div/div[5]/div[2]/label[2]")
    support_radio.click()
    sv_button = browser.find_element_by_id("btnSave")
    sv_button.click()   
    time.sleep(5) 
    fact_button = browser.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/div[1]/div[2]/span")
    fact_button.click()
    time.sleep(17)
    ok=False
    for i in range(20):
        ok=input_table()
        if ok==True: break    
        browser.refresh()
        time.sleep(10)
    time.sleep(5)
    sv_button = browser.find_element_by_id("btnSave")
    sv_button.click()

    #отправяем на согласование
    time.sleep(5)
    send_for_approval_button = browser.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div[2]/div[2]/div/div')
    send_for_approval_button.click()
    time.sleep(5)
    yes_button= browser.find_element_by_xpath('/html/body/div[3]/div/div[3]/div/div/div[1]')
    yes_button.click()
    time.sleep(5)

    #Возаращаем в работу
    send_to_work_button = browser.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div[2]/div[2]/div/div[2]')
    send_to_work_button.click()
    time.sleep(5)
    yes_button= browser.find_element_by_xpath('/html/body/div[3]/div/div[3]/div/div/div[1]')
    yes_button.click()
    time.sleep(5)

    #Провряем статус
    return_to_work_status = browser.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div[1]/div[2]/div/div[2]/div[2]') 
    return_to_work_status_text=return_to_work_status.text
    assert return_to_work_status_text=="В работе","Неверный текст кнопки"
    
    

except:
    print("Элемент не найден")
    

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

