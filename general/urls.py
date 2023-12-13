from django.urls import path
from . import views


urlpatterns = [
    path('add/', views.ipfs_add, name='ipfs_add'),
    path('cat/<str:ipfs_hash>/', views.ipfs_cat, name='ipfs_cat'),
    path('name/publish/', views.ipfs_publish, name='ipfs_name_publish'),
]