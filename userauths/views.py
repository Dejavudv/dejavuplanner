from django.shortcuts import render,redirect
from userauths.forms import  UserRegisterForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.conf import settings
from userauths.models import User


# User = settings.AUTH_USER_MODEL

def register_view(request):



    if request.method == "POST":
        form = UserRegisterForm(request.POST or None)
        if form.is_valid():
            new_user = form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"hey {username}, your account was created successfully")
            new_user = authenticate(username = form.cleaned_data["email"], 
                                    password = form.cleaned_data["password1"]
            )
            login(request, new_user)
            return redirect("core:index")



    else:
        form = UserRegisterForm()


    context = {
        'form': form,
    }
    return render(request, "userauths/sign-up.html", context)


def login_view(request):
    if request.user.is_authenticated:
        messages.warning(request, f"hey you are already logged in")
        return redirect('core:index')
    
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        try:
            user = User.objects.get(email = email)
            user = authenticate(request, email = email, password = password)

            if user is not None:
                login(request, user)
                messages.success(request,"you are logged in")
                return redirect("core:index")
            
            else:
                messages.warning(request, "user doesnt exist create an account.")
                # return redirect("userauths/sign-up.html")
        except:
            messages.warning(request, f"user with {email} does not exist")
            return redirect("core:index")


             

    context = {

    }

    return render(request, "userauths/sign-in.html", context)


def logout_view(request):
    logout(request)
    messages.success(request, "you are logged out")

    return redirect("core:index")
    # return render(request, "userauths/sign-in.html")