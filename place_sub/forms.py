from django import forms
from .models import Place_sub
from django.contrib.admin import widgets
# import floppyforms as forms
# from .models import Date_Time
from django.forms import ModelForm
from datetime import datetime, timedelta
import datetime
from django.forms import widgets
import pandas as pd

def get_dates(start_time='07:00', end_time='15:00', period=5):
    today = datetime.date.today()
    start = today.strftime('%Y-%m-%d T') + start_time
    end_day = today + timedelta(days=period)
    end = end_day.strftime('%Y-%m-%d T') + end_time
    date_time = (pd.DataFrame(columns=['NULL'],
                              index=pd.date_range(start, end,
                              freq='15T'))
       .between_time(start_time, end_time)
       .index.strftime('%Y-%m-%d %H:%M')
       .tolist()
    )
    result = []
    for dt in date_time:
        result.append((dt, dt))
    return result

class Place_subForm(forms.ModelForm):
    DATE_CHOICES = get_dates()
    # DATE_CHOICES = (
    #         ("2021-04-30 7:30", "2021-04-30 7:30"),
    #         ("2021-04-30 8:30", "2021-04-30 8:30"),
    #         ("2021-04-30 9:30", "2021-04-30 9:30"),
    # )
    date_time = forms.ChoiceField(choices=DATE_CHOICES)

    class Meta:
        model = Place_sub
        fields = (
                "place_id",
                "date_time"
            )
