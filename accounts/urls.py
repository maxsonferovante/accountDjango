from django.contrib.auth.views import LogoutView
from django.urls import path


from . import views


urlpatterns = [
    path('', views.LoginCustomView.as_view(next_page='/list-users/'), name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('register/', views.register, name='register'),
    path('check_email/', views.check_email, name='check_email'),
    path('list-users/', views.list_users, name='list_users'),

]
