from django.forms import ModelForm
from app.models import Games

class GamesForm(ModelForm):
    class Meta:
        model = Games
        fields = ['title', 'category', 'console', 'asin', 'language']