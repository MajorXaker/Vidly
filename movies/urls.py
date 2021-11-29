from django.urls import path
from . import views

# movies/
# movies/1/details

app_name = "movies"
#нужно чтобы делать линки вот такого типа "movies:detail" в хтмл разметке

urlpatterns = [
    path('', views.index, name = "index"),
    path('<int:movie_id>', views.detail, name="detail")
]