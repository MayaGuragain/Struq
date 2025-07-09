from django.shortcuts import render

def cb_view(request):
    return render(request, 'playground/cb.html')
