# Sprint_5

UI-автотесты для сервиса Stellar Burgers.

## Stack

- Python
- Selenium
- pytest
- Google Chrome

## What is covered

- регистрация пользователя;
- ошибка для короткого пароля;
- вход с главной страницы;
- вход через «Личный кабинет»;
- вход через форму регистрации;
- вход через форму восстановления пароля;
- переход в личный кабинет;
- возврат в конструктор по ссылке «Конструктор»;
- возврат в конструктор по логотипу Stellar Burgers;
- выход из аккаунта;
- переключение вкладок «Булки», «Соусы» и «Начинки».

## Project structure

```text
Sprint_5/
├── tests/
│   ├── test_registration.py
│   ├── test_login.py
│   ├── test_personal_account.py
│   └── test_constructor.py
├── locators.py
├── urls.py
├── data.py
├── helpers.py
├── actions.py
├── conftest.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Install dependencies

```bash
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
```

## Run tests

```bash
pytest -v
```

## Project notes

- временные учетные данные создаются во время запуска и не хранятся в репозитории;
- все фикстуры находятся в `conftest.py`;
- все Selenium-локаторы вынесены в `locators.py`.

## Runtime note

В текущем OpenClaw runtime тесты запускались через:

```bash
LD_LIBRARY_PATH=/tmp/selenium_deps/extract/usr/lib/x86_64-linux-gnu .venv/bin/python -m pytest -v
```

Для ревью в обычном локальном окружении это не должно быть основным способом запуска, если Chrome и системные зависимости установлены корректно.
