from django.shortcuts import render
from .models import Data


def form(request):
    if request.method == "POST":
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        comment=request.POST['comment']
        print(firstname,lastname,comment)
        data=Data(firstname=firstname,lastname=lastname,comment=comment)
        data.save()



    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def comment(request):
    return render(request,'comments.html')



