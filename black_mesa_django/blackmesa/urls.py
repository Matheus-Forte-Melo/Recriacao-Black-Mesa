from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from blackmesa.views import home, enredo


urlpatterns = [
    path('', home),
    path('enredo/', enredo)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)