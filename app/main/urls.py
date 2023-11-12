from django.urls import path
from .import views
from .models import Board, Thread, User, Post
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.index, name="index"),
    path('board<int:id>/', views.index_board, name="index_board"),
    path('thread<int:id>/', views.index_thread, name="index_thread"),
    path('user<str:username>/', views.index_user, name="index_user"),
    path('post_list/', views.index_posts, name="index_posts"),
    path('members_list/', views.index_users, name="index_users"),
    path('prescribed_conditions/', views.terms_and_conditions, name="terms_and_conditions"),
    path('register/', views.register, name="register"),
    path('login/', auth_views.LoginView.as_view(template_name="main/login.html", extra_context={
                                                    'Threads': Thread.objects.all().order_by("Time_Created")[:10]}),
         name="login"),
    path('logout/', auth_views.LogoutView.as_view(next_page='/', extra_context={
                                                    'Threads': Thread.objects.all().order_by("Time_Created")[:10]}),
         name="logout"),
    #path('search/', views.index_post, name="search"),
]