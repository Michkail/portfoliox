from django.shortcuts import render

def blogs(request):
  return render(request, 'blog.html')

def blog_single(requset):
  return render(requset, 'blog-single.html')