from django.shortcuts import render
#from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'main4/index.html')

def about(request):
    return render(request, 'main4/about.html')
    #return HttpResponse("<h4>Stranitsa pro nas</h4>")