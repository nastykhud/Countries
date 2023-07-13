from django.urls import path
from MainApp import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('countries-list/<int:numstr>', views.countries_list, name = 'count-list'),
    path('countries-list-alphabet/<str:alpha>', views.countries_list_alphabet, name = 'count-list-a'),
    path('country/<str:country>', views.country, name = 'country'),
    path('languages-list/', views.lang_list, name = 'lang-list'),
    path('languages/<str:lang>', views.lang, name = 'lang'),
]
