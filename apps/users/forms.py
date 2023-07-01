from django import forms

class LoginForm(forms.Form):
    login_name = forms.CharField(
        label="Nome de usuário",
        required=True,
        max_length=100,
        widget = forms.TextInput(
            attrs={
                "class": "login-input"
            }
        )
    )

    password = forms.CharField(
        label="Senha",
        required=True,
        widget = forms.PasswordInput(
            attrs={
                "class": "login-input"
            }
        )
    )