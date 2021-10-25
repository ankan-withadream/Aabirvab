
from django.urls.conf import path
from django.urls import path
from abirvab import views


urlpatterns = [
    path("", views.index),
    path("view/<str:contentType>", views.view_content,  name="viewContent"),
    path("addcontent", views.add_content)
]
