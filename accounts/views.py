from django.utils import timezone
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from accounts.forms import NewUserForm, LoginForm, OtpForm, AvatarForm, TeamMembersForm
from accounts.models import NewUser, TeamLeader
from django.contrib.auth.decorators import login_required


def signup(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home:home')
        else:
            return render(request, 'accounts/signup.html', {'form': form})
    else:
        return render(request, 'accounts/signup.html', {'form': NewUserForm()})


def login_attempt(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            request.session['phone_number'] = form.data['phone_number']
            return redirect('accounts:otp')
        return render(request, 'accounts/login.html', {'form': form})
    return render(request, 'accounts/login.html', {'form': LoginForm()})


def check_otp(request):
    if request.method == 'POST':
        form = OtpForm(request.POST)
        if form.is_valid():
            phone_number = request.session['phone_number']
            otp = form.data['otp']
            get_user = NewUser.objects.filter(phone_number=phone_number).first()
            if get_user is None:
                return redirect('accounts:signup')
            elif timezone.now() > get_user.otp_expire:
                return render(request, 'accounts/otp_login.html',
                              {'form': OtpForm(), 'message': 'otp code expire login and get otp code again'})
            elif otp == str(get_user.otp):
                login(request, get_user)
                return redirect('home:home')
            return render(request, 'accounts/otp_login.html', {'form': OtpForm(), 'message': 'otp code is wrong'})
        return render(request, 'accounts/otp_login.html', {'form': form})
    return render(request, 'accounts/otp_login.html', {'form': OtpForm()})


def user_logout(request):
    logout(request)
    return redirect('home:home')


@login_required()
def user_profile(request, pk):
    get_user = NewUser.objects.get(id=pk)
    if request.method == 'POST':
        form = AvatarForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('accounts:profile', request.user.id)
        else:
            form = AvatarForm(instance=request.user)
        return render(request, 'accounts/profile.html', {'get_user': get_user, 'form': form})
    return render(request, 'accounts/profile.html', {'get_user': get_user, 'form': AvatarForm()})


def add_to_group(request, pk):
    if request.method == 'POST':
        form = TeamMembersForm(request.POST, request=request)
        if form.is_valid():
            # form.save()
            pass
        return render(request, 'accounts/join-group.html',
                      {'form': form, 'message': 'You have been added to the group'})
    return render(request, 'accounts/join-group.html', {'form': TeamMembersForm()})
