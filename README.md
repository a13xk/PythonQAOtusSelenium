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
