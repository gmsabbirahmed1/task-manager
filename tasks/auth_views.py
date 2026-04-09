from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib import messages


def register(request):
    """Handle user registration."""
    if request.user.is_authenticated:
        return redirect('tasks:list')

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f'Welcome, {user.username}! Your account has been created.')
            return redirect('tasks:list')
    else:
        form = UserCreationForm()

    return render(request, 'auth/register.html', {'form': form})
