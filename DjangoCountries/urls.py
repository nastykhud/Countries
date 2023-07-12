from django.urls import path
from MainApp import views

urlpatterns = [
    path('', views.home),
    path('countries-list/', views.countries_list),
    path('countries-list-alphabet/<str:alpha>', views.countries_list_alphabet),
    path('country/<str:country>', views.country),
    path('languages-list/', views.lang_list),
    path('languages/<str:lang>', views.lang),
]
