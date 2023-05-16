from django.shortcuts import render

# Create your views here.
def portfolio(request):
    return render(request,'portfolio/portfolio.html')

def testimonials(request):
    return render(request,'portfolio/testimonials.html')

def projects(request):
    return render(request,'portfolio/projects.html')
