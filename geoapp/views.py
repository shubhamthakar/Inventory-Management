from django.shortcuts import render, redirect

# Create your views here.
def testPage(request):
    return render(request, 'geoapp/index.html', {})