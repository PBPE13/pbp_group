from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from main.models import Profile

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your username',
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your password',
    }))

class RegisterForm(UserCreationForm):
    STATUS_CHOICES = [('M', 'Member'), ('A', 'Admin')]
    role = forms.ChoiceField(
        required=True,
        choices=STATUS_CHOICES
    )
    name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your username',
    }))
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your username',
    }))
    preferred_genre = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'What are your favorite genres ?',
    }))
    bio_data = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder': 'Tell us about yourself !',
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your password',
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Repeat password',
    }))
    class Meta:
        model = User
        fields = ('role', 'name', 'username', 'preferred_genre', 'bio_data', 'password1', 'password2')

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.role = self.cleaned_data["role"]
        user.name = self.cleaned_data["name"]
        user.preferred_genre = self.cleaned_data["preferred_genre"]
        user.bio_data = self.cleaned_data["bio_data"]

        if commit:
            user.save()
        
        return user