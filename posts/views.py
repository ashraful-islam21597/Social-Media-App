from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView

from notifications.models import Notifications
from posts.forms import CommentForm, ReplyForm
from posts.models import Post, Reaction, Post_reaction, Comment


class create_status(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'create_status.html'
    fields = ('status', 'post_image')
    login_url = 'login'
    success_url = reverse_lazy('home')

    def form_valid(self, form):  # new
        form.instance.user = self.request.user
        return super().form_valid(form)





def react_post(request, pk):
    s = Post_reaction.objects.get(post_id=pk)

    try:
        r = Reaction.objects.get(user=request.user, post_reaction_id=s.id)
        r.post_reaction.total_react = r.post_reaction.total_react - 1
        r.post_reaction.save()
        r.delete()
    except:
        Reaction.objects.create(user=request.user, post_reaction_id=s.id)
        Notifications.objects.create(user=s.post.user,text=str(request.user.username)+' is likeD your image',
                                     notification_TYPE=1)
        print(s.post.status)
    return redirect(request.META['HTTP_REFERER'])


def CreateComment(request, pk):
    obj = Post.objects.get(id=pk)


    for i in obj.post_reaction_set.all():
        i.reaction_set.all().first()
        #print(i.reaction_set.all().first())
    comment = obj.comment_set.all()


    if 'c.id' in request.POST:
        replyform = ReplyForm(request.POST)
        com = Comment.objects.get(id=request.POST['c.id'])
        replies = com.reply_set.all()
        if replyform.is_valid():
            replyform.instance.user = request.user
            replyform.instance.comment_id = request.POST['c.id']
            replyform.save()
            Notifications.objects.create(user=request.user,notification_TYPE=3)
            return HttpResponseRedirect('/write/comment/' + str(pk),
                                        {'obj': obj, 'comment': comment, 'replies': replies})


    if 'comment' in request.POST:
        print('start')
        com=request.POST['comment_text']
        Comment(comment=com,user=request.user,post_id=obj.id).save()
        # commentform = CommentForm(request.POST)
        # print("x")
        # if commentform.is_valid():
        #     print('bnfgsfb')
        #     commentform.instance.user = request.user
        #     commentform.instance.post_id = obj.id
        #     commentform.save()
        #     Notifications.objects.create(user=request.user,notification_TYPE=2)
        #     print("hello")
        return HttpResponseRedirect('/write/comment/' + str(pk),{'obj': obj, 'comment': comment})



    else:
        print("y")
        form1 = CommentForm()
        form2 = ReplyForm()
        context = {
            'form1': form1,
            'form2': form2,
            'obj': obj,
            'comment': comment
        }
        return render(request, 'create_comment.html', context)
