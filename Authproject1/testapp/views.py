from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from testapp.forms import SignUpForm
from django.http import HttpResponseRedirect
# Create your views here.
def home_page_view(request):
    return render(request,"testapp/home.html")
@login_required
def java_page_view(request):
    return render(request,"testapp/javaexams.html")

@login_required
def python_page_view(request):
    return render(request,"testapp/pythonexams.html")

@login_required
def apptitude_page_view(request):
    return render(request,"testapp/apptitudeexams.html")

@login_required
def Logout_page_view(request):
    return render(request,'testapp/logout.html')

def Signup_page_view(request):
    form=SignUpForm()
    if request.method=="POST":
        form=SignUpForm(request.POST)
        user=form.save()
        user.set_password(user.password)
        user.save()
        return HttpResponseRedirect("/accounts/login")
    return render(request,"testapp/sign_up.html",{"form":form})
