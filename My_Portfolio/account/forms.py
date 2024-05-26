from django import forms
from django.contrib.auth import authenticate
from account.models import Account


class AccountAuthenticationForm(forms.ModelForm):
    password = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'placeholder': 'Enter your password'})
    )

    class Meta:
        model = Account
        fields = ("email","password")
        widgets = {
            'email': forms.EmailInput(attrs={'placeholder': 'Enter your email'}),
        }

    def clean(self):
        if self.is_valid():
            email = self.cleaned_data["email"]
            password = self.cleaned_data["password"]
            if not authenticate(email=email, password=password):
                raise forms.ValidationError("invalid email/password")
class OTPVerificationForm(forms.Form):
    otp = forms.CharField(label="OTP", max_length=6, widget=forms.TextInput(attrs={'placeholder': 'Enter your OTP'}))
