from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, logout
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.http import HttpResponseRedirect
from django.views.generic import DetailView , View,CreateView
# Create your views here.
from accounts.forms import NewUserForm, LoginForm, OtpForm, JoinGroupForm
from accounts.models import NewUser , TeamMembers , TeamLeader


def signup(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
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
            try:
                phone_number = request.session['phone_number']
            except:
                phone_number = 00000000000
            otp = form.data['otp']
            get_user = NewUser.objects.filter(phone_number=phone_number).first()
            if get_user is None:
                return redirect('accounts:signup')
            if otp == str(get_user.otp):
                login(request, get_user)
                return redirect('home:home')
            return render(request, 'accounts/otp_login.html', {'form': OtpForm(), 'message': 'otp code is wrong'})
        return render(request, 'accounts/otp_login.html', {'form': form})
    return render(request, 'accounts/otp_login.html', {'form': OtpForm()})


def user_logout(request):
    logout(request)
    return redirect('home')



class UserProfile(DetailView):
    model = NewUser
    template_name = "accounts/userprofile.html"
    context_object_name = "user"


@method_decorator(csrf_exempt, name='dispatch')
class JoinGroup(CreateView):
    form_class = JoinGroupForm
    template_name = "accounts/joingroup.html"
    redirect_authenticated_user = True
    success_url = reverse_lazy('user-profile')


    def get(self, *args, **kwargs):
        if TeamMembers.objects.filter(users=self.request.user).exists():
            return redirect("home:home")
        return render(self.request,self.template_name,{
            "form":self.form_class
        })

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            TeamMembers.objects.create(leader=form.cleaned_data["leader"],users=request.user)
            TeamMembers.save()
    
    
    