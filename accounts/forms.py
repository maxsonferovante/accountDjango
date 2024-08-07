from django import forms
from django.contrib.auth import get_user_model, password_validation

User = get_user_model()


class UserRegisterForm(forms.ModelForm):

    password = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        help_text=password_validation.password_validators_help_text_html(),
    )
    username = forms.CharField(
        label="Username",
        strip=False,
        validators= [User._meta.get_field("username").validators[0]],
        widget=forms.TextInput(attrs={"autocomplete": "username"}),
    )

    class Meta:
        model = User
        fields = ["email", "username"]


    def save(self, commit: bool = True) -> User:
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

