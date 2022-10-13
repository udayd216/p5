from django.shortcuts import render

# Create your views here.
def app_uday(request):
    a={'name':'udaykumar'}
    return render(request,'app.html',a)