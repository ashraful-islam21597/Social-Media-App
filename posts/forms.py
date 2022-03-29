from django  import forms
from django.forms import ModelForm, TextInput

from posts.models import Post, Comment, Reply


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('comment','picture',)
        widgets = {
            'comment': TextInput(attrs={
                'class': "comment_textarea form-control  col-lg-10 ",
                'style': '',
                'placeholder': 'Write comment',
                'autocomplete':'off',
            }),

        }

class ReplyForm(ModelForm):
    class Meta:
        model = Reply
        fields = ('reply','picture',)
        widgets = {
            'reply': TextInput(attrs={
                'class': "comment_textarea form-control col-lg-10 ",
                'style': '',
                'placeholder': 'write reply',
                'autocomplete':'off',
            }),

        }