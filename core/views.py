from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import profile
from django.contrib.auth import update_session_auth_hash
from .forms import PasswordChangeForm
# Create your views here.

@login_required(login_url='login')
def index(request):
    user_object = User.objects.get(username = request.user.username)
    try:
        user_profile = profile.objects.get(user=user_object)
    except:
        messages.info(request, 'Credentials Invalid')
        return redirect('login')
    # posts = Post.objects.all()
    # dash_obj = profile.objects.get(user = request.user)
    context={
        'user_profile':user_profile,
        # 'posts':posts
    }
    return render(request,'index.html', context)

@login_required(login_url='login')
def setting(request):
    user_profile = profile.objects.get(user = request.user)

    if request.method == "POST":
        if request.FILES.get('image') == None:
            image = user_profile.profileimg
            username = request.POST['username']
            email = request.POST['email']
            phone = request.POST['phone']
            bio = request.POST['bio']

            user_profile.profileimg = image
            user_profile.name = username
            user_profile.email = email
            user_profile.phone = phone
            user_profile.bio = bio
            user_profile.save()

        if request.FILES.get('image') != None:
            image = request.FILES.get('image')
            username = request.POST['username']
            email = request.POST['email']
            phone = request.POST['phone']
            bio = request.POST['bio']

            user_profile.profileimg = image
            user_profile.name = username
            user_profile.email = email
            user_profile.phone = phone
            user_profile.bio = bio
            user_profile.save()

        return redirect('settings')
    
    context={
        'user_profile': user_profile
    }
    return render(request,'setting.html',context)

def signup(request):

    if request.method == "POST":
        form = request.POST
        username = form['username']
        email = form['email']
        password = form['password']
        password2 = form['password2']
        phone = form['phone']
        description = form['description']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request,"Email Taken")
                return redirect("signup")
            elif User.objects.filter(username=username).exists():
                messages.info(request,"Username Taken")
                return redirect("signup")
            else:
                user = User.objects.create_user(username=username, email=email,password=password)
                user.save()

                #Log user in and redirect to settings page
                user_login = auth.authenticate(username=username, password=password)
                auth.login(request, user_login)
                #create a Profile object for the new user
                user_model = User.objects.get(username=username)
                new_profile = profile.objects.create(user=user_model, name = username, id_user = user_model.id, email = email, phone = phone, bio = description)
                new_profile.save()
                return redirect('settings')
        else:
            messages.info(request,"Password Not Matched")
            return redirect('signup')
    else:
        return render(request,'signup.html')


def login_view(request):

    if request.method == "POST":
        form = request.POST
        username = form['username']
        password = form['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Credentials Invalid')
            return redirect('login')
    else:
        return render(request,'login.html')
    
@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    return redirect('login')

@login_required(login_url='login')
def change_password(request):
    form = PasswordChangeForm(user=request.user)
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            user = form.save()
            # Update session authentication hash to avoid logging out the user
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password has been updated!')
            return redirect('index')
        else:
            messages.error(request, 'Please correct the errors below.')
    return render(request, 'changePassword.html', {'form': form})