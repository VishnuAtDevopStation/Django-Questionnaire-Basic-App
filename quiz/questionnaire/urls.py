from django.conf.urls import url
from . import views

app_name = "questionnaire"

urlpatterns = [
url(r'^$', views.home_page, name = 'home_page'),
url(r'^quiz/', views.list_view, name='list_view'),
]