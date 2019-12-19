from django.shortcuts import render, redirect
from .models import Todo

# Create your views here.
def list_todos(request):
    todos = Todo.objects.all()

    context = {
        'todos': todos,
    }
    return render(request, 'todos/list.html', context)

def add_todo(request):
    if(request.method == 'GET'):
        # sends user to create.html to add task
        return render(request, 'todos/create.html')
    elif(request.method == 'POST'):
        # else posts task to list DB
        #  - THIS CREATES NEW POST, THIS IS LIKE USING save()
        new_todo = Todo.objects.create(
            title = request.POST['title'],
            text = request.POST['text'],
            status = request.POST['status'],
        )
        new_todo.save()
        # returns to list page
    return redirect('list')

def remove_todo(request):
    pass

def update(request, id):
    pass

def mark(request, id):
    a_todo = Todo.objects.get(id = id)
    a_todo.status=True
    print("HHHHHHHHHHHHHHHHHHHHHEDSADJKSDJASDJAKLSDHJLDHSJADJSAJHKSADJSDALJHKASDJK")
    a_todo.save()
    return redirect('list')

def detail(request, id):
    a_todo = Todo.objects.get(id = id)
    context = {
        'todo': a_todo
    }

    return render(request, 'todos/detail.html', context)
