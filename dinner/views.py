# -*- coding: utf-8 -*-
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.core.context_processors import csrf
from django.contrib.auth import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import *

#first_page,login
def first_page(request):
    if request.POST:
                username = password = ''
                username = request.POST.get('inputName')
                password = request.POST.get('inputPassword')
                user     = authenticate(username=username, password=password)
                if user is not None and user.is_active:
                    login(request,user)
                    return redirect('/dinner/index')
    ctx = {}
    ctx.update(csrf(request))
    return render(request, 'login.html',ctx)
    
# def dinner_register(request):
#     if request.method == 'POST': 
#         user = UserCreationForm()
#         user.Meta.fields = request.POST.get('username')
#         user.password1 = request.POST.get('password')
#         user.password2 = request.POST.get('password')
#         userInfo = authenticate(username=request.POST.get('username'), password=request.POST.get('password'))
#         if userInfo.
#         if user.is_valid():
#             new_user = User.objects.create_user(request.POST['username'], request.POST['password'])  
#             new_user.save()
#             return redirect("/dinner/")
#         else:
#             return redirect("/dinner/register")
#     else:
#         ctx = {}
#         ctx.update(csrf(request))       
#         return render(request, "register.html", ctx)
    
def dinner_register(request):
    if request.method == 'POST': 
        form = UserCreationForm(request.POST) 
        if form.is_valid(): 
            new_user = form.save() 
        return redirect("/") 
    else:
        form = UserCreationForm()
        ctx = {'form': form}
        ctx.update(csrf(request))
        return render(request, "register.html", ctx)
    
    