#проверка корректной раздачи прав для энергоменеджера

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
    lg_element.send_keys("en")

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
    actionsEM_button = browser.find_element_by_id("ActionsEM") #раздел "Мероприятия в работе"
    performActionsOnCompletion_button = browser.find_element_by_id("ActionsEM") #раздел "Исполнения мероприятий на доработке"

    #расскрываем раздел "Программа ПЭС 5 лет"
    prog_5y_button = browser.find_element_by_id("prog-5y")
    prog_5y_button.click()

    #Проверяем, что права правильно раздаются. Если неправильно - выпадет исключение  
    tariffs5y_button = browser.find_element_by_id("tariffs-5y") #Тарифы
    usActions_button = browser.find_element_by_id("usActions") #Классификатор
    actions5y_button = browser.find_element_by_id("actions-5y") #Мероприятия
    formProg_button = browser.find_element_by_id("FormProg") #Сформированная програма
    divaims_button = browser.find_element_by_id("divaims") #Целевые показатели
    agreement5y_button = browser.find_element_by_id("agreement-5y") #Согласование
    minenergoForms_button = browser.find_element_by_id("MinenergoForms") #Формы минэнерго
    repMacroeconomicFactors_button = browser.find_element_by_id("RepMacroeconomicFactors") #Макроэкономический показатели
    ImpactOnUREPlan_button = browser.find_element_by_id("ImpactOnUREPlan") #Влияние на УРЭ

    #расскрываем раздел "Мониторинг исполнения программы"
    monitoring_button = browser.find_element_by_id("monitoring")
    monitoring_button.click()

    #Проверяем, что права правильно раздаются. Если неправильно - выпадет исключение 
    tariffs1y_button = browser.find_element_by_id("tariffs-1y") #Тарифы
    monit_button = browser.find_element_by_id("monit") #Ежемесяные отчеты
    plan_fact_button = browser.find_element_by_id("plan-fact") #Отчет план/факт
    agreement_1y_button = browser.find_element_by_id("agreement-1y") #Согласование
    repTotal_button = browser.find_element_by_id("RepTotal") #Свод
    impactOnURE_button = browser.find_element_by_id("ImpactOnURE") #Влияние на УРЭ

    #расскрываем раздел "Параметры программы"
    prog_params_button = browser.find_element_by_id("prog-params")
    prog_params_button.click()

    #Проверяем, что права правильно раздаются. Если неправильно - выпадет исключение 
    subnorms_button = browser.find_element_by_id("subnorms") #Нормативы эффективности

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