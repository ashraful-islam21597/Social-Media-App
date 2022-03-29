from django.urls import path

from networks.views import addfriend, accept_request

app_name='networks'
urlpatterns=[
    path('addfriend/<int:pk>',addfriend,name='addfriend'),
    path('accept/<int:pk>',accept_request,name='accept_request')
]