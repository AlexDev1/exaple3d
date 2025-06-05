# 3D Scene Backend API

Django backend для выдачи 3D сцены с .glb моделями.

## Структура проекта

```
project/
├── backend/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── views.py
│   └── wsgi.py
├── static/
│   └── 3d-models/
│       ├── boiler.glb
│       └── burner.glb
├── manage.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── README.md
```

## Быстрый запуск с Docker

### 1. Сборка и запуск
```bash
docker-compose up --build
```

### 2. Проверка API
- JSON сцена: http://localhost:8000/api/project/1/scene/
- 3D модель котла: http://localhost:8000/static/3d-models/boiler.glb
- 3D модель горелки: http://localhost:8000/static/3d-models/burner.glb

## Локальный запуск (без Docker)

### 1. Установка зависимостей
```bash
pip install -r requirements.txt
```

### 2. Запуск сервера
```bash
python manage.py runserver
```

## API Эндпоинты

### GET /api/project/{project_id}/scene/
Возвращает JSON описание 3D сцены:

```json
{
  "objects": [
    {
      "model": "/static/3d-models/boiler.glb",
      "position": [0, 0, 0],
      "rotation": [0, 0, 0],
      "meta": { "title": "Котёл 400 кВт" },
      "connections": ["burner"]
    },
    {
      "model": "/static/3d-models/burner.glb",
      "position": [1.5, 0, 0],
      "rotation": [0, 0, 0],
      "connects_to": "boiler"
    }
  ]
}
```

## Особенности

- ✅ Django 5.0+ с Django REST Framework
- ✅ Без базы данных (данные захардкожены)
- ✅ Статические файлы .glb моделей
- ✅ Docker контейнеризация
- ✅ Готов к работе из коробки 