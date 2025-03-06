from django.urls import path
from . import views
from .views import IndexView, add, delete, update 

app_name='todos'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:todo_id>/delete', views.delete, name='delete'),
    path('<int:todo_id>/update', views.update, name='update'),
    path('edit/<int:todo_id>/', update, name='edit'),
    path('add/', views.add, name='add')
]

