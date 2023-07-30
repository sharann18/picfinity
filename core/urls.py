from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('home/',views.index,name='index'),
    path('signup/',views.signup,name='signup'),
    path('signin/',views.signin,name='signin'),
    path('logout/',views.logout,name='logout'),
    path('settings/',views.settings,name='settings'),
    path('upload/',views.upload,name='upload'),
    path('like-post/',views.like_post,name='like-post'),
    path('profile/<str:pk>',views.profile,name='profile'),
    path('follow/',views.follow,name='follow'),
    path('profile-image/<str:pk>',views.profile_image,name='profile-image'),
    path('del-post/<str:pk>',views.del_post,name='del-post'),
    path('search/',views.search,name='search'),
    path('home/search/',views.search,name='search'),
]
