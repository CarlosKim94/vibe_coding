from django.shortcuts import render, get_object_or_404, redirect
from .models import Todo
from .forms import TodoForm

def index(request):
    todos = Todo.objects.order_by("-created_at")
    return render(request, "todo/index.html", {"todos": todos})

def detail(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    return render(request, "todo/detail.html", {"todo": todo})

def create_todo(request):
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("todo_index")
    else:
        form = TodoForm()
    return render(request, "todo/form.html", {"form": form, "title": "Create TODO"})

def edit_todo(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    if request.method == "POST":
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect("todo_index")
    else:
        form = TodoForm(instance=todo)
    return render(request, "todo/form.html", {"form": form, "title": "Edit TODO"})

def delete_todo(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    if request.method == "POST":
        todo.delete()
        return redirect("todo_index")
    return render(request, "todo/confirm_delete.html", {"todo": todo})

def toggle_resolved(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    todo.resolved = not todo.resolved
    todo.save()
    return redirect("todo_index")
