from django.conf.urls import url
from . import views
from .views import(
    search_results,
    )

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^search/$', search_results, name="search_results,"),
    ]
