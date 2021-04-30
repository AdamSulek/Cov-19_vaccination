from django import forms
from .models import Submission

class SubmissionForm(forms.ModelForm):
    dialisis = forms.TypedChoiceField(
                   coerce=lambda x: x == 'True',
                   choices=((False, 'NIE'), (True, 'TAK')),
                   widget=forms.RadioSelect, initial=False)
    cancers = forms.TypedChoiceField(
                   coerce=lambda x: x == 'True',
                   choices=((False, 'NIE'), (True, 'TAK')),
                   widget=forms.RadioSelect, initial=False)
    transplant = forms.TypedChoiceField(
                   coerce=lambda x: x == 'True',
                   choices=((False, 'NIE'), (True, 'TAK')),
                   widget=forms.RadioSelect, initial=False)
    thrombosis = forms.TypedChoiceField(
                   coerce=lambda x: x == 'True',
                   choices=((False, 'NIE'), (True, 'TAK')),
                   widget=forms.RadioSelect, initial=False)
    chronic = forms.TypedChoiceField(
                   coerce=lambda x: x == 'True',
                   choices=((False, 'NIE'), (True, 'TAK')),
                   widget=forms.RadioSelect, initial=False)

    class Meta:
        model = Submission
        fields = (
                "dialisis",
                "cancers",
                "transplant",
                "thrombosis",
                "chronic",
                "drugs",
                "additional_question"
            )
