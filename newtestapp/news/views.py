from django.shortcuts import render
from .models import Articles

def news_home(request):
    news = Articles.objects.order_by('-date').all()
    data = {
        'title':'Novosti na saite',
        'news':news
    }
    return render(request, 'news/news_home.html', data)

def create(request):
    return render(request, 'news/create.html')
