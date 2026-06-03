# Sprint_5

UI-автотесты для сервиса Stellar Burgers.

## Stack

- Python
- Selenium
- pytest
- Google Chrome

## Environment requirements

- Python 3.12 or another installed Python 3 version
- Google Chrome
- Mozilla Firefox

Основной браузер для запуска автотестов на ревью: Google Chrome.

## Install dependencies on Windows

Откройте PowerShell в корне проекта:

```powershell
cd D:\Code_Project\Sprint_5
py -3.12 -m venv .venv
.\.venv\Scripts\python.exe -m pip install --upgrade pip
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

Если Python 3.12 недоступен, используйте установленный Python 3:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install --upgrade pip
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

## Run tests

```powershell
.\.venv\Scripts\python.exe -m pytest -v
```

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

## Project notes

- временные учетные данные создаются во время запуска и не хранятся в репозитории;
- все фикстуры находятся в `conftest.py`;
- все Selenium-локаторы вынесены в `locators.py`.
