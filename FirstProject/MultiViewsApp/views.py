from django.shortcuts import render
from django.http import HttpResponse;

# Create your views here...

def f1(request):
    return HttpResponse("<h2>Good Morning CHINNI..!!Have a nice day...</h2><hr/>");

def f2 (request):
    return HttpResponse("<h2>Good Afternoon CHINNI..!!Hope you are doing good...</h2><hr/>");
    
def f3 (request):
    return HttpResponse("<h2>Good Evening CHINNI..!! How was ur day...</h2><hr/>");