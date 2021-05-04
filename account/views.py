from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from .forms import RegistrationForm, AccountForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
import datetime
from place.models import Place
from place_sub.models import Place_sub
from submission.models import Submission

def register_view(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Poprawnie zarejestrowales konto {username}!')
            return redirect("login")
    else:
        form = RegistrationForm()
    return render(request, "account/register.html", {"form": form})

def home_view(request):
    context = {
        'place': Place.objects.all().order_by("city"),
        "submission_num": Submission.objects.count()
    }
    return render(request, "account/home.html", context)

def about_view(request):
    return render(request, "account/about.html")

def logout_view(request):
    logout(request)
    return redirect('/')


def login_view(request):

	context = {}

	user = request.user
	if user.is_authenticated:
		return redirect("profile")

	if request.POST:
		form = AccountForm(request.POST)
		if form.is_valid():
			email = request.POST['email']
			password = request.POST['password']
			user = authenticate(email=email, password=password)

			if user:
				login(request, user)
				return redirect("profile")

	else:
		form = AccountForm()

	context['login_form'] = form

	return render(request, "account/login.html", context)

@login_required
def profile_view(request):
    place_text = None
    if request.user.user_submission:
        submission = Submission.objects.filter(user=request.user).get()
        place_text = Place_sub.objects.filter(sub_id=submission).get()
    context = {
        "place_text": place_text,
        "submission_num": Submission.objects.count()
    }
    return render(request, "account/profile.html", context)
