# QAP-28_final_project

Итоговый проект по автоматизации тестирования. Объект тестирования: https://b2c.passport.rt.ru/

Тест-кейсы и описания багов расположены тут: 

Задание:

Протестировать требования;  
Разработать тест-кейсы (не менее 15);  
Провести автоматизированное тестирование продукта (не менее 15 автотестов);  
Оформить описание обнаруженных багов.  
  
test_registration_website.py - автотесты страницы регистрации

test_authorization_website.py - автотесты страницы авторизации

Описание тестовых сценариев:  
TEST_001 проверка, что пользователь может перейти на страницу регистрации  
TEST_002 проверка, что пользователь может открыть чат поддержки, перейдя на страницу регистрации  
TEST_003 проверка, что на странице регистрации есть продуктовый слоган  
TEST_004 проверка регистрации на сайте с корректными данными  
TEST_005 проверка регистрации пользователя с некорректным вводом всех полей (только цифры)  
TEST_006 проверка регистрации пользователя с некорректным вводом некоторых полей  
TEST_007 проверка регистрации пользователя с вводом неверного кода доступа  
TEST_008 проверка регистрации пользователя с некорректным вводом всех полей (только спецсимволы)  
TEST_009 проверка регистрации пользователя с некорректным вводом всех полей (русская и английская раскладка)  
TEST_010 проверка, что если пользователь ввёл в поле "Подтверждение пароля" пароль, отличный от пароля "Новый пароль" то под полем "Подтверждение" отображается "Пароли не совпадают"  
TEST_011 проверка регистрации пользователя, который уже зарегистрирован  
TEST_012 проверка, что пользователь может перейти на страницу авторизации  
TEST_013 проверка, что пользователь может открыть чат поддержки на странице авторизации  
TEST_014 проверка, что на странице авторизации есть продуктовый слоган  
TEST_015 проверка, что таб выбора авторизации по номеру, "Номер"  
TEST_016 проверка, что таб выбора авторизации по логину и паролю, "Почта"  
TEST_017 проверка, что таб выбора авторизации по почте и паролю, "Логин"  
TEST_018 проверка, что таб выбора авторизации по лицевому счету и паролю, "Лицевой счёт"  
TEST_019 проверка, что пользователь может войти в аккаунт с помощью корректно введённых данных (мобильный телефон и пароль) \ (заранее должен быть создан аккаунт)  
TEST_020 проверка, что пользователь может войти в аккаунт с помощью корректно введённых данных (электронная почта и пароль) \ (заранее должен быть создан аккаунт)  
TEST_021 проверка, что пользователь может войти в аккаунт с помощью корректно введённых данных (логин и пароль) \ (заранее должен быть создан аккаунт)  
TEST_022 проверка, что введён верный номер телефона, но неверный пароль  
TEST_023 проверка, что введена верная электронная почта, но неверный пароль  
TEST_024 проверка, что пользователь может перейти на страницу "Восстановление пароля"  
  
  
python -m pytest -v --driver Chrome --driver-path chromedriver.exe test_registration_website.py - команда для запуска тестов страницы регистрации

python -m pytest -v --driver Chrome --driver-path chromedriver.exe test_authorization_website.py - команда для запуска тестов страницы авторизации

Тесты написаны с помощью WebDriver. Всего в проекте 24 кейса. Каждый тест сохраняет скриншот в папку проекта. Для запуска тестов требуется предварительная установка библиотек pytest selenium, а также скачивание драйвера, совместимого с браузером.
