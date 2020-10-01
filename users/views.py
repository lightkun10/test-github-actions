from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

# Create your views here.

# Display info about the currently signed in user
def index(request):
    # If user not authenticated...
    if not request.user.is_authenticated:
        # Redirect user to login view
        return HttpResponseRedirect(reverse("login"))
    # If user is authenticated, 
    # redirect them to user page
    return render(request, "users/user.html")

# Login view
def login_view(request):
    # If user is submitting a login data
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        # Try to authenticate user
        user = authenticate(request, username=username, password=password)
        # If authentication is a success...
        if user is not None:
            # Log the user in
            login(request, user)
            # Redirect user to the index route
            return HttpResponseRedirect(reverse("index"))
        # else if authentication is a failure...
        else:
            # Render the same user login page again 
            # and add additional context
            return render(request, "users/login.html", {
                "message": "Invalid credentials."
            })


    # A form where user can log themselves in
    return render(request, "users/login.html")

def logout_view(request):
    # pass
    logout(request)
    # After user logged out, take 
    # them back to the login page
    return render(request, "users/login.html", {
        "message": "Logged out."
    })