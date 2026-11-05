from django import forms
from .models import Reservation


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['nom', 'email', 'telephone', 'personnes', 'date', 'heure', 'message']
        labels = {
            'nom': 'Nom',
            'email': 'Email',
            'telephone': 'Téléphone',
            'personnes': 'Nombre de personnes',
            'date': 'Date souhaitée',
            'heure': 'Heure souhaitée',
            'message': 'Message complémentaire',
        }
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'heure': forms.TimeInput(attrs={'type': 'time'}),
            'message': forms.Textarea(attrs={'rows': 4}),
            'personnes': forms.NumberInput(attrs={'min': 1, 'max': 12}),
        }
