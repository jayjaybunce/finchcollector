from django.urls import path
from . import views

app_name='finches'
urlpatterns = [
    path('', views.home, name='home'),
    path('finches/', views.finches_index, name='index'),
    path('finches/<int:finch_id>/', views.finches_detail, name='detail'),
    path('finches/<int:finch_id>/update', views.update_finch, name='update_finch'),
    path('finches/<int:finch_id>/delete', views.delete_finch, name='delete_finch'),
    path('finches/new', views.new_finch, name='new_finch'),
]