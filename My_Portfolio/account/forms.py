from django import forms
from django.contrib.auth import authenticate
from account.models import Account



class AccountAuthenticationForm(forms.Form):  # Changed to `forms.Form` for simplicity
    email = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(attrs={'placeholder': 'Enter your email'}),
    )
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'placeholder': 'Enter your password'}),
    )

    def clean(self):
        cleaned_data = super().clean()  # Apply default validations
        email = cleaned_data.get("email")
        password = cleaned_data.get("password")

        if email and password:
            # Authenticate user using email and password
            user = authenticate(email=email, password=password)
            if not user:
                raise forms.ValidationError("Invalid email or password.")
        else:
            raise forms.ValidationError("Both email and password are required.")

        return cleaned_data

    class Meta:
        model = Account
        fields = ("email", "password")
        widgets = {
            'email': forms.EmailInput(attrs={'placeholder': 'Enter your email'}),
        }

    def clean(self):
        cleaned_data = super().clean()  # Ensure built-in validations are applied
        email = cleaned_data.get("email")
        password = cleaned_data.get("password")

        if not authenticate(email=email, password=password):
            raise forms.ValidationError("Invalid email or password")

        return cleaned_data


class OTPVerificationForm(forms.Form):
    otp = forms.CharField(
        label="OTP",
        max_length=6,
        widget=forms.TextInput(attrs={'placeholder': 'Enter your OTP'})
    )

