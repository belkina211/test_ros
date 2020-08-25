#проверяем раздачу прав для контроллера глобального
from selenium import webdriver
import time

try:
    #ссылка на вход и драйвер
    link="http://web01/Energy_test/Account/Login"
    browser = webdriver.Opera()
    browser.get(link)
    browser.maximize_window()

    #ввод логина
    lg_element = browser.find_element_by_id("UserName")
    lg_element.send_keys("kg")

    #ввод пароля
    ps_element = browser.find_element_by_id("Password")
    ps_element.send_keys("Qwerty12345")

    #нажимаем кнопку "Вход"
    enter_button = browser.find_element_by_id("btnSignIn")
    enter_button.click()

    #расскрываем раздел "Задачи"
    tasks_button = browser.find_element_by_id("tasks")
    tasks_button.click()

    #Проверяем, что права правильно раздаются. Если неправильно - выпадет исключение  
    actionsOnCoord_button = browser.find_element_by_id("ActionsOnCoord") #раздел "Мероприятия на содобрении"
    performActionsOnCoord_button = browser.find_element_by_id("PerformActionsOnCoord") #раздел "Исполнение мероприятий на одобрении"

    #расскрываем раздел "Программа ПЭС 5 лет"
    prog_5y_button = browser.find_element_by_id("prog-5y")
    prog_5y_button.click()

    #Проверяем, что права правильно раздаются. Если неправильно - выпадет исключение  
    tariffs5y_button = browser.find_element_by_id("tariffs-5y") #Тарифы
    formProg_button = browser.find_element_by_id("FormProg") #Сформированная програма
    divaims_button = browser.find_element_by_id("divaims") #Целевые показатели
    divisions5y_button = browser.find_element_by_id("divisions-5y") #Подразделения
    minenergoForms_button = browser.find_element_by_id("MinenergoForms") #Формы минэнерго
    repMacroeconomicFactors_button = browser.find_element_by_id("RepMacroeconomicFactors") #Макроэкономический показатели
    ImpactOnUREPlan_button = browser.find_element_by_id("ImpactOnUREPlan") #Влияние на УРЭ

    #расскрываем раздел "Мониторинг исполнения программы"
    monitoring_button = browser.find_element_by_id("monitoring")
    monitoring_button.click()

    #Проверяем, что права правильно раздаются. Если неправильно - выпадет исключение 
    plan_fact_button = browser.find_element_by_id("plan-fact") #Отчет план/факт
    repByDivis_button = browser.find_element_by_id("RepByDivis") #Контроль исполнения по месяцам
    divisions1y_button = browser.find_element_by_id("divisions-1y") #Контроль исполнения по сегментам
    repTotal_button = browser.find_element_by_id("RepTotal") #Свод
    impactOnURE_button = browser.find_element_by_id("ImpactOnURE") #Влияние на УРЭ

    #расскрываем раздел "Параметры программы"
    prog_params_button = browser.find_element_by_id("prog-params")
    prog_params_button.click()

    #Проверяем, что права правильно раздаются. Если неправильно - выпадет исключение 
    subnorms_button = browser.find_element_by_id("subnorms") #Нормативы эффективности

     #проверяем наличие раздела "Моделированик" и проверяем,что он нажимаем
    modeling_button = browser.find_element_by_id('Modeling')
    modeling_button.click()
    
    #проверяем наличие раздела "Инструкции" и проверяем,что он нажимаем
    guide_button = browser.find_element_by_id("guide")
    guide_button.click()

except:
    print("Элемент не найден")
    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
