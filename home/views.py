from django.shortcuts import render, redirect
from Users.models import CustomUser, profile, profession, Graduate_school, school, college, social_link
from chat.models import ChatRoom
from networks.models import Network
from posts.models import Post


def Home(request):

    if request.user.is_authenticated:
        rooms=[]
        room=ChatRoom.objects.all()
        object=profile.objects.get(user=request.user)
        profession.objects.get_or_create(profile_id=object.id)
        job=profession.objects.get(profile__user=object.user)
        Graduate_school.objects.get_or_create(profile_id=object.id)
        gs=Graduate_school.objects.get(profile__user=object.user)
        school.objects.get_or_create(profile_id=object.id)
        s=school.objects.get(profile__user=object.user)
        college.objects.get_or_create(profile_id=object.id)
        cl=college.objects.get(profile__user=object.user)
        social_link.objects.get_or_create(user=object.user)
        link=social_link.objects.get(user=object.user)
        for j in room:
            for i in j.user.all():
                if i.username==request.user.username:
                    rooms.append(j)
        print(rooms)

        friends=[]
        news = [request.user.id]
        user = request.user


        s = Network.objects.get(user=request.user.pk)
        s1 = CustomUser.objects.all()
        for k in s.connection_set.all():
            if k.connected:
                #k.profiles.user
                friends.append(k.profiles.user)
        for i in s1:
            for j in s.connection_set.all():
                if i == j.profiles.user:
                    news.append(i.id)


        newsfeed = Post.objects.filter(user__id__in=news).order_by('-updated_at')
        context = {
            'user': user,
            'newsfeed': newsfeed,
            'friends':friends,
            'room':room,
            'rooms':rooms,
            'link':link,
            'object':object,
            'gs':gs,
            'cl':cl,
            'job':job,
            's':s

        }
        if 'search' in request.POST:
            #search=request.POST['s']
            search_profile=profile.objects.filter(user__username__icontains=request.POST['s'])|profile.objects.filter(user__first_name__icontains=request.POST['s'])|profile.objects.filter(user__last_name__icontains=request.POST['s'])
            search_post=Post.objects.filter(status__iregex=request.POST['s'],)
            print(search_post)
            context={
                'search_profile':search_profile,
                'search_post':search_post
            }
            return render(request,'search.html',context)
        return render(request, 'home.html', context)
    else:
        return redirect('/users/login/')


def friends(request, pk):
    l = []
    l1 = []
    l3 = []
    requests = Network.objects.get(user=pk)

    users = profile.objects.all()
    connection = requests.connection_set.all()
    for i in connection:

        if i.connected:
            for j in i.profiles.user.network.connection_set.all():
                if j.profiles.user != request.user:
                    l3.append(j.profiles)

    for i in connection:
        l.append(i.profiles)
        l1.append(i.network)

    context = {
        'requests': requests,
        'users': users,
        'connection': connection,
        'l': l,
        'l3': l3
    }
    if request.user.is_authenticated:

        return render(request, 'friends.html', context)
    else:
        return redirect('/users/login/')

def SearchView(request):
    if 'search' in request.POST:
        search=request.POST['s']
        return render(request,'search.html')
    else:
        return redirect('/')

