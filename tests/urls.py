from django.urls import re_path

from sudo import views


urlpatterns = [
    re_path(r"^sudo/", views.sudo, name="sudo"),
]
