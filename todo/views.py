from django.shortcuts import render, redirect

# Create your views here.
from django.views.decorators.http import require_POST

from .forms import TodoForm
from .models import Todo


def activity(request):
    todo_list = Todo.objects.order_by('id')

    form = TodoForm()

    context = {'todo_list': todo_list, 'form': form}

    return render(request, 'todo/activity.html', context)


@require_POST
def addTodo(request):
    form = TodoForm(request.POST)

    if form.is_valid():
        new_todo = Todo(text=request.POST['text'])
        new_todo.save()

    return redirect('activity')


def completeTodo(request, todo_id):
    todo = Todo.objects.get(pk=todo_id)
    todo.complete = True
    todo.save()

    return redirect('activity')


def deleteCompleted(request):
    Todo.objects.filter(complete__exact=True).delete()

    return redirect('activity')


def deleteAll(request):
    Todo.objects.all().delete()

    return redirect('activity')

