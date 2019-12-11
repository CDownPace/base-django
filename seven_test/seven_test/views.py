from django.shortcuts import render

def index(request):
    return render(request,'index.html')
def company(request):
    return render(request, 'company.html')

def school(request):
    return render(request, 'school.html')