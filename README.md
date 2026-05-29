#  Financial Tracker

> Система учета личных финансов на Django

Веб-приложение для персонального учета доходов и расходов с категоризацией операций, аналитикой и визуализацией статистики.

---

## Возможности

- **Учет операций** — добавление, редактирование и удаление расходов и доходов
- **Категоризация** — пользовательские категории для расходов и доходов с защитой от дублирования
- **Автоматическая инициализация** — при регистрации создается набор типовых категорий (Дом, Продукты, Транспорт, Зарплата и др.)
- **Статистика** — статистика по периодам (день, месяц, произвольный интервал) с фильтрацией по категориям
- **Визуализация** — диаграммы распределения доходов и расходов по категориям (Chart.js)
- **Баланс** — расчет текущего баланса за выбранный период
- **Авторизация** — регистрация, вход/выход пользователей с разделением данных по владельцам

---

## Технологии

| Компонент    | Технология                 |
|--------------|----------------------------|
| Backend      | Python 3.14, Django 6.0.5  |
| База данных  | PostgreSQL 18.3 / SQLite 3 |
| Frontend     | HTML5, CSS3, Chart.js 4.4  |
| Тестирование | pytest, pytest-django      |

---

## 🚀 Быстрый старт

### 1. Клонирование репозитория

```bash
git clone https://github.com/tkchh/financial-tracker.git
cd financial-tracker
```

### 2. Установка зависимостей

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Настройка окружения

Приложение поддерживает два режима работы с БД:

**SQLite (для разработки):**
```bash
export USE_SQLITE=1
# Windows: set USE_SQLITE=1
```
Файл БД - db.sqlite3

**PostgreSQL:**
```bash
export DB_ENGINE=django.db.backends.postgresql
export DB_NAME=finance_db
export DB_USER=postgres
export DB_PASSWORD=postgres
export DB_HOST=localhost
export DB_PORT=5432
```

> По умолчанию используется PostgreSQL. Для SQLite установите `USE_SQLITE=1`.

### 4. Миграции и запуск

#### Воспроизвести SQL-схему без Django-миграций:
```bash
# SQLite
sqlite3 new_db.sqlite3 < db_schema.sql 

# PostgreSQL
psql -h localhost -U postgres -d finance_db < db_schema.sql
```

#### С Django-миграциями:
```bash
python manage.py migrate
pytohn manage.py createsuperuser #создать super-пользователя
python manage.py runserver
```

Приложение будет доступно по адресу: `http://127.0.0.1:8000/`

---

## Тестирование

```bash
pytest
```

Покрытие тестами включает:
- Модели и ограничения целостности
- CRUD-операции для транзакций и категорий
- Сервисный слой (баланс, периоды, категории по умолчанию)
- Селекторы статистики
- Авторизацию и разграничение доступа

---

## 📁 Структура проекта

```
financial-tracker/
├── config/                 # Конфигурация Django
│   ├── settings.py         # Настройки (поддержка env-переменных)
│   ├── urls.py             # Корневой роутинг
│   └── wsgi.py / asgi.py   
├── tracker/                # Основное приложение
│   ├── models/             # Модели: Expense, Income, категории
│   ├── views/              # CBV: транзакции, категории, статистика, авторизация
│   ├── forms/              # Формы с валидацией
│   ├── services/           # Бизнес-логика (баланс, периоды, дефолтные категории)
│   ├── selectors/          # Слой чтения данных (статистика)
│   ├── tests/              # pytest-тесты
│   └── urls.py             # Url-паттерны приложения
├── templates/              # HTML-шаблоны (Django Templates)
├── static/css/             # CSS-стили
├── requirements.txt        # Зависимости
└── manage.py
└── db_schema.sql           # Логическая резервная копия схемы базы данных
```


