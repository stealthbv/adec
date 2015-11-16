from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()


class RegisterUserForm(forms.ModelForm):
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput, required=True)
    password2 = forms.CharField(
        label="Confirm password",
        widget=forms.PasswordInput, required=True)
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

    def clean_username(self):
        data = self.cleaned_data['username'].strip()

        if User.objects.filter(username=data).exists():
            raise forms.ValidationError("A user with the same username already exists")

        return data

    def clean_email(self):
        data = self.cleaned_data['email'].strip()

        if User.objects.filter(email=data).exists():
            raise forms.ValidationError("A user with that email address already exists")

        return data

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1', '')
        password2 = self.cleaned_data.get('password2', '')

        if password1 != password2:
            raise forms.ValidationError("The two password fields didn't match.")
        return password2

    def save(self, commit=True):
        user = super(RegisterUserForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])

        if commit:
            user.save()

        return user
