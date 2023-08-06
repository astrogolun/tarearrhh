from django import forms

class EmployeeFilterForm(forms.Form):
    national_id_number = forms.IntegerField(required=False, widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'National ID Number'}))
    fecha_inicio = forms.DateField(required=False, widget=forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Fecha Inicio (AAAA-MM-DD)'}))
    fecha_termino = forms.DateField(required=False, widget=forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Fecha Termino (AAAA-MM-DD)'}))

