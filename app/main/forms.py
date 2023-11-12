import re
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from .models import Post, Thread


class RegistrationForm(forms.Form):
    username = forms.CharField(label='User name', max_length=30)
    email = forms.EmailField(label='Email')
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput())
    password2 = forms.CharField(label='repeat password', widget=forms.PasswordInput())

    def clean_password(self):
        if 'password1' in self.cleaned_data:
            password1 = self.cleaned_data['password1']
            password2 = self.cleaned_data['password2']
            if password1 == password2 and password1:
                return password2
        raise forms.ValidationError('Неправильный пароль')

    def clean_username(self):
        username = self.cleaned_data['username']
        if not re.search(r'^\w+$', username):
            raise forms.ValidationError('Имя учетной записи не может содержать специальные символы')
        try:
            User.objects.get(username=username)
        except ObjectDoesNotExist:
            return username
        raise forms.ValidationError('Аккаунт уже существует')

    def save(self):
        User.objects.create_user(username= self.cleaned_data['username'], email=self.cleaned_data['email'], password=self.cleaned_data['password1'])


class CommentForm(forms.ModelForm):
    def __int__(self, *args, **kwargs):
        self.UserID = kwargs.pop('UserID', None)
        self.ThreadID = kwargs.pop('ThreadID', None)
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        post = super().save(commit=False)
        post.UserID = self.UserID
        post.ThreadID = self.ThreadID
        post.save()

    class Meta:
        model = Post
        fields = ['Content']


class ThreadForm(forms.ModelForm):
    def __int__(self, *args, **kwargs):
        self.UserID = kwargs.pop('UserID', None)
        self.Board = kwargs.pop('Board', None)
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        thread = super().save(commit=False)
        thread.UserID = self.UserID
        thread.Board = self.Board
        thread.save()

    class Meta:
        models = Thread
        fields = ['Tittle', 'Content']