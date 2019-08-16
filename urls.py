from django.urls import path
from . import views

urlpatterns = [
    path("home", views.home, name="home"),
    path("display", views.display, name="starter"),
    path("display2", views.display2, name="display2"),
    path("abc", views.abc, name="abc"),
    path("test", views.test, name="test"),
]