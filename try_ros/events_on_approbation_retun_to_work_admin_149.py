from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


def input_table():  #ввод в таблицу
    try:
        time.sleep(5)
        element = browser.find_element(By.ID, "c_4_5_TabSheet339")
        actions = ActionChains(browser)
        actions.move_to_element(element).double_click().perform()
        browser.find_element(By.CSS_SELECTOR, ".PPTSEditor").send_keys("56")
        element = browser.find_element(By.ID, "TabSheet339_table_container")
        actions = ActionChains(browser)
        actions.move_to_element(element).release().perform()
        element = browser.find_element(By.ID, "c_4_6_TabSheet339")
        actions = ActionChains(browser)
        actions.move_to_element(element).click().perform()
        time.sleep(5)
        return True
    except:
        return False

def find_element():  #находит расскрывающий элемент
    try:
        elements = browser.find_elements_by_xpath("//div[contains(@class,'PPTSExpander PPTSEEXPP')]")
        element = elements[-1]
        element.click()
        #прокрутка страницы
        try:
            scroll_down_elements = browser.find_elements_by_xpath("//div[@class='ArrowCell Right']")
            scroll_down = scroll_down_elements[0]
            for i in range(50):
                scroll_down.click()
        finally:
            #чекбокс в таблице 
            elements = browser.find_elements_by_xpath("//div[contains(@class,'iconTabSheet')]")
            element = elements[-1]
            element.click()
            return True
    except:
        return False

def find_icon():  #находит чекбокс у элемента в таблице
    try:
        elements = browser.find_elements_by_xpath("//div[contains(@class,'iconTabSheet394_1 PPTSPicture')]")
        element = elements[-1]
        element.click()
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
    button.click()
    time.sleep(5)

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
    time.sleep(15)

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
    time.sleep(2)
    plan_button = browser.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/div[1]/div[2]/span")
    plan_button.click()
    time.sleep(15)
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
    sv_button.click
    time.sleep(5)

    #Проверяем, что мероприятие прошло контроль эффективности 
    eco_button = browser.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/div[1]/div[3]/span")
    eco_button.click()
    time.sleep(10)

    #Отправляем мероприятение на согласование
    url_event = browser.current_url
    send_for_approval_button = browser.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div[2]/div[2]/div/div')
    send_for_approval_button.click()
    time.sleep(5)
    yes_button= browser.find_element_by_xpath('/html/body/div[3]/div/div[3]/div/div/div[1]')
    yes_button.click()
    time.sleep(5)

    #Отправляем мероприятение на рассмотрение
    browser.get(url_event)
    send_for_review_button = browser.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div[2]/div[2]/div/div')
    send_for_review_button.click()
    time.sleep(5)
    yes_button = browser.find_element_by_xpath('/html/body/div[3]/div/div[3]/div/div/div[1]')
    yes_button.click()
    time.sleep(10)

    #выход из системы 
    name_og = browser.find_element_by_xpath("//div[@class='user-block__work']")
    name_og_text = name_og.text
    exit_button = browser.find_element_by_id("LogOffLnk")
    exit_button.click()
    time.sleep(3)

    #Подтверждение выхода
    yes_button = browser.find_element_by_xpath('/html[1]/body[1]/div[3]/div[1]/div[3]/div[1]/div[1]/div[1]')
    yes_button.click()

    #вход за админа
    lg_element = browser.find_element_by_id("UserName")
    lg_element.send_keys("adm")
    ps_element = browser.find_element_by_id("Password")
    ps_element.send_keys("Qwerty12345")

    #нажимаем кнопку "Вход"
    button = browser.find_element_by_id("btnSignIn")
    button.click()

    #Переходим на "Задачи" - "Мероприятия на одобрении"
    prog_5y_button = browser.find_element_by_id("tasks")
    prog_5y_button.click()
    time.sleep(3)
    usActions_button = browser.find_element_by_id("ActionsOnCoord")
    usActions_button.click()
    time.sleep(25)

    #выбираем ог
    combo_button = browser.find_element_by_xpath('/html[1]/body[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]')
    combo_button.click()
    time.sleep(3)
    og_combo = browser.find_element_by_xpath("//*[contains(text(),'АО «Ульяновскнефтепродукт»')]")
    og_combo.click()
    time.sleep(3)

   
    #расскрываем последний элемент
    ok=False
    for i in range(15):
        #нажимаем кнопку применить 
        apply_button = browser.find_element_by_id("btn-apply-selection")
        apply_button.click()
        time.sleep(25)

        #еще раз 
        apply_button = browser.find_element_by_id("btn-apply-selection")
        apply_button.click()
        time.sleep(25)
    
        ok=find_element()
        if ok==True: break 
        browser.refresh()
        time.sleep(10)

    return_to_work_button = browser.find_element_by_id("proBtn_190")
    return_to_work_button.click()
    time.sleep(15)    

    browser.get(url_event)
    time.sleep(10)
    work_status= browser.find_element_by_class_name("status__text") 
    work_status_text = work_status.text
    assert work_status_text=="В работе","Неверный текст кнопки"
        

except:
    print("Элемент не найден")
    time.sleep(25)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

