from django.shortcuts import render

# Create your views here.
def boxmodel(request):
    return render(request,'boxmodel.html')

def form(request):
    return render(request,'form.html')

def hypertext(request):
    return render(request,'hypertext.html')

def table(request):
    return render(request,'table.html')