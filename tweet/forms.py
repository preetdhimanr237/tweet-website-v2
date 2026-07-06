from django import forms
from .models import Tweet, Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ["text", "photo"]

        widgets = {
            "text": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 4,
                "placeholder": "What's happening?"
            }),
            "photo": forms.FileInput(attrs={
                "class": "form-control"
            })
        }


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            "class": "form-control"
        })
    )
    first_name = forms.CharField(
    widget=forms.TextInput(attrs={"class": "form-control"})
)

    last_name = forms.CharField(
    widget=forms.TextInput(attrs={"class": "form-control"})
)

    username = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control"
        })
    )

    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            "class": "form-control"
        })
    )

    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            "class": "form-control"
        })
    )

    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "username",
            "email",
            "password1",
            "password2",
        )


class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = [
            "profile_image",
            "bio",
            "location",
            "website",
        ]

        widgets = {

            "bio": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 4,
                "placeholder": "Tell us something about yourself..."
            }),

            "location": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Your Location"
            }),

            "website": forms.URLInput(attrs={
                "class": "form-control",
                "placeholder": "https://example.com"
            }),

            "profile_image": forms.FileInput(attrs={
                "class": "form-control"
            }),

           

        }