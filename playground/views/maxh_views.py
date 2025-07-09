from django.shortcuts import render

def maxh_view(request):
    return render(request, 'playground/maxh.html')
