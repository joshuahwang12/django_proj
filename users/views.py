from django.shortcuts import render
from django.contrib.auth.forms import UserChangeForm

def register(request):
    form = UserChangeForm()
    return render(request, 'users/register.html', {'form': form})
