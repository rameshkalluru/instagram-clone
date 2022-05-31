from codecs import namereplace_errors
from django import views
from django.urls import path
from .views import *
urlpatterns=[
    path('home/',homeView.as_view(),name='home'),

    path('post/',CretaePostView.as_view(),name='post'),
    path('post_update/<int:pk>/',UpdatePostView.as_view(),name='post_update'),
    path('post_delete/<int:pk>/',DeletePostView.as_view(),name='post_delete'),
    path('posts/',PostsView.as_view(),name='posts'),


    path('reel/',CreateReelView.as_view(),name='reel'),
    path('update_reel/<int:pk>/',UpdateReelView.as_view(),name='update_reel'),
    path('delete_reel/<int:pk>/',DeleteReelView.as_view(),name='delete_reel'),
    path('reels/',ReelsView.as_view(),name='reels'),



    path('profile_all/',Profileview.as_view(),name='profile_all'),
    path('edit/<int:pk>/',ProfileEditView.as_view(),name='edit'),
    path('detail/<int:pk>/',DetailsView.as_view(),name='detail'),
    path('like/<int:pk>/',LikeView,name='like_post'),
    path('profile_view/',ProfileView,name='Profile'),


    path('search/',search,name='search'),
    path('follow/<int:id>/<str:username>/',follow,name='follow'),
    
    





]