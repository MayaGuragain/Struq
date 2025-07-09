from django.shortcuts import render

def dict_view(request):
    return render(request, 'playground/dict.html')
