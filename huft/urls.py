from django.urls import path
from . import views

urlpatterns = [
    path('', views.blogs, name="blogs"),
    path('blog-single/', views.blog_single, name="blog_single")
]
