from django.forms import ModelForm, TextInput
from app.models import Games

class GamesForm(ModelForm):
    class Meta:
        model = Games
        fields = ['title', 'category', 'console', 'asin', 'language']
        widgets = {
            'title': TextInput(attrs={'class':'form-control'}),
            'category': TextInput(attrs={'class':'form-control'}),
            'console': TextInput(attrs={'class':'form-control'}),
            'asin': TextInput(attrs={'class':'form-control'}),
            'language': TextInput(attrs={'class':'form-control'}),
        }