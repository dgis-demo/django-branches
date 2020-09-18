from django import forms
from .models import Branch


class BranchForm(forms.ModelForm):
    latitude = forms.DecimalField(min_value=-90, max_value=90, required=False)
    longitude = forms.DecimalField(min_value=-180, max_value=180, required=False)

    class Meta(object):
        model = Branch
        exclude = []
