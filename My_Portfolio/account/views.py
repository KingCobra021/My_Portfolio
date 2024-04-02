from django.shortcuts import redirect, render
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

    return render(request, "account/login.html", {"login_form": form})
