from unicodedata import name
from django.urls import path
from .views import HomeView, WriteupDetailView, AddPostView, UpdatePostView, DeletePostView, AddCategoryView
from .import views
urlpatterns = [
#  path('', views.home, name='home'),
    path('', HomeView.as_view(), name='home'),
    path('writeup/<int:pk>', WriteupDetailView.as_view(), name='writeup_detail'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('add_category/', AddCategoryView.as_view(), name='add_category'),
    path('writeup/edit/<int:pk>', UpdatePostView.as_view(), name ='update_post'),
    path('writeup/<int:pk>/delete', DeletePostView.as_view(), name ='delete_post'),
    path("contact", views.contact, name="contact"),
    path("about", views.about, name="about"),
    #path('like/<int:pk>', LikeView , name='like_post'),

    
]
