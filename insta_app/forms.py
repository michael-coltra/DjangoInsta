from django.forms import ModelForm
from .models import UsernameInstagramUser


class InstaForm(ModelForm):
    class Meta:
        model = UsernameInstagramUser
        fields = '__all__'
