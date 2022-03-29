from Users.models import profile
from networks.models import Network
from posts.models import Post

news=[]
def newsfeed(request):
    s=Network.objects.get(user=request.user.pk)
    for i in profile.objects.all():
        for j in s.connection_set.all():
            if i.user == j.profiles.user:
                news.append(i)


