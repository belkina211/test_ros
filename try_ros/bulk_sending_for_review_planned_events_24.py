from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

def input_table():
    try:
        time.sleep(5)
        element = browser.find_element(By.ID, "c_4_5_TabSheet335")
        actions = ActionChains(browser)
        actions.move_to_element(element).double_click().perform()
        browser.find_element(By.CSS_SELECTOR, ".PPTSEditor").send_keys("56")
        element = browser.find_element(By.ID, "TabSheet335_table_container")
        actions = ActionChains(browser)
        actions.move_to_element(element).release().perform()
        element = browser.find_element(By.ID, "c_4_6_TabSheet335")
        actions = ActionChains(browser)
        actions.move_to_element(element).click().perform()
        time.sleep(5)
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
    time.sleep(5);

    #Пробуем создать мероприятие
    browser.find_element_by_xpath("//*[text()='1.1 Реализация энергосберегающего потенциала на механизированном фонде скважин']").click()
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
    plan_button = browser.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/div[1]/div[2]/span")
    plan_button.click()
    time.sleep(17)
    ok=False
    for i in range(5):
        ok=input_table()
        if ok==True: break    
        browser.refresh()
        time.sleep(10)
        plan_button = browser.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/div[1]/div[2]/span")
        plan_button.click()
    time.sleep(5)
    sv_button = browser.find_element_by_id("btnSave")
    sv_button.click()

    #Проверяем, что мероприятие прошло контроль эффективности 
    eco_button = browser.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/div[1]/div[3]/span")
    eco_button.click()
    time.sleep(5)

    #Отправляем мероприятение на согласование
    url_event = browser.current_url
    send_for_approval_button = browser.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div[2]/div[2]/div/div')
    send_for_approval_button.click()
    time.sleep(5)
    yes_button= browser.find_element_by_xpath('/html/body/div[3]/div/div[3]/div/div/div[1]')
    yes_button.click()
    time.sleep(15)

    #Отправляем мероприятие массового на рассмотрение
    review_button = browser.find_element_by_id("btnSendToReviewAll")
    review_button.click()
    time.sleep(5)
    yes_button=browser.find_element_by_xpath("/html/body/div[3]/div/div[3]/div/div/div[1]")
    yes_button.click()
    time.sleep(5)

    #Возвращаемся в мероприятие, проверяем статус
    browser.get(url_event)
    return_to_work_status = browser.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div[1]/div[2]/div/div[1]/div[2]') 
    return_to_work_status_text=return_to_work_status.text
    assert return_to_work_status_text=="На рассмотрении","Неверный текст кнопки"
    

except:
    print("Элемент не найден")
    

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
