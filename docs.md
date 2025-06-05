🧾 Техническое задание: Backend (Django) для выдачи 3D сцены
🎯 Цель
Поднять минимальный backend на Django, который:

Отдаёт JSON-сцену по эндпоинту /api/project/1/scene/

Раздаёт .glb модели через static/

Не использует базу данных (данные захардкожены)

Работает с двумя моделями: boiler.glb и burner.glb

🛠️ Стек
Python 3.10+

Django 5.0+

Django REST Framework

Статические файлы в static/3d-models/

📁 Структура проекта
cpp
Копировать
Редактировать
project/
├── backend/
│   ├── views.py
│   ├── urls.py
│   └── settings.py
├── static/
│   └── 3d-models/
│       ├── boiler.glb
│       └── burner.glb
└── manage.py
🔗 Эндпоинт
GET /api/project/1/scene/
Возвращает описание 3D-сцены в JSON:

json
Копировать
Редактировать
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
🧩 Код (views.py)
python
Копировать
Редактировать
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def get_scene(request, project_id):
    return Response({
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
    })
🔌 urls.py
python
Копировать
Редактировать
from django.urls import path
from .views import get_scene

urlpatterns = [
    path("api/project/<int:project_id>/scene/", get_scene),
]
⚙️ settings.py
python
Копировать
Редактировать
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
✅ Проверка
После запуска сервера:

http://localhost:8000/api/project/1/scene/ — JSON сцена

http://localhost:8000/static/3d-models/boiler.glb — доступ к модели

