# QAP-28_final_project

Итоговый проект по автоматизации тестирования. Объект тестирования: https://b2c.passport.rt.ru/

Тест-кейсы и описания багов расположены тут: https://docs.google.com/spreadsheets/d/1v-Am2D7eHdIfC_BvSs_2ktkqCgHRT3puk647a5vTu0Q/edit#gid=0

Задание:

Протестировать требования;
Разработать тест-кейсы (не менее 15);
Провести автоматизированное тестирование продукта (не менее 15 автотестов);
Оформить описание обнаруженных багов.

test_registration_website.py - автотесты страницы регистрации

test_authorization_website.py - автотесты страницы авторизации

python -m pytest -v --driver Chrome --driver-path chromedriver.exe test_registration_website.py - команда для запуска тестов страницы регистрации

python -m pytest -v --driver Chrome --driver-path chromedriver.exe test_authorization_website.py - команда для запуска тестов страницы авторизации

Тесты написаны с помощью WebDriver. Всего в проекте 24 кейса. Каждый тест сохраняет скриншот в папку проекта. Для запуска тестов требуется предварительная установка библиотек pytest selenium, а также скачивание драйвера, совместимого с браузером.
