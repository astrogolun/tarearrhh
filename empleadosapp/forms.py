# forms.py

from django import forms

class EmployeeFilterForm(forms.Form):
    national_id = forms.CharField(max_length=15, required=False)
    start_date = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))
    end_date = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))
