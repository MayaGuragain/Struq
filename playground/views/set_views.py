from django.shortcuts import render

def set_view(request):
    return render(request, 'playground/set.html')
