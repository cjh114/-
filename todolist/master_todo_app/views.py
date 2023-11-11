from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import *

# Create your views here.
def index(request) :
  todos = TODO.objects.all()
  content = {"todos" : todos }
  return render(request, 'master_todo_app/index.html', content)

def createtodo(request) :
  inputs = request.POST['todoContent']
  new_todo = TODO(content = inputs)
  new_todo.save()
  return HttpResponseRedirect(reverse('index'))

# 삭제 기능을 가진 View 함수
def deletetodo(request) :
  delete_todo_id = request.GET['todoNum']
  print( "삭제할 TODO ID : ", delete_todo_id )
  todo = TODO.objects.get( id = delete_todo_id )
  todo.delete()
  return HttpResponseRedirect( reverse('index') )

