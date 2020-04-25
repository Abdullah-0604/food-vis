from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("record/", views.record, name="record"),
    path("province/", views.province, name="province"),
    path("visualization/", views.visualization, name="visualization"),
    path("feedback/", views.feedback, name="feedback"),

]