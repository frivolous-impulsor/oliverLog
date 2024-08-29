from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .forms import UserUpdateForm, ProfileUpdateForm
from .models import Profile
# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST) #a form with post-input data
        if form.is_valid():
            form.save() #create entry in database
            username = form.cleaned_data.get('username')
            messages.success(request, f'An account for {username} is registered successfully')
            return redirect('login')
    else:
        form = UserRegisterForm() #empty form
    return render(request, 'users/register.html', {'form': form}) #form depends on page fresh or not

def confirm_logout(request):
    return render(request, 'users/confirm_logout.html')

def UserLogout(request):
    logout(request)
    return render(request, 'users/logout.html')

@login_required
def profile_update(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance = request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance = request.user.profile)
        if u_form.is_valid() and p_form.is_valid:
            u_form.save()
            p_form.save()
            messages.success(request, f'Profile of Acccount {request.user.username} is updated')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance = request.user)
        p_form = ProfileUpdateForm(instance = request.user.profile)
    
    context = {'u_form': u_form, 'p_form': p_form}
    return render(request, 'users/profile_form.html', context)

@login_required
def profile_view(request):
    profile = Profile.objects.filter(user = request.user).first()
    return render(request, 'users/profile.html', {'profile': profile})