from django import forms
from django.contrib.auth.models import User


class RegisterForm(forms.ModelForm):
    username = forms.CharField(label="username", required=True)
    password = forms.CharField(label="password", strip=False, required=True, widget=forms.PasswordInput)
    password_confirm = forms.CharField(label="confirm_password", strip=False, required=True, widget=forms.PasswordInput)
    # avatar = forms.ImageField(label="avatar", required=True)

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")
        # avatar = cleaned_data.get("avatar")

        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError('Password mismatch')
        if not username:
            raise forms.ValidationError("Enter the username")
        if not password:
            raise forms.ValidationError('Enter password')
        if not password_confirm:
            raise forms.ValidationError('Confirm password!')
        # if not avatar:
        #     raise forms.ValidationError('Enter your avatar')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

    class Meta:
        model = User
        fields = ['username', 'password', 'password_confirm',]
