from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
    path('change/', views.to_change, name='change'),
    path('modify/', views.modify, name='modify'),
    path('posting/', views.posting, name='posting'),
    path('showuser/',views.show_user, name='showuser'),
    path('create_plate/', views.create_plate, name='create_plate'),
    path('add_plate/', views.add_plate, name='add_plate'),
    path('create_tag/', views.create_tag, name='create_tag'),
    path('add_tag/', views.add_tag, name='add_tag'),
    path('add_post/', views.add_post, name='add_post'),
    path('show_post/', views.post, name='show_post'),
    path('add_like/', views.add_like, name='add_like'),
    path('reduce_like/', views.reduce_like, name='reduce_like'),
    path('add_review/', views.add_review, name='add_review'),
    path('show_posts/', views.show_posts, name='show_posts'),
    path('dynamic_login', views.dynamic_login, name='dynamic_login'),
]