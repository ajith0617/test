
from django.shortcuts import render,redirect
from django.contrib.auth.forms import  UserCreationForm,AuthenticationForm
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate,login as loginuser,logout
from app.forms import TodoForm
from app.models import Todo
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='/login')
def main(request):
    if request.user.is_authenticated:
        user = request.user
        form = TodoForm
        todos = Todo.objects.filter(user=user).order_by('priority')
        return render(request,'app/main.html',{'form':form,'todos':todos})

def login(request):
    form = AuthenticationForm()
    if request.method =='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            usern = form.cleaned_data.get('username')
            passw = form.cleaned_data.get('password')
            user=authenticate(username=usern,password=passw)
            if user is not None:
                loginuser(request,user)
                return redirect('/')
    return render(request,'app/login.html',{'form':form})

def signup(request):
    form = UserCreationForm()
    context = {'form':form}
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request,'User Created Successfully')
            return redirect('/login')
            
        else:
            messages.info(request,'Details are not correct.Try again')
            return redirect('/signup')
            
    return render (request,'app/signup.html',context=context)



def add(request):
    if request.user.is_authenticated:
        user = request.user
        if request.method =="POST":
            form= TodoForm(request.POST)
            if form.is_valid():
                form = form.save(commit=False)
                form.user = user
                form.save()
                return redirect('/')


def signout(request):
    logout(request)
    return redirect('/login')


def delete(request,id):
    Todo.objects.filter(id=id).delete()
    return redirect('/')

def update(request,id):
    todo = Todo.objects.get(id=id)
    if request.method=="POST":
        form = TodoForm(request.POST,instance=todo)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request,'app/update.html',{'todo':todo})
