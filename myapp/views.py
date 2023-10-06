
from django.shortcuts import render,redirect
from .models import *

def insert(request):
    if request.method=='POST':
        data=request.POST
        name=data.get('name')
        email=data.get('email')
        password=data.get('password')
        user=User.objects.create(
            name=name,
            email=email,
            password=password,
        )

    users=User.objects.all()

    return render(request,'myapp/add.html',context={'users': users}) 


def user_delete(request,id):
      user=User.objects.get(id=id)
      user.delete()
      return redirect('/')


def update_user(request,id):
    u=User.objects.get(id=id)
    if request.method=='POST':
          name=request.POST.get('name')
          email=request.POST.get('email')
          password=request.POST.get('password')

          u.name=name
          u.email=email
          u.password=password
          u.save()
          return redirect('/')

    return render(request,'myapp/update.html',context={'u':u})
