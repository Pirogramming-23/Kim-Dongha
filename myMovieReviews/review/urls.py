from django.urls import path
from . import views

urlpatterns = [
    path('', views.review_main, name='review_main'),
    path('post/<int:pk>/', views.review_detail, name='review_detail'),
    path('post/new', views.review_new, name='review_new'),
    path('post/<int:pk>/edit/', views.review_edit, name='review_edit'),
    path('post/<int:pk>/delete/', views.review_delete, name='review_delete'),
]