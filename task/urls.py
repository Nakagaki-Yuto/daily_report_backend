from django.urls import path
from . import views

urlpatterns = [
    path('', views.ListTask.as_view()), #未完タスク一覧
    path('finished/', views.ListFinishedTask.as_view()), #完了タスク一覧
    
]