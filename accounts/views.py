from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from accounts.forms import NewUserForm


def signup(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            return render(request, 'accounts/signup.html', {'form': form})
    else:
        return render(request, 'accounts/signup.html', {'form': NewUserForm()})
