from django.shortcuts import render, redirect
from .forms import SubmissionForm
from place_sub.models import Place_sub
from .models import Submission
from place_sub.forms import Place_subForm
from django.contrib.auth.decorators import login_required
from account.models import Account
from place_sub.models import Place_sub
from django.contrib import messages
from place.models import Place
from city.models import City
from django.core.mail import send_mail
from django.conf import settings
from account.models import Account

def check_place(place_sub, queue=1):
    '''
        This function check if some place and term are available.
        Only one person (queue by default=1) can submit to one place at interval time (default=15min).
        place_sub - as object than __str__ method can be used to concatenate with empty string.
        Return True if place_with_term is available, False if not.
    '''
    count = 0
    place_sub_as_text = ""
    place_sub_as_text += str(place_sub) + "+00:00"
    for place in Place_sub.objects.all():
        place_text = ''
        place_text += str(place)
        if place_text == place_sub_as_text:
            count += 1
        if count >= queue:
            return False

    return True

@login_required
def submission_view(request):
    context = {}
    if request.method == "POST":
        if request.user.is_authenticated:
            sub_form = SubmissionForm(request.POST)
            place_sub_form = Place_subForm(request.POST)
            if sub_form.is_valid() and place_sub_form.is_valid():
                obj_sub = sub_form.save(commit=False)
                obj_sub.user = Account.objects.get(pk=request.user.id)
                obj_place_sub_form = place_sub_form.save(commit=False)
                obj_place_sub_form.sub_id = obj_sub
                # choose place
                if check_place(obj_place_sub_form):
                    obj_sub.save()
                    obj_place_sub_form.save()
                    request.user.user_submission = True
                    request.user.save()
                    submission = Submission.objects.filter(user=request.user).get()
                    place_text = Place_sub.objects.filter(sub_id=submission).get()
                    place_as_text = ""
                    place_as_text += str(place_text)
                    size = len(place_as_text)
                    place_as_text = place_as_text[:size -9]
                    message_content = ""
                    message_content += "Szanown(y)/(a) Panie/Pani," + '\n\n' \
                                    + "Zostal Pan pozytywnie zakwalifikowany do szczepienia!" \
                                    + '\n' + "Miejsce i termin szczepienia: " + place_as_text
                    account = submission.user.email
                    mail = ""
                    mail += account
                    send_mail(
                        "Potwierdzenie rejestracji na szczepienie przeciw Covid-19", #subject
                        message_content, #message
                        settings.EMAIL_HOST_USER, #from send_mail
                        [mail], # to mail
                    )
                else:
                    place_as_text = None
                    messages.error(request, f'Wybierz inny termin wizyty!')
    else:
        sub_form = SubmissionForm()
        place_sub_form = Place_subForm()
        place_as_text = None

    context = {"sub_form": sub_form,
               "place_sub_form": place_sub_form,
               "place_text": place_as_text,
               "submission_num": Submission.objects.count() }

    return render(request, "submission/submission.html", context)
