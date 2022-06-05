from django.shortcuts import render
import random


# Create your views here.
def index (request):
    return render(request, 'index.html')

def dinner(request, name):#url에 표기하기로 한 name이 여기로 들어와서
    menus = [{"name":'족발', "price":30000}, {"name":'햄버거', "price":5000}, {"name":'치킨', "price":20000}, {"name":'초밥', "price":15000}]
    pick = random.choice(menus)
    context = {
        'pick': pick,
        'name': name,#여기에 담겨서
        'menus': menus,
    }
    return render(request, 'dinner.html', context)#context에 포함되 html에 표기되는 것

  
    
      
        