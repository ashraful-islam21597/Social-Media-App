import time
from datetime import timezone, date

from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import CreateView, DetailView, UpdateView

from Users.forms import usercreationfrom, editgraduateschool, editcollege, editschool
from Users.models import CustomUser, profile, profession, Graduate_school, school, college, social_link
from networks.models import Network


class SignUpView(CreateView):
    form_class = usercreationfrom
    success_url = reverse_lazy('login')
    model = CustomUser
    template_name = "signup.html"

# def SignUpView(request):
#
#     if request.method == "POST":
#         form= userForm(request.POST)
#         if form.is_valid():
#             form.save()
#             print(request.user.username)
#             user=CustomUser.objects.get(username=form.instance.username)
#             context={
#                 'user':user
#             }
#             return reverse('home:home')
#         else:
#             print("hh")
#             return redirect('signup')
#     else:
#         form= userForm(request.POST or None)
#         return render(request,'signup.html',{'form':form})

    # if request.method == "POST":
    #     username=request.POST.get('username')
    #     email=request.POST.get('email')
    #     password=request.POST.get('password')
    #     confirm_password=request.POST.get('confirm_password')
    #     if password==confirm_password:
    #         user=CustomUser.objects.create(username=username,password=password,email=email)
    #         user.save()
    #         context={
    #             'user':user
    #         }
    #         return render(request, 'home.html',context)
    #     else:
    #         return redirect('signup')
    #
    #
    #
    #
    # else:
    #     return render(request,'signup.html',{'form':form})

# def signin(request):
#     if 'SignUp' in request.POST:
#         First_name = request.POST['name']
#         contact = request.POST['contact']
#         username = request.POST['Username']
#         email = request.POST['email']
#         password = request.POST['password']
#         confirmpassword = request.POST['confirmpassword']
#         birthday = request.POST['dd']
#         if password == confirmpassword:
#             if CustomUser.objects.filter(username=username).exists():
#                 messages.info(request, "usernametaken")
#                 return render(request, "account.html")
#             if CustomUser.objects.filter(password=password).exists():
#                 messages.info(request, "Password not strong")
#                 return render(request, "account.html")
#             if CustomUser.objects.filter(email=email).exists():
#                 messages.info(request, "duplicate email")
#                 return render(request, "account.html")
#
#
#             else:
#
#                 user = CustomUser.objects.create_user(username=username, email=email, password=password)
#                 user.save();
#
#                 u = Profile(name=name, contact=contact,birthday=birthday, username=username, email=email, password=password)
#                 u.save()
#                 k=get_object_or_404(Profile,pk=u.id)
#                 l = usersociallink(user_link_id=k.id)
#                 l.save()
#                 f = friend.objects.create(name=name, contact=contact, username=username, email=email)
#                 f.save()
#                 q = auth.authenticate(username=username, password=password)
#                 q1=get_object_or_404(Profile, username=q.username)
#                 q1.active_status="yes"
#                 q1.save()
#                 auth.login(request, q)
#                 return redirect('/')
#         else:
#             return render(request, 'account.html')
#     if 'Login' in request.POST:
#         username = request.POST['username']
#         password = request.POST['password']
#         q = auth.authenticate(username=username, password=password)
#
#
#         if q is not None:
#             q1 = get_object_or_404(Profile, username=q.username)
#             q1.active_status="yes"
#             q1.save()
#
#             auth.login(request, q)
#
#             return redirect('/')
#         else:
#             messages.info(request, "wrong credential")
#             return render(request, "account.html")
#
#     else:
#         return render(request, 'account.html')
class userprofile(View):
    model = profile
    template_name = 'profile_detail.html'
    def get(self, request, *args, **kwargs):
        friends=[]
        today = date.today()
        d = today.strftime("%B %d, %Y")
        d=str(d)
        print(d)
        object=profile.objects.get(id=self.kwargs['pk'])
        profession.objects.get_or_create(profile_id=object.id)
        job=profession.objects.get(profile__user=object.user)
        Graduate_school.objects.get_or_create(profile_id=object.id)
        gs=Graduate_school.objects.get(profile__user=object.user)
        school.objects.get_or_create(profile_id=object.id)
        s=school.objects.get(profile__user=object.user)
        college.objects.get_or_create(profile_id=object.id)
        cl=college.objects.get(profile__user=object.user)
        net=Network.objects.get(user=request.user)
        s1 = CustomUser.objects.all()
        social_link.objects.get_or_create(user=object.user)
        link=social_link.objects.get(user=object.user)

        obj = Network.objects.get(user=request.user)
        connection=obj.connection_set.all()
        for k in net.connection_set.all():
            if k.connected:
                #k.profiles.user
                friends.append(k.profiles.user)
        #return render(request, self.template_name, {'connection': connection,'object':object, 'obj': obj})

        try:
            c=obj.connection_set.get(network_id=obj.id,profiles_id=object.id,connected=False)
            print("x",c.profiles.user)
            return render(request, self.template_name, {'connection': connection,'friends':friends,'object':object,'c':c, 'obj': obj,'job':job,'gs':gs,'s':s,'cl':cl,'link':link,'d':d})
            #return render(request, self.template_name, {'c': c, 'obj': obj})
            #if c.request_for_connection==False and c.sent_request_for_connection==False:
        except:
            connections=[]
            connection=obj.connection_set.all()
            for j in connection:
                connections.append(j.profiles)
            return render(request, self.template_name, {'connections': connections,'friends':friends,'object':object, 'obj': obj,'job':job,'gs':gs,'s':s,'link':link,'cl':cl,'d':d})
            #return render(request, self.template_name, {'connection': connection, 'obj': obj})

def Upload_profile_photo(request,pk):
    if 'upload_profile_photo' in request.POST:
        profile_photo=request.FILES['photo']
        photo=profile.objects.get(user=request.user)
        photo.profilepicture=profile_photo
        photo.save()
        return redirect('/users/profile/'+str(pk))
    else:
        return render(request,'profile-pic.html')

def Upload_cover_photo(request,pk):
    if 'upload_cover_photo' in request.POST:
        cover_photo=request.FILES['cover-photo']
        print("x")
        photo=profile.objects.get(user=request.user)
        print('y')
        photo.cover_picture=cover_photo
        print('z')
        photo.save()
        return redirect('/users/profile/'+str(pk))
    else:
        return render(request,'cover-pic.html')

# def EditProfile(request,pk):
#     p=profile.objects.get(user=request.user)
#     print(p)
#     if 'job' in request.POST:
#         job=profession(profile_id=p.id,profession=request.POST['proffession'],company=request.POST['company'])
#         job.save()
#         return  render(request,'edit_proffession.html',{'p':p,'job':job})
#     else:
#         return  render(request,'edit_proffession.html',{'p':p})

class EditProffession(UpdateView):
    model = profession
    fields = ('profession', 'company')
    template_name = 'edit_proffession.html'
    login_url = 'login'
    success_url = reverse_lazy('home')
class Editgraduateschool(UpdateView):
    model = Graduate_school
    #fields = ('Graduate_school_name', 'start','end',)
    form_class = editgraduateschool
    template_name = 'edit_graduate_school.html'
    login_url = 'login'
    success_url = reverse_lazy('home')
class Editcollege(UpdateView):
    model = college
    #fields = ('Graduate_school_name', 'start','end',)
    form_class = editcollege
    template_name = 'edit_college.html'
    login_url = 'login'
    success_url = reverse_lazy('home')

class Editschool(UpdateView):
    model = school
    form_class = editschool
    template_name = 'edit_school.html'
    login_url = 'login'
    success_url = reverse_lazy('home')
class EditProfile(UpdateView):
    model = profile
    fields = ('contact',)
    template_name = 'edit_profile.html'
    login_url = 'login'
    success_url = reverse_lazy('home')

class Editlink(UpdateView):
    model = social_link
    fields = ('Facebook','Instragram','Linkedin','Twitter','Github',)
    template_name = 'edit_link.html'
    login_url = 'login'
    success_url = reverse_lazy('home')

class Editaddress(UpdateView):
    model = profile
    fields = ('address','Home',)
    template_name = 'edit_address.html'
    login_url = 'login'
    success_url = reverse_lazy('home')



