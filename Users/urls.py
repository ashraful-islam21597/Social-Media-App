from django.urls import path

from Users.views import SignUpView, userprofile, Upload_profile_photo, Upload_cover_photo, EditProffession, \
    Editgraduateschool, Editcollege, Editschool, EditProfile, Editlink, Editaddress

urlpatterns=[
    path('signup/', SignUpView.as_view(), name='signup'),
    path('profile/<int:pk>/', userprofile.as_view(), name='profile'),
    path('upload/profile-photo/<int:pk>/',Upload_profile_photo,name='profile-photo'),
    path('upload/cover-photo/<int:pk>/',Upload_cover_photo,name='cover-photo'),
    path('edit_proffession/<int:pk>/',EditProffession.as_view(),name='edit_proffession'),
    path('edit_graduate_school/<int:pk>/',Editgraduateschool.as_view(),name='edit_graduate_schhol'),
    path('edit_coolege/<int:pk>/',Editcollege.as_view(),name='edit_college'),
    path('edit_school/<int:pk>/',Editschool.as_view(),name='edit_school'),
    path('edit_profile/<int:pk>/',EditProfile.as_view(),name='edit_profile'),
    path('edit_link/<int:pk>/',Editlink.as_view(),name='edit_link'),
    path('edit_address/<int:pk>/',Editaddress.as_view(),name='edit_address'),
    # path('create/',createprofession,name='create_proffession')
]