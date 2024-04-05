from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

from .models import User

User = get_user_model()

class RegisterCustomerForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']