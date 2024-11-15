from django import forms
from .models import Author, User

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'email', 'date_of_birth']

class UsersForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'surname', 'username', 'city']