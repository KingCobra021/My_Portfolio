from django.shortcuts import redirect, render
from django.contrib.auth import login, logout, authenticate, get_user_model
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib import messages
from account.forms import AccountAuthenticationForm, OTPVerificationForm
from django_otp.plugins.otp_totp.models import TOTPDevice


def logout_view(request):
    """Logs the user out and redirects to the home page."""
    logout(request)
    return redirect('home')


def login_view(request):
    if request.user.is_authenticated:
        return redirect("home")  # Redirect if already logged in

    if request.method == 'POST':
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            # Authenticate the user
            user = authenticate(email=email, password=password)
            if user:
                # Temporarily store the user ID in the session
                request.session['pre_otp_user_id'] = user.id
                return redirect("otp_verify")  # Redirect to OTP verification
            else:
                messages.error(request, "Invalid email or password.")
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = AccountAuthenticationForm()

    return render(request, "account/login.html", {"login_form": form})

User = get_user_model()
def otp_verify_view(request):
    if request.method == 'POST':
        form = OTPVerificationForm(request.POST)
        user_id = request.session.get('pre_otp_user_id')  # Get user ID from session

        if user_id is None:
            messages.error(request, "Session expired. Please log in again.")
            return redirect("login")

        user = User.objects.get(id=user_id)  # Retrieve the user from the database

        if form.is_valid():
            otp = form.cleaned_data['otp']

            # Verify OTP using django-otp
            device = TOTPDevice.objects.filter(user=user).first()
            if device and device.verify_token(otp):
                # Log in the user after successful OTP verification
                login(request, user)
                del request.session['pre_otp_user_id']  # Clear the session
                messages.success(request, "Login successful!")
                return redirect("home")  # Redirect to your home/dashboard page
            else:
                messages.error(request, "Invalid OTP. Please try again.")
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = OTPVerificationForm()

    return render(request, "account/otp_verify.html", {"otp_form": form})