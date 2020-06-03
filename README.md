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

Написать тест создания товара с добавлением картинок
Цель: Научиться загружать файлы на сервер
(1) Простой уровень - обязательный
1.1. Перейти на адрес https://developer.mozilla.org/ru/docs/Web/HTML/Element/Input/file
1.2. Найти элемент "Выберите файл"
1.3. Загрузить файл на сервер

(2*) Сложный уровень - необязательный
2.1. Открыть опенкарт - админку - страницу редактирования товара
2.2. Добавить фото (с помощью javascript)

### Решение

```bash
pytest -v --browser=chrome tests/test_upload_file.py
```