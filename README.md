# Проект магазин


## Описание:
Проект магазин это домашнее задание студента: работа над ядром для интернет-магазина


## Установка:
1. Клонируйте репозиторий 
``` git clone nttps:https://github.com/elenapantsurkina/Shop```


## Зависимости
- python 3.12
- requests 2.32.3


## Установка зависимостей
```pip install -r requirements.txt```


## Конфигурация
Перед запуском проекта убедитесь, что все зависимости установлены и выполнены необходимые конфигурационные шаги


## Использование:
Точка запуска программы является модулем main.py— просто запустите его


## Функционал:
обновлен модуль Product (сделали атрибут price приватным, реализован метод __str__)
обновлен модуль Category ( добавлен метод add product, 
геттер выводит список товаров в виде строк в заданном формате,
сделали категорию products приватной,реализован метод __str__,
добавлен метод total считает количество продуктов в категориях)


## Тестирование:
Код в модульных пакетах src/с покрытыми тестами Для запуска тестов воспользуйтесь командой pytest
Для проверки покрытий тестами воспользуйтесь командой pytest --cov

## Документация:
отсутствует


## Лицензия 
Этот проект лицензирован под лицензией MIT. 