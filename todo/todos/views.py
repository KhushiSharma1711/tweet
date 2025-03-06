from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.http import HttpResponseBadRequest
from .models import Todo

# List all todos
class IndexView(generic.ListView):
    template_name = 'index.html'
    context_object_name = 'todo_list'

    def get_queryset(self):
        """Return all todos, ordered by latest created."""
        return Todo.objects.order_by('-created_at')

# Add a new todo
def add(request):
    if request.method == 'POST':
        title = request.POST.get('title', '').strip()
        if title:
            Todo.objects.create(title=title)
            return redirect('todos:index')
        return HttpResponseBadRequest("Title cannot be empty")
    return redirect('todos:index')

# Delete a todo
def delete(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)
    todo.delete()
    return redirect('todos:index')

# Update a todo
def update(request, todo_id):
    if request.method == 'POST':
        todo = get_object_or_404(Todo, pk=todo_id)
        todo.isCompleted = bool(request.POST.get('isCompleted'))
        todo.save()
    return redirect('todos:index')
