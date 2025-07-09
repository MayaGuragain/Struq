from django.shortcuts import render

def tup_view(request):
    return render(request, 'playground/tup.html')
