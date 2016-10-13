from django import forms
from models import Venue

class VenueForm(forms.ModelForm):
    selected = forms.BooleanField()

    class Meta:
        model = Venue