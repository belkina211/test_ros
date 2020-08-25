from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

def input_table():
    try:
        time.sleep(10)
        element = browser.find_element_by_xpath('//*[@id="TabSheet336_table_container"]')
        actions = ActionChains(browser)
        actions.move_to_element(element).click_and_hold().perform()
        element = browser.find_element(By.ID, "TabSheet336_table_container")
        actions = ActionChains(browser)
        actions.move_to_element(element).release().perform()
        browser.find_element(By.ID, "TabSheet336_table_container").click()
        element = browser.find_element(By.CSS_SELECTOR, "#TabSheet336_table_container_selection_border > .PPTSSelectionInnerBorder")
        actions = ActionChains(browser)
        actions.move_to_element(element).click_and_hold().perform()
        element = browser.find_element(By.ID, "TabSheet336_table_container")
        actions = ActionChains(browser)
        actions.move_to_element(element).release().perform()
        browser.find_element(By.CSS_SELECTOR, "#TabSheet336_table_container_selection_border > .PPTSSelectionInnerBorder").click()
        element = browser.find_element(By.CSS_SELECTOR, "#TabSheet336_table_container_selection_border > .PPTSSelectionInnerBorder")
        actions = ActionChains(browser)
        actions.double_click(element).perform()
        browser.find_element(By.CSS_SELECTOR, ".PPTSEditor").send_keys("100")
        time.sleep(3)
        element = browser.find_element(By.ID, "c_6_1_TabSheet336")
        actions = ActionChains(browser)
        time.sleep(3)
        actions.move_to_element(element).click_and_hold().perform()
        time.sleep(3)
        element = browser.find_element(By.ID, "TabSheet336_table_container")
        actions = ActionChains(browser)
        time.sleep(3)
        actions.move_to_element(element).release().perform()
        time.sleep(3)
        browser.find_element(By.ID, "btnSave").click()
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

    #проверяем статус
    at_work_status = browser.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div[1]/div[2]/div/div[1]/div[2]')
    at_work_status_text=at_work_status.text
    assert at_work_status_text=="В работе","Неверный текст кнопки"

    #возвращаемся в реестр мероприятий
    url_event = browser.current_url
    cancel_button = browser.find_element_by_id("btnCancel")
    cancel_button.click()
    time.sleep(3)
    yes_button=browser.find_element_by_xpath("/html/body/div[2]/div/div[3]/div/div/div[1]")
    yes_button.click()
    time.sleep(5)
    

except:
    print("Элемент не найден")
    

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
