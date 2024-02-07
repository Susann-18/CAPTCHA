# myapp/views.py
from django.shortcuts import render

from django.shortcuts import render,redirect
from.forms import MyForm
from django.http import HttpResponse

def index(request):
    form=MyForm
    return render(request,'base.html',{'form':form})


from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .forms import MyForm  # Make sure to import your form

def submit(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['fullname']
            email = form.cleaned_data['email']
            print('success')
            print(name)
            print(email)
            messages.success(request, "Thank you for submitting this form")
            return redirect('index')
        else:
            print('fail')
            messages.error(request, "Form submission failed. Please check the entered data.")

    return redirect('index')

