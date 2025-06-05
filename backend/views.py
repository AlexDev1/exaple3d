from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def get_scene(request, project_id):
    """
    Возвращает JSON описание 3D сцены для проекта.
    Данные захардкожены согласно ТЗ.
    """
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