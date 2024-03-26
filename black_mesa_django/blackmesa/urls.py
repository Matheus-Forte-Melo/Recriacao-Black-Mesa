from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from blackmesa.views import home, capitulos


urlpatterns = [
    path('', home),
    path('capitulos/', capitulos)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)