from django.urls import include, re_path
from upload_app.api.views import saveFileView
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    re_path(r'savefile', saveFileView) 
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)