from django.shortcuts import render,get_object_or_404
from .models import Blog
def myblog(request):
	blogs=Blog.objects.order_by('-date')[:9]
	return render(request,'my_blog/index.html',{'blogs':blogs})

def about(request):
	return render(request,'my_blog/about.html')

def post(request,blog_id):
	blog=get_object_or_404(Blog,pk=blog_id)
	return render(request,'my_blog/post.html',{'blog':blog})

def contact(request):
	return render(request,'my_blog/contact.html')

def nav(request):
	return render(request,'my_blog/base_navg.html')	
# Create your views here.
