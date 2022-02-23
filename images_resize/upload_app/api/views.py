from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
from django.core.files.storage import default_storage
from rest_framework import status
from upload_app.models import Images
from upload_app.api.serializers import ImageSerializer
from upload_app.api.resize_image import resize_image

@csrf_exempt
def saveFileView(request):
    if request.method == 'POST':
        files = request.FILES.getlist('files')
        storage = []
        if files:
            for file in files:
                file, image_name, image_orientation = resize_image(file)
                file_name = default_storage.save(image_name, file)
                storage.append({"name": file_name, "orientation": image_orientation})
        return JsonResponse({"message": storage})
    else:
        return JsonResponse({"message": "Metodo no permitido"},  status=status.HTTP_400_BAD_REQUEST)