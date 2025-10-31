from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from .models import Users
from django import forms


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "placeholder": "Никнейм"
    }))

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        "class": "form-control",
        "placeholder": "Пароль"
    }))

    class Meta:
        model = Users
        fields = ("username", "password")


class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "placeholder": "Имя"
    }))

    last_name = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "placeholder": "Фамилия"
    }))

    username = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "placeholder": "Никнейм"
    }))

    email = forms.EmailField(widget=forms.EmailInput(attrs={
        "class": "form-control",
        "placeholder": "Эл. почта"
    }))

    telephone = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "placeholder": "Номер телефона"
    }))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        "class": "form-control",
        "placeholder": "Пароль"
    }))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        "class": "form-control",
        "placeholder": "Повторите пароль"
    }))

    class Meta:
        model = Users
        fields = ("first_name", "last_name", "username", "email", "telephone", "password1", "password2")


class Profile(UserChangeForm):
    image = forms.ImageField(widget=forms.FileInput(attrs={"class": "custom-file-input"}), required=False)
    first_name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    username = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "readonly": True}))
    email = forms.CharField(widget=forms.EmailInput(attrs={"class": "form-control", "readonly": True}))
    telephone = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    region = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    district = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    city = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    street = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    house_number = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))
    entrance_number = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    flat_number = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    post_index = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)

    class Meta:
        model = Users
        fields = (
            "image",
            "first_name",
            "last_name",
            "username",
            "email",
            "telephone",
            "region",
            "district",
            "city",
            "street",
            "house_number",
            "entrance_number",
            "flat_number",
            "post_index")