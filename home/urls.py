from django.urls import path

from home.views import Home, friends, SearchView

urlpatterns=[
    path('',Home,name='home'),
    path('friends/<int:pk>',friends,name='friends'),
    path('search/',SearchView,name='search'),

]