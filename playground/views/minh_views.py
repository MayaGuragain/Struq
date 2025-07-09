from django.shortcuts import render

def minh_view(request):
    return render(request, 'playground/minh.html')
