from .models import Account
from bboard.models import Bboard
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

class RegistrationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Account
        fields = UserCreationForm.Meta.fields + ("email", )


class PostForm(ModelForm):
    class Meta:
        model = Bboard
        fields = ['name', 'description', 'price']