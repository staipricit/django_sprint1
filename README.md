# Блогикум часть 1

## Это часть работы над проектом Блогикум:

- Блогикум часть 1 ← _этот репозиторий_

## Технологии:

- Python 3.9.13
- Django 4.2.16

## Установка (Windows):

1. Клонирование репозитория

```
git clone https://github.com/staipricit/django_sprint1.git
```

2. Переход в директорию django_sprint1

```
cd django_sprint1
```

3. Создание виртуального окружения

```
python -m venv venv
```

4. Активация виртуального окружения

```
source venv/Scripts/activate
```

5. Обновите pip

```
python -m pip install --upgrade pip
```

6. Установка зависимостей

```
pip install -r requirements.txt
```

7. Переход в директорию blogicum

```
cd blogicum
```

8. Настройте переменные окружения

Создайте файл `.env` в корневой директории проекта и добавьте в него следующие переменные:

```
DJANGO_SECRET_KEY=your_secret_key_here
DJANGO_DEBUG=True
DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1
```

Замените `your_secret_key_here` на уникальный ключ безопасности. Для продакшена установите `DJANGO_DEBUG=False` и укажите нужные хосты в `DJANGO_ALLOWED_HOSTS`.

9. Применение миграций

```
python manage.py migrate
```

10. Запуск проекта, введите команду

```
python manage.py runserver
```

11. Отмена

```
Ctrl + C
```

12. Деактивация виртуального окружения

```
deactivate
```
