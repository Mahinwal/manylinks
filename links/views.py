from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Profile

def home(request):
    if request.user.is_authenticated:
        return redirect('profile')
    else:
        return render(request, 'links/index.html', {})

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user_login = authenticate(username=username, password=password)

        if user_login is not None:
            login(request, user_login)
            return redirect('profile')
        else:
            messages.warning(request, 'Invalid credentials')
            return redirect('home')
    else:
        return redirect(request, 'home')

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password1 = request.POST['password1']

        if password == password1:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username already taken.")
                return redirect('signup')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email already taken.')
                return redirect('signup')
            else:
                print("here")
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()

                user_login = authenticate(username=username, password=password)
                login(request, user_login)
                return redirect('profile')
    else:
        return render(request, 'links/signup.html', {})


@login_required(login_url='signin')    
def profile(request):

    context = {
        'user': request.user,
    }

    if Profile.objects.filter(user=request.user).exists():
        user_profile = Profile.objects.get(user=request.user)
                
        context = {
            'user_profile': user_profile,
            }
    
    return render(request, 'links/profile.html', context)
    

@login_required(login_url='signin')
def profile_update(request):
    user = User.objects.get(username=request.user.username)
    if request.method == 'POST':
        
        fullname = request.POST['fullname']
        about = request.POST['about']
        facebook = request.POST['facebook']
        instagram = request.POST['instagram']
        twitter = request.POST['twitter']
        linkedin = request.POST['linkedin']
        youtube = request.POST['youtube']
        github = request.POST['github']
        email = request.POST['email']

        user_profile = Profile.objects.update_or_create(user=user, defaults={'fullname': fullname, 'about':about, 'facebook':facebook, 'instagram':instagram, 'twitter':twitter, 'linkedin':linkedin, 'youtube': youtube, 'github':github})
        messages.info(request, "Your profile has been successfully updated!")
        return redirect('profile')
    else:
        return redirect('profile')

@login_required(login_url='signin')    
def user_logout(request):
    logout(request)
    return redirect('home')

@login_required(login_url='signin')
def change_password(request):
    if request.method == 'POST':
        user = User.objects.get(username=request.user.username)
        old_password = request.POST['password']
        new_password = request.POST['newpassword']
        renew_password = request.POST['renewpassword']

        if not user.check_password(old_password):
            messages.warning(request, "Old password is mismatched.")
            return redirect('profile')
        elif old_password == new_password:
            messages.warning(request, "New password is the same as the old password.")
            return redirect('profile')
        elif new_password != renew_password:
            messages.warning(request, "New password and re-password are mismatched.")
            return redirect('profile')
        else:
            user.set_password(new_password)
            user.save()
            # Log out the user
            logout(request)
            return redirect('home')
