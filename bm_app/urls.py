from django.urls import path
from bm_app.views import home_page_bm, capitulos, graficos # Só selecionar o interpretador certo que dá


urlpatterns = [
    path('', home_page_bm),
    path('capitulos/', capitulos),
    path('graficos/', graficos)
]