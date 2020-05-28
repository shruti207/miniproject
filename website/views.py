
from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages

from .models import TodoList

# Create your views 

    

def todolist(request):
    if request.method =="POST":
        
        if request.POST.get('content'):
            x = TodoList()
            x.content = request.POST.get("content")
            x.save()
            list_item = TodoList.objects.all()
            messages.success(request,"item added")
            return render(request,"todolist.html",{'list_item':list_item})
            
    else:
        list_item = TodoList.objects.all()
        return render(request,"todolist.html",{'list_item':list_item})
    

def delete(request,list_id):
    item = TodoList.objects.get(id = list_id)
    item.delete()
    messages.success(request,"item deleted")
    #return HttpResponseRedirect("/todolist/")
    return redirect("http://localhost:8000/todolist/")

def cross(request, list_id):
    item = TodoList.objects.get(id=list_id)
    item.completed = True
    item.save()
    return redirect("http://localhost:8000/todolist/")

def uncross(request, list_id):
    item = TodoList.objects.get(id =list_id)
    item.completed = False
    item.save()
    return redirect("http://localhost:8000/todolist/")
