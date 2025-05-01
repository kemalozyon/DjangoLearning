from django.urls import path
from . import views

urlpatterns = [
    path("", views.home),
    path("<int:month>", views.index_num),
    path("<str:month>", views.index, name="num")
]