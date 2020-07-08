from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("record/", views.record, name="record"),
    path("province1/", views.province1, name="province1"),
    path("province2/", views.province2, name="province2"),
    path("province3/", views.province3, name="province3"),
    path("province4/", views.province4, name="province4"),
    path("province5/", views.province5, name="province5"),
    path("visualization/", views.visualization, name="visualization"),
    path("feedback/", views.feedback, name="feedback"),

]