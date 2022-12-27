from selenium import webdriver
from selenium.webdriver.common.by import By
from config import correct_name, correct_email, correct_password, incorrect_password, correct_phone
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import pytest
import time

@pytest.fixture(autouse=True)
def testing():
    # инициализация драйвера
    selenium = webdriver.Chrome()
    selenium.implicitly_wait(10)
    # открытие сайта
    selenium.get('https://b2c.passport.rt.ru')

    yield selenium
    selenium.quit()

# TEST_012
# проверка, что пользователь может перейти на страницу авторизации
def test_opening_authorization_page(testing):
    selenium = testing
    # открытие сайта
    selenium.get('https://b2c.passport.rt.ru')

    element = WebDriverWait(selenium, 10).until(EC.visibility_of_element_located((By.ID, 'kc-login')))

    assert selenium.find_element(By.TAG_NAME, 'h1').text == 'Авторизация', print('Тест провален')
    assert selenium.find_element(By.ID, 'kc-login'), print('Тест провален')

    # снимок экрана с результатом теста
    selenium.save_screenshot('test_opening_authorization_page.png')

# TEST_013
# проверка, что пользователь может открыть чат поддержки на странице авторизации
def test_opening_chat_authorization_page(testing):
    selenium = testing
    # открытие сайта
    selenium.get('https://b2c.passport.rt.ru')

    element = WebDriverWait(selenium, 10).until(EC.visibility_of_element_located((By.ID, 'kc-login')))

    # нажать на виджет "Поддержка"
    selenium.find_element(By.ID, 'widget_bar').click()
    time.sleep(3)

    assert selenium.find_element(By.ID, 'widget_sendPrechat'), print('Тест провален')

    # снимок экрана с результатом теста
    selenium.save_screenshot('test_opening_chat_authorization_page.png')

# TEST_014
# проверка, что на странице авторизации есть продуктовый слоган
def test_authorization_grocery_slogan(testing):
    selenium = testing
    # открытие сайта
    selenium.get('https://b2c.passport.rt.ru')

    element = WebDriverWait(selenium, 10).until(EC.visibility_of_element_located((By.ID, 'kc-login')))

    assert selenium.find_element(By.TAG_NAME, 'p').text == 'Персональный помощник в цифровом мире Ростелекома', \
        print('Тест провален')

    # снимок экрана с результатом теста
    selenium.save_screenshot('test_authorization_grocery_slogan.png')

# TEST_015
# проверка, что таб выбора авторизации по номеру, "Номер"
def test_opening_authorization_page_2(testing):
    selenium = testing
    # открытие сайта
    selenium.get('https://b2c.passport.rt.ru')

    element = WebDriverWait(selenium, 10).until(EC.visibility_of_element_located((By.ID, 'kc-login')))

    # таб "Телефон"
    selenium.find_element(By.ID, 't-btn-tab-phone').click()
    # снимок экрана с результатом теста
    selenium.save_screenshot('test_opening_authorization_page_2.png')
    time.sleep(3)

    assert selenium.find_element(By.ID, 't-btn-tab-phone').text == 'Номер', print('Тест провален')

# TEST_016
# проверка, что таб выбора авторизации по логину и паролю, "Почта"
def test_opening_authorization_page_3(testing):
    selenium = testing
    # открытие сайта
    selenium.get('https://b2c.passport.rt.ru')

    element = WebDriverWait(selenium, 10).until(EC.visibility_of_element_located((By.ID, 'kc-login')))

    # таб "Логин"
    selenium.find_element(By.ID, 't-btn-tab-login').click()
    # снимок экрана с результатом теста
    selenium.save_screenshot('test_opening_authorization_page_3.png')
    time.sleep(3)

    assert selenium.find_element(By.ID, 't-btn-tab-login').text == 'Почта', print('Тест провален')

# TEST_017
# проверка, что таб выбора авторизации по почте и паролю, "Логин"
def test_opening_authorization_page_4(testing):
    selenium = testing
    # открытие сайта
    selenium.get('https://b2c.passport.rt.ru')

    element = WebDriverWait(selenium, 10).until(EC.visibility_of_element_located((By.ID, 'kc-login')))

    # таб "Почта"
    selenium.find_element(By.ID, 't-btn-tab-mail').click()
    # снимок экрана с результатом теста
    selenium.save_screenshot('test_opening_authorization_page_4.png')
    time.sleep(3)

    assert selenium.find_element(By.ID, 't-btn-tab-mail').text == 'Логин', print('Тест провален')

# TEST_018
# проверка, что таб выбора авторизации по лицевому счету и паролю, "Лицевой счёт"
def test_opening_authorization_page_5(testing):
    selenium = testing
    # открытие сайта
    selenium.get('https://b2c.passport.rt.ru')

    element = WebDriverWait(selenium, 10).until(EC.visibility_of_element_located((By.ID, 'kc-login')))

    # таб "Лицевой счёт"
    selenium.find_element(By.ID, 't-btn-tab-ls').click()
    # снимок экрана с результатом теста
    selenium.save_screenshot('test_opening_authorization_page_5.png')
    time.sleep(3)

    assert selenium.find_element(By.ID, 't-btn-tab-ls').text == 'Лицевой счёт', print('Тест провален')

# TEST_019
# проверка, что пользователь может войти в аккаунт с помощью корректно введённых данных (мобильный телефон и пароль) \
# (заранее должен быть создан аккаунт)
def test_authorization(testing):
    selenium = testing
    # открытие сайта
    selenium.get('https://b2c.passport.rt.ru')

    element = WebDriverWait(selenium, 10).until(EC.visibility_of_element_located((By.ID, 'kc-login')))

    # нажать на "Телефон"
    selenium.find_element(By.ID, 't-btn-tab-phone').click()
    # ввод корректного номера телефона
    selenium.find_element(By.ID, 'username').send_keys(correct_phone)
    # ввод корректного пароля
    selenium.find_element(By.ID, 'password').send_keys(correct_password)
    # нажимаем на кнопку "Войти"
    selenium.find_element(By.XPATH, '//button[@type="submit"]').click()
    time.sleep(5)

    # снимок экрана с результатом теста
    selenium.save_screenshot('test_authorization.png')

    assert selenium.find_element(By.TAG_NAME, 'h3').text == 'Учетные данные', print('Тест провален')

# TEST_020
# проверка, что пользователь может войти в аккаунт с помощью корректно введённых данных (электронная почта и пароль) \
# (заранее должен быть создан аккаунт)
def test_authorization_2(testing):
    selenium = testing
    # открытие сайта
    selenium.get('https://b2c.passport.rt.ru')

    element = WebDriverWait(selenium, 10).until(EC.visibility_of_element_located((By.ID, 'kc-login')))

    # нажать на "Почта"
    selenium.find_element(By.ID, 't-btn-tab-mail').click()
    # ввод корректной электронной почты
    selenium.find_element(By.ID, 'username').send_keys(correct_email)
    # ввод корректного пароля
    selenium.find_element(By.ID, 'password').send_keys(correct_password)
    # нажимаем на кнопку "Войти"
    selenium.find_element(By.XPATH, '//button[@type="submit"]').click()
    time.sleep(5)

    # снимок экрана с результатом теста
    selenium.save_screenshot('test_authorization_2.png')

    assert selenium.find_element(By.TAG_NAME, 'h3').text == 'Учетные данные', print('Тест провален')

# TEST_021
# проверка, что пользователь может войти в аккаунт с помощью корректно введённых данных (логин и пароль) \
# (заранее должен быть создан аккаунт)
def test_authorization_3(testing):
    selenium = testing
    # открытие сайта
    selenium.get('https://b2c.passport.rt.ru')

    element = WebDriverWait(selenium, 10).until(EC.visibility_of_element_located((By.ID, 'kc-login')))

    # нажать на "Логин"
    selenium.find_element(By.ID, 't-btn-tab-login').click()
    # ввод корректного логина
    selenium.find_element(By.ID, 'username').send_keys(correct_name)
    # ввод корректного пароля
    selenium.find_element(By.ID, 'password').send_keys(correct_password)
    # нажимаем на кнопку "Войти"
    selenium.find_element(By.XPATH, '//button[@type="submit"]').click()
    time.sleep(5)

    # снимок экрана с результатом теста
    selenium.save_screenshot('test_authorization_3.png')

    assert selenium.find_element(By.TAG_NAME, 'h3').text == 'Учетные данные', print('Тест провален')

# TEST_022
# проверка, что введён верный номер телефона, но неверный пароль
def test_authorization_4(testing):
    selenium = testing
    # открытие сайта
    selenium.get('https://b2c.passport.rt.ru')

    element = WebDriverWait(selenium, 10).until(EC.visibility_of_element_located((By.ID, 'kc-login')))

    # нажать на "Телефон"
    selenium.find_element(By.ID, 't-btn-tab-phone').click()
    # ввод корректного номера телефона
    selenium.find_element(By.ID, 'username').send_keys(correct_phone)
    # ввод некорректного пароля
    selenium.find_element(By.ID, 'password').send_keys(incorrect_password)
    # нажимаем на кнопку "Войти"
    selenium.find_element(By.XPATH, '//button[@type="submit"]').click()
    time.sleep(5)

    # снимок экрана с результатом теста
    selenium.save_screenshot('test_authorization_4.png')

    assert selenium.find_element(By.ID, 'form-error-message').text == 'Неверный логин или пароль', \
        print('Тест провален')

# TEST_023
# проверка, что введена верная электронная почта, но неверный пароль
def test_authorization_5(testing):
    selenium = testing
    # открытие сайта
    selenium.get('https://b2c.passport.rt.ru')

    element = WebDriverWait(selenium, 10).until(EC.visibility_of_element_located((By.ID, 'kc-login')))

    # нажать на "Почта"
    selenium.find_element(By.ID, 't-btn-tab-mail').click()
    # ввод корректной электронной почты
    selenium.find_element(By.ID, 'username').send_keys(correct_email)
    # ввод некорректного пароля
    selenium.find_element(By.ID, 'password').send_keys(incorrect_password)
    # нажимаем на кнопку "Войти"
    selenium.find_element(By.XPATH, '//button[@type="submit"]').click()
    time.sleep(5)

    # снимок экрана с результатом теста
    selenium.save_screenshot('test_authorization_5.png')

    assert selenium.find_element(By.ID, 'form-error-message').text == 'Неверный логин или пароль', \
        print('Тест провален')

# TEST_024
# проверка, что пользователь может перейти на страницу "Восстановление пароля"
def test_password_recovery(testing):
    selenium = testing
    # открытие сайта
    selenium.get('https://b2c.passport.rt.ru')

    element = WebDriverWait(selenium, 10).until(EC.visibility_of_element_located((By.ID, 'kc-login')))

    # нажимаем на кнопку "Забыл пароль"
    selenium.find_element(By.ID, 'forgot_password').click()

    # снимок экрана с результатом теста
    selenium.save_screenshot('test_password_recovery.png')

    assert selenium.find_element(By.TAG_NAME, 'h1').text == 'Восстановление пароля', print('Тест провален')
    assert selenium.find_element(By.TAG_NAME, 'p').text == 'Введите данные и нажмите «Продолжить»', \
        print('Тест провален')
