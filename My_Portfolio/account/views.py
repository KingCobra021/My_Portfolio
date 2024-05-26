'''from django.shortcuts import redirect, render
from django.contrib.auth import login, logout, authenticate
from account.forms import AccountAuthenticationForm


# Create your views here.
def logout_view(request):
    logout(request)
    return redirect('home')


def login_view(request):
    user = request.user
    if user.is_authenticated:
        return redirect("home")

    if request.method == 'POST':
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']  # Use cleaned_data to access form data
            password = form.cleaned_data['password']
            user = authenticate(email=email, password=password)
            if user:
                login(request, user)
                return redirect("home")
    else:
        form = AccountAuthenticationForm()

    return render(request, "account/login.html", {"login_form": form})'''



from django.shortcuts import redirect, render
from django.contrib.auth import login, logout, authenticate
from account.forms import AccountAuthenticationForm
from django.http import JsonResponse

def logout_view(request):
    logout(request)
    return redirect('home')

def login_view(request):
    user = request.user
    if user.is_authenticated:
        return redirect("home")

    if request.method == 'POST':
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(email=email, password=password)
            if user:
                # Temporarily login the user to check OTP
                login(request, user)
                return JsonResponse({"success": True, "message": "Authenticated. Proceed to OTP verification."})
            else:
                return JsonResponse({"success": False, "errors": "Invalid email or password."})
        else:
            return JsonResponse({"success": False, "errors": form.errors})
    else:
        form = AccountAuthenticationForm()

    return render(request, "account/login.html", {"login_form": form})

def otp_verify_view(request):
    if request.method == 'POST':
        otp = request.POST.get('otp')
        # Add your OTP verification logic here
        if otp == "123456":  # Example OTP check
            return JsonResponse({"success": True, "message": "OTP verified. Login successful."})
        else:
            return JsonResponse({"success": False, "errors": "Invalid OTP."})
    return render(request, "account/otp_verify.html")
