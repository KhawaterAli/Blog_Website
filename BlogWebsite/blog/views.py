from django.http import HttpResponse
from django.template import loader
from .models import Member
from .models import Post
from .models import Comment
from .models import Category


def user(request):
  user_list = Member.objects.all().values()
  template = loader.get_template('users.html')
  context = {
    'user': user_list,
  }
  return HttpResponse(template.render(context, request))

def blogtitles(request):
  title = Post.objects.all().values()
  template = loader.get_template('blogs.html')
  context = {
    'Blog title': title,
  }
  return HttpResponse(template.render(context, request))

def comments(request):
  comment = Comment.objects.all().values()
  template = loader.get_template('comments.html')
  context = {
    'mycomment': comment,
  }
  return HttpResponse(template.render(context, request))

def categories(request):
  mycategory = Category.objects.all().values()
  template = loader.get_template('categories.html')
  context = {
    'mycategory': mycategory,
  }
  return HttpResponse(template.render(context, request))

def blogdetails(request, ID):
  blogdetails = Post.objects.get(ID=ID)
  template = loader.get_template('blogdetails.html')
  context = {
    'blogdetails': blogdetails,
  }
  return HttpResponse(template.render(context, request))



def main(request):
  template = loader.get_template('index.html')
  return HttpResponse(template.render())