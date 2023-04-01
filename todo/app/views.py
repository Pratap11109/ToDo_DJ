from django.shortcuts import render
from django.views import View
from .forms import SignupForm, ToDoForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic.edit import FormView,UpdateView,DeleteView
from django.urls import reverse_lazy
from .models import ToDo

# Create your views here.


class AddView(FormView):
    form_class = ToDoForm
    template_name = "app/todo.html"
    success_url = "../profile/"

    def form_valid(self, form):
        messages.success(self.request, 'form is valid')
        form.instance.user = self.request.user
        form.save()
        return super().form_valid(form)
    
class UpdatTodoView(UpdateView):
    model  = ToDo
    template_name = "app/todo.html"
    fields = ['date',"title","description","priority"]
    success_url = "../profile/"

    def form_valid(self, form):
        messages.success(self.request, 'form is valid')
        form.instance.user = self.request.user
        form.save()
        return super().form_valid(form)
        
class ToDoDeleteView(DeleteView):
    model = ToDo
    template_name = "app/delete.html"
    success_url = reverse_lazy('profile')

def home(request):
    return render(request,"app/home.html")

class SignupView(View):
    def get(self,request):
        if request.user.is_authenticated:
            return HttpResponseRedirect("../profile/")
        form = SignupForm()
        return render(request,"app/signup.html",{"form":form})
    
    def post(self,request):
        if request.user.is_authenticated:
            return HttpResponseRedirect("../profile/")
        form = SignupForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]

            if User.objects.filter(email=email).exists():
                messages.error(request,"User Already Exits with this mail")
                return render(request,"app/signup.html",{"form":form})
            else:
                form.save()
                messages.success(request,"user Created Successfully.")
                return HttpResponseRedirect("../login/")
        return render(request,"app/signup.html",{"form":form})

class LoginView(View):

    def get(self,request):
        if request.user.is_authenticated:
            return HttpResponseRedirect("../profile/")
        form = AuthenticationForm()
        return render(request,"app/login.html",{"form":form})
    
    def post(self,request):
        if request.user.is_authenticated:
            return HttpResponseRedirect("../profile/")
        form = AuthenticationForm(request,request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                messages.success(request,"Login Successfully.")
                return HttpResponseRedirect("../profile/")
            else:
                messages.error(request,"Enter Valid Credential.")
        else:
            messages.error(request,"Enter Valid Data..")
        form = AuthenticationForm()
        return render(request,"app/login.html",{"form":form})

        
class ProfileView(View):
    @method_decorator(login_required)
    def get(self,request):
        data = ToDo.objects.filter(user=request.user)
        return render(request,"app/profile.html",{"data":data})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect("../")

