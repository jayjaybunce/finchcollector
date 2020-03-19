from django.urls import path
from . import views

app_name='finches'
urlpatterns = [
    path('', views.home, name='home'),
    path('finches/', views.finches_index, name='index'),
    path('finches/<int:finch_id>/', views.finches_detail, name='detail'),
    path('finches/<int:pk>/update', views.FinchUpdate.as_view(), name='update_finch'),
    path('finches/<int:finch_id>/feedings', views.add_feeding, name='add_feeding'),
    path('finches/<int:finch_id>/toys/add/<int:toy_id>/', views.finch_add_toy, name='finch_add_toy'),
    path('finches/<int:finch_id>/toys/remove/<int:toy_id>/', views.finch_remove_toy, name='finch_remove_toy'),
    path('finches/<int:pk>/delete', views.FinchDelete.as_view(), name='delete_finch'),
    path('finches/new', views.FinchCreate.as_view(), name='new_finch'),
    path('toys/', views.toys_index, name='toys_index'),
    path('toys/new', views.add_toy, name='add_toy'),
    path('accounts/signup/', views.signup, name='signup'),
    

]