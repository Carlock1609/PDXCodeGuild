from django.shortcuts import render, redirect
from .models import Todo

# Create your views here.
def list_todos(request):
    # todos = Todo.objects.filter(user = request.user) # 
    todos = Todo.objects.all()

    context = {
        'todos': todos,
    }
    return render(request, 'todos/list.html', context)

def add_todo(request):
    if(request.method == 'GET'):
        # sends user to create.html to add task
        return render(request, 'todos/create.html')
    if(request.method == 'POST'):
        # else posts task to list DB
        #  - THIS CREATES NEW POST, THIS IS LIKE USING save()
        new_todo = Todo.objects.create(
            title = request.POST['title'],
            text = request.POST['text'],
            status = request.POST['status'],
            # user = request.user # MUST ADD IF YOU WANT TO HAD LIST FOR
        )
        new_todo.save()
        # returns to list page
        return redirect('list')

def remove_todo(request, id):
    a_todo = Todo.objects.get(id = id)
    a_todo.delete()
    return redirect('list') 

def update(request, id):
    a_todo = Todo.objects.get(id= id)

    if(request.method == 'GET'):
        # else posts task to list DB
        #  - THIS CREATES NEW POST, THIS IS LIKE USING save()
        context = {
            'todo': a_todo,
        }
        # returns to list page
        return render(request, 'todos/update.html', context)
    elif(request.method == 'POST'):
        a_todo.title = request.POST['title']
        a_todo.text = request.POST['text']
        a_todo.status = request.POST['status']
        a_todo.save()
                
        return redirect('list')

def mark(request, id):
    a_todo = Todo.objects.get(id = id)
    a_todo.status=True
    a_todo.save()
    return redirect('list')

def detail(request, id):
    a_todo = Todo.objects.get(id = id)
    context = {
        'todo': a_todo
    }

    return render(request, 'todos/detail.html', context)
