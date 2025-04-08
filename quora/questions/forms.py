from django import forms
from django.contrib.auth.models import User

from .models import Answer, Question


# User registration form
class UserRegistrationForm(
    forms.ModelForm,
):
    password = forms.CharField(
        widget=forms.PasswordInput,
    )

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
        ]

    def save(
        self,
        commit=True,
    ):
        user = super().save(
            commit=False
        )
        user.set_password(
            self.cleaned_data['password'],
        )
        if commit:
            user.save()
        return user


# User login form
class UserLoginForm(
    forms.Form
):
    username = forms.CharField()
    password = forms.CharField(
        widget=forms.PasswordInput,
    )


# Question posting form
class QuestionForm(
    forms.ModelForm,
):
    class Meta:
        model = Question
        fields = [
            'title',
            'description',
        ]


# Answer form
class AnswerForm(
    forms.ModelForm,
):
    class Meta:
        model = Answer
        fields = [
            'content',
        ]
