from django import forms  
from Elearning.models import Etudiant
class EtudiantForm(forms.ModelForm):
    class Meta:  
        model = Etudiant
        fields = ['nom', 'prenom', 'email']
        widgets = { 'nom': forms.TextInput(attrs={ 'class': 'form-control' }),
            'prenom': forms.TextInput(attrs={ 'class': 'form-control' }),
            'email': forms.EmailInput(attrs={ 'class': 'form-control' }),
                }