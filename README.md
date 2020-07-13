# PythonQAOtusSelenium

Упражнения для курса Python QA Engineer. Для удобства, упражнения по теме Selenium вынесены в отдельный репозиторий.

Основной репозиторий с домашними заданиями https://github.com/a13xk/PythonQAOTUS.


## 2 месяц, модуль 9 - Поиск и действия с элементами

### Домашнее задание
Поиск элементов на странице.
Цель: Нучиться использовать методы поиска элементов в selenium.
1. Написать тесты проверяющие наличие элементов на разных страницах приложения opencart.
2. Реализовать минимум пять тестов (одни тест = одна страница приложения)
3. Какие элементы проверять определить самостоятельно, но не меньше 5 для каждой страницы.

Покрыть нужно:

* Главную `/`
* Каталог `/index.php?route=product/category&path=20`
* Карточку товара `/index.php?route=product/product&path=57&product_id=49`
* Страницу логина `/index.php?route=account/login`
* Страницу логина в админку `/admin/`

### Решение

1. Главная страница:
    ```bash
    pytest -v tests/test_main_page.py --browser=chrome
    ```
2. Страница каталога:
    ```bash
    pytest -v tests/test_catalog_page.py --browser=chrome --opencart_url=/index.php?route=product/category\&path=20
    ```
3. Страница товара:
    ```bash
    pytest -v tests/test_product_page.py --browser=chrome --opencart_url=/index.php?route=product/product\&path=57\&product_id=49
    ```
4. Страница логина:
    ```bash
    pytest -v tests/test_login_page.py --browser=chrome --opencart_url=/index.php?route=account/login
    ```
5. Страница логина в админку:
    ```bash
    pytest -v tests/test_admin_page.py --browser=chrome --opencart_url=https://localhost/admin/
    ```

## 2 месяц, модуль 10 - Ожидания элементов

### Домашнее задание
Ожидание элементов.
Цель: Научиться использовать ожидания и обработку исключений в тестах
1. К существующим тестам добавить явные ожидания элементов.
2. Добавить 2 тестовых сценария на раздел администратора

    2.1. Добавить проверку логина и разлогина раздела.

    2.2. Добавить проверку перехода к разделу с товарами, что появляется таблица с товарами.

Критерии оценки: Приложить скриншот того, что тесты проходят. 

### Решение

2.1. Проверка логина и разлогина:
```bash
pytest -v tests/test_admin_page.py::TestAdminPage::test_login_logout --browser=chrome --opencart_url=https://localhost/admin/
```
2.2. Проверка перехода к разделу с товарами:
```bash
pytest -v tests/test_admin_page.py::TestAdminPage::test_browse_to_catalog_products_table --browser=chrome --opencart_url=https://localhost/admin/
```

## 2 месяц, модуль 11 - JavaScript in Selenium

### Домашнее задание

Работа с элементами.
Цель: Попрактиковаться в работе со свойствами элементов.
Для страницы Products реализовать тесты, которые проверяют:
1) Функциональность добавления.
2) Функциональность изменения.
3) Функциональность удаления продукта.
Дополнительно: Реализовать предусловие, которое гарантирует наличие продукта в списке для тестов удаления и редактирования. 

### Решение

1. Добавление продукта:
    ```bash
    pytest -v tests/test_admin_page.py::TestAdminPage::test_add_new_product
    ```
2. Удаление продукта:
    ```bash
    pytest -v tests/test_admin_page.py::TestAdminPage::test_delete_product
    ```
3. Изменение продукта:
    ```bash
    pytest -v tests/test_admin_page.py::TestAdminPage::test_edit_product
    ```

## 2 месяц, модуль 12 - Архитектура веб-тестов (Page Object, Page Element)

### Домашнее задание
PageObject.
Цель: Научиться реализовывать паттерн PageObject на практике.
В имеющемся проекте автоматизации приложения OpenCart на данный момент имеются описания селекторов страниц и небольшой пул автотестов.
Необходимо перевести код на паттерн PageObject. Добавить 5 новых тестов написанных в этой парадигме.
Выбор функциональности или сценариев остается на ваше усмотрение.
Критерии оценки: Тесты проекта выполнены в парадигме PageObject.

### Решение

* Имеющиеся тесты переведены на паттерн Page Object:
    ```bash
    pytest -v --browser=chrome tests/test_admin_login_page.py::TestAdminLoginPage
    pytest -v --browser=chrome tests/test_administration_page.py::TestAdministrationPage
    pytest -v --browser=chrome tests/test_catalog_page.py::TestCatalogPage
    pytest -v --browser=chrome tests/test_login_page.py::TestLoginPage
    pytest -v --browser=chrome tests/test_main_page.py::TestMainPage
    pytest -v --browser=chrome tests/test_product_page.py::TestProductPage
    ```
* Добавлены 5 новых тестов.

1. Просмотр страницы **Catalog** → **Categories**:
    ```bash
    pytest -v --browser=chrome tests/test_administration_page.py::TestAdministrationPage::test_browse_to_catalog_categories
    ```
2. Просмотр страницы **Catalog** → **Recurring Profiles**:
    ```bash
    pytest -v --browser=chrome tests/test_administration_page.py::TestAdministrationPage::test_browse_to_recurring_profiles
    ```
3. Просмотр страницы **Catalog** → **Filters**:
    ```bash
    pytest -v --browser=chrome tests/test_administration_page.py::TestAdministrationPage::test_browse_to_filters
    ```
4. Просмотр страницы **Catalog** → **Attributes** → **Attributes**:
    ```bash
    pytest -v --browser=chrome tests/test_administration_page.py::TestAdministrationPage::test_browse_to_attributes
    ```
5. Просмотр страницы **Catalog** → **Attributes** → **Attribute Groups**:
    ```bash
    pytest -v --browser=chrome tests/test_administration_page.py::TestAdministrationPage::test_browse_to_attribute_groups
    ```

## 2 месяц, модуль 13 - Работа с окнами

### Домашнее задание

Написать тест создания товара с добавлением картинок.

Цель: Научиться загружать файлы на сервер

1. Простой уровень - обязательный

    1.1. Перейти на адрес https://developer.mozilla.org/ru/docs/Web/HTML/Element/Input/file

    1.2. Найти элемент "Выберите файл"

    1.3. Загрузить файл на сервер

2. Сложный уровень - необязательный

    2.1. Открыть опенкарт - админку - страницу редактирования товара

    2.2. Добавить фото (с помощью javascript)

### Решение

1. Простой уровень - обязательный

```bash
pytest -v --browser=chrome tests/test_upload_file.py
```

## 2 месяц, модуль 14 - Протоколирование и отчетность

### Домашнее задание

Протоколирование

Настроить протоколирование проекта

Критерии оценки:

* 1 балл - за настроенный event_firing_webdriver (в том числе снятие скриншотов при падениях драйвера)
* 1 балл - запись лога в файл
* 1 балл - работа с логом с помощью модуля logging
* 1 балл - снятие логов с браузера
* 1 балл - настройка логирования http запросов через proxy 

### Решение

Логирование в базовом классе:

```bash
pytest -v --browser=chrome --base_class_logging tests/test_catalog_page.py
```

Логирование с помощью подхода Event Firing Webdriver:

```bash
pytest -v --browser=chrome --webdriver_logging tests/test_product_page.py
```

## 2 месяц, модуль 15 - Удаленный запуск (Grid)

### Домашнее задание

Постройте небольшой грид, научитесь использовать облачный грид
1) Установите виртуальную машину, внутри которой работает Windows/Linux, и создайте грид, который состоит из диспетчера, 
работающего на вашей основной машине, и двух узлов -- один тоже на основной машине, а другой внутри виртуальной машины.

Настройте узлы так, чтобы в виртуальной машине был доступен браузер Firefox/Chrome, а на основной машине, наоборот, он был недоступен.

Попробуйте запустить какие-нибудь тесты удалённо на этом гриде, указывая разные браузеры, и убедитесь, что Firefox/Chrome, 
действительно запускается внутри виртуальной машины, а другие браузеры, наоборот, на вашей основной машине.

Можно использовать любую систему виртуализации, но если у вас нет предпочтений -- берите https://www.virtualbox.org/

Готовые образы Windows для разных систем виртуализации можно найти здесь: https://developer.microsoft.com/en-us/microsoft-edge/tools/vms/

2) Запустить несколько тестов в каком-нибудь облачном сервисе на выбор:

https://www.browserstack.com/
https://www.gridlastic.com/
https://saucelabs.com/
https://testingbot.com/

Критерии оценки: 
1) Ссылка на коммит + скриншот консоли грида
2) Ссылка на коммит + скриншот с облачного сервиса

### Решение

#### 1. Запуск тестов в ноде (виртуальной машине)

Предварительно необходимо установить виртуальную машину, установить на ней браузер Chrome и его вебдрайвер, настроить сетевое 
подключение (адаптер 1 - Host-only Adapter, адаптер 2 - Bridged Adapter).

1. На хосте (Kubuntu 20.04) запустить Selenium Server в роли хаба:
```bash
java -jar selenium-server-standalone-3.141.59.jar -role hub
```

2. На виртуальной машине (Windows 10) запустить Selenium Server в роли ноды:
```bash
java -jar .\selenium-server-standalone-3.141.59.jar -role node -hub http://192.168.56.1:4444/grid/register/
```
, где `http://192.168.56.1:4444/grid/register/` - адрес хаба, транслируемый в консоли после его запуска.

3. В хосте выполнить команду запуска тестов: 
```bash
pytest -v --browser=chrome --opencart_url=https://demo.opencart.com/
```

#### 2. Запуск тестов в BrowserStack

Предварительно необходимо создать аккаунт в сервисе https://www.browserstack.com.

```bash
pytest -v \
--browserstack_executor=https://alexanderknyazev2:sDCeYxp5XUhfQKQ8oxfy@hub-cloud.browserstack.com/wd/hub \
--opencart_url=https://demo.opencart.com/
```

## 3 месяц, модуль 19 - Работа с БД

### Домашнее задание

Добавление тестовых данных в бд для автотестов
Цель: Научиться работать с разными БД из Python кода и применять эти знания при написании автотестов.
В рамках ДЗ необходимо сделать:
1. Добавить в тесты создания, редактирования и удаления товара из админки проверку, что сущность удалена, добавлена и изменена в БД.
2. Сделать подготовку тестовых данных для тестов на удаление и редактирование товара через INSERT в БД внутри кода: 
перед тестом небходимо добавить в БД товар, который будет редактироваться или удаляться внутри теста.
Создание коннекта к бд можно сделать в фикстуре к тесту или внутри теста

### Решение

Тесты на добавление, удаление и изменение продукта с проверками в базе данных.

```bash
pytest -v tests/test_administration_page_db.py
```