from django.urls import path

from posts.views import create_status, react_post, CreateComment

urlpatterns = [
    path('status/', create_status.as_view(), name='create_status'),
    path('comment/<int:pk>/', CreateComment, name='create_comment'),
    #path('reply/<int:pk>/', CreateReply.as_view(), name='#demo'),
    path('react/<int:pk>/', react_post, name='react')
]
