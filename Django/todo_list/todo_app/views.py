from django.shortcuts import render
from .models import Todo

# Create your views here.
def list_todos(request):
    todos = Todo.objects.all()

    context = {
        'todos': todos,
    }
    return render(request, 'todos/list.html', context)

def  add_todo(request):
    if(request.method == 'GET'):
        return render(request, 'todos/create.html')
    elif(request.method == 'POST'):
        #  - THIS CREATES NEW POST, THIS IS LIKE USING save()
        new_todo = Todo.objects.create(
            title = request.POST['title']
            text = request.POST['text']
            status = request.POST['status']
        )
    return redirect('list')

def remove_todo(request):
    pass

def update(request, id):
    pass

def mark(request, id):
    pass

def detail(request, id):
    a_todo = Todo.objects.get(id = id)
    context = {
        'todo': a_todo
    }

    return render(request, 'todos/detail.html', context)
