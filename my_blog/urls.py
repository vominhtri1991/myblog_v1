from django.urls import path, include
from . import views
app_name='my_blog'
urlpatterns = [
   
    path('',views.myblog,name='myblog'),
    path('about/',views.about,name='about'),
    path('post/<int:blog_id>/',views.post,name='post'),
    path('contact/',views.contact,name='contact'),
    path('nav/',views.nav,name='nav'),
]