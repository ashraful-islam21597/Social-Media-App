from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.forms import ModelForm, DateInput, TextInput, PasswordInput

from Users.models import CustomUser, profession, Graduate_school, college, school


class DateInput(forms.DateInput):
    input_type = 'date'
class usercreationfrom(UserCreationForm):
    class Meta:
        model = CustomUser

        #username = forms.CharField(label='Your name', max_length=100)
        fields= ('username','email','first_name','last_name','DOB',)
        widgets = {
            'DOB': DateInput(),
            'username': TextInput(attrs={
                                'class': "rounded border-primary ",
                                'style': '',
                                'autocomplete':'off',
                            }),
            'first_name': TextInput(attrs={
                'class': "rounded border-primary ",
                'style': '',
                'autocomplete':'off',
            }),
            'last_name': TextInput(attrs={
                'class': "rounded border-primary ",
                'style': '',
                'autocomplete':'off',
            }),


        }







# class usercreationfrom(UserCreationForm):
#     #username = forms.CharField(label='Your name', max_length=100)
#     #email= forms.Emailfield(label='email')
#     #password=forms.CharField(label='password', max_length=100)
#
#     class Meta:
#         model = CustomUser
#
#         #username = forms.CharField(label='Your name', max_length=100)
#         fields= ('username','email','DOB','password')
#         #fields= '__all__'
#         # widgets = {
#         #     'DOB': DateInput(),
#         #
#         # }
#         widgets = {
#             'first_name': TextInput(attrs={
#                 'class': "input100",
#                 'style': '',
#                 'autocomplete':'off',
#             }),
#             'last_name': TextInput(attrs={
#                 'class': "input100",
#                 'style': '',
#                 'autocomplete':'off',
#             }),
#             # 'username': T(attrs={
#             #     'class': "input100",
#             #     'style': '',
#             # }),
#             'email': TextInput(attrs={
#                 'class': "input100",
#                 'style': '',
#                 'placeholder': 'Email',
#                 'autocomplete':'off',
#             }),
#             'password':PasswordInput(attrs={
#                     'class': "input100",
#                     'style': '',
#
#                     'placeholder': 'password',
#
#
#                 }),
#             'confirm_password':PasswordInput(attrs={
#                     'class': "input100",
#                     'style': '',
#
#                     'placeholder': 'confirm password',
#
#
#                 }),
#             'DOB': DateInput(attrs={
#                     'class': "input100",
#                     'style': '',
#                 'placeholder': 'Date Of Birth',
#                     'autocomplete':'off',
#                 }
#             ),
#
#         }


class editprofession(ModelForm):
    class Meta:
        model = profession
        fields= ('profession','company',)
class editgraduateschool(ModelForm):
    class Meta:
        model = Graduate_school
        fields= ('Graduate_school_name','start','end',)
        widgets = {
            'start': DateInput(),
            'end': DateInput(),




        }
class editcollege(ModelForm):
    class Meta:
        model = college
        fields= ('college','start','end',)
        widgets = {
            'start': DateInput(),
            'end': DateInput(),




        }
class editschool(ModelForm):
    class Meta:
        model = school
        fields= ('school','start','end',)
        widgets = {
            'start': DateInput(),
            'end': DateInput(),




        }
class userchangefrom(UserChangeForm):
    class Meta:
        model = CustomUser
        fields= "__all__"
        # widgets = {
        #     'comment': TextInput(attrs={
        #         'class': "comment_textarea form-control  col-lg-10 ",
        #         'style': '',
        #         'placeholder': 'Write comment',
        #         'autocomplete':'off',
        #     }),
        #
        # }

# class usercreationfrom(UserCreationForm):
#     #username = forms.CharField(label='Your name', max_length=100)
#     #email= forms.Emailfield(label='email')
#     #password=forms.CharField(label='password', max_length=100)
#
#     class Meta:
#         model = CustomUser
#
#         #username = forms.CharField(label='Your name', max_length=100)
#         #fields= ('username','email','DOB',)
#         fields= '__all__'
#         # widgets = {
#         #     'DOB': DateInput(),
#         #
#         # }
#         widgets = {
#             # 'first_name': TextInput(attrs={
#             #     'class': "input100",
#             #     'style': '',
#             #     'autocomplete':'off',
#             # }),
#             # 'last_name': TextInput(attrs={
#             #     'class': "input100",
#             #     'style': '',
#             #     'autocomplete':'off',
#             # }),
#             # # 'username': T(attrs={
#             # #     'class': "input100",
#             # #     'style': '',
#             # # }),
#             # 'email': TextInput(attrs={
#             #     'class': "input100",
#             #     'style': '',
#             #
#             #     'autocomplete':'off',
#             # }),
#             # 'password':PasswordInput(
#             #     attrs={
#             #         'class': "input100",
#             #         'style': '',
#             #
#             #         'placeholder': 'password',
#             #
#             #
#             #     }),
#             # 'confirm_password':PasswordInput(
#             #     attrs={
#             #         'class': "input100",
#             #         'style': '',
#             #
#             #         'placeholder': 'confirm password',
#             #
#             #
#             #     }),
#             'DOB': DateInput(
#                 attrs={
#                     'class': "input100",
#                     'style': '',
#
#                     'autocomplete':'off',
#                 }
#             ),
#
#         }