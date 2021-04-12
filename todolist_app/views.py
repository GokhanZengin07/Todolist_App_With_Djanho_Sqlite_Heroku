from django.shortcuts import render,redirect
from django.http import HttpResponse
from todolist_app.models import Todolistmodels
from .forms import Todolistform
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def todolist (request): # browserdan herhangi bir sey cagirinca request istiyor
    if request.method =="POST":
        form = Todolistform(request.POST or None)
        if form.is_valid():
            form.save()
        messages.success(request,("New Task Added!"))
        return redirect("todolist")
    else:
        all_tasks=Todolistmodels.objects.all()
        paginator=Paginator(all_tasks,5)
        page=request.GET.get("pg")
        all_tasks=paginator.get_page((page))

    return render(request,"todolist.html",{"all_tasks":all_tasks})

def delete_task(request,task_id):
    task=Todolistmodels.objects.get(pk=task_id)
    task.delete()
    return redirect("todolist")

def edit_task(request,task_id):
    if request.method=="POST":
        task = Todolistmodels.objects.get( pk=task_id )
        form=Todolistform(request.POST or None, instance=task)
        if form.is_valid():
            form.save()

        messages.success(request,("Task Edited!"))
        return redirect("todolist")
    else:
        task_obj = Todolistmodels.objects.get(pk=task_id)

    return render(request,"edit.html",{"task_obj":task_obj})

def complete_task (request,task_id):
    task =Todolistmodels.objects.get( pk=task_id )
    task.done = True
    task.save()
    return redirect("todolist")

def pending_task (request,task_id):
    task =Todolistmodels.objects.get( pk=task_id )
    task.done = False
    task.save()
    return redirect("todolist")


def code (request): # code
    context={
        "code_text":"Welcome To My Coding Journey"
    }
    return render(request,"code.html",context)
@login_required
def diary (request): # code
    context={
        "diary_text":"Welcome To My Diary"
    }
    return render(request,"diary.html",context)

def myenglish(request): # code
    context={
        "myenglish_text":"Welcome To My English Improvement Process"
    }
    return render(request,"myenglish.html",context)

def index(request): # code
    context={
        "index_text":"Welcome To Home Page "
    }
    return render(request,"index.html",context)
