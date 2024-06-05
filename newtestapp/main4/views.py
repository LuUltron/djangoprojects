from django.shortcuts import render
#from django.http import HttpResponse

# Create your views here.
def index(request):
    data = {
        'title': 'Glavnaya stranitsa!!',
        'values': ['some', 'Hello', 123],
        'obj': {
            'car': 'bmw',
            'age': 18,
            'hobby': 'football'
        }
    }
    return render(request, 'main4/index.html', data)

def about(request):
    return render(request, 'main4/about.html')
    #return HttpResponse("<h4>Stranitsa pro nas</h4>")