from django.urls import path

from chat.views import room

urlpatterns=[
    #path('',index,name='index'),
    path('<int:pk>/',room.as_view(),name='chat')
]