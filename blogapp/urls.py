from django.urls import path, include
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path("login/", cuslogin, name='login'),
    path("register/", register, name='register'),
    path('blog/', HomeView.as_view(), name='index'),
    path('logout/', logout_view, name='logout'),
    path('article/<slug:slug>', ArticleDetail.as_view(), name='article_detail'),
    path('add_post/', AddPost.as_view(), name='add_post'),
    path('article/edit/<int:pk>', UpdatePost.as_view(), name='update_post'),
    path('article/<int:pk>/delete', DeletePost.as_view(), name='delete_post'),
   
]

