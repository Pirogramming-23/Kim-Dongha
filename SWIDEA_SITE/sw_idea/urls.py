from django.urls import path
from . import views
from .views import signup_view, login_view, logout_view

urlpatterns = [
    path('', views.idea_list, name='idea_list'),
    path('idea/<int:pk>/', views.idea_detail, name='idea_detail'),
    path('idea/new/', views.idea_create, name='idea_create'),
    path('idea/<int:pk>/edit/', views.idea_edit, name='idea_edit'),
    path('idea/<int:pk>/delete/', views.idea_delete, name='idea_delete'),
    path('idea/<int:pk>/toggle_star/', views.toggle_star, name='toggle_star'),
    path('idea/<int:pk>/update_interest/', views.update_interest, name='update_interest'),

    path('devtools/', views.devtool_list, name='devtool_list'),
    path('devtools/<int:pk>/', views.devtool_detail, name='devtool_detail'),
    path('devtools/new/', views.devtool_create, name='devtool_create'),
    path('devtools/<int:pk>/edit/', views.devtool_edit, name='devtool_edit'),
    path('devtools/<int:pk>/delete/', views.devtool_delete, name='devtool_delete'),

    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]
