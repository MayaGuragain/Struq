from django.shortcuts import render

def ht_view(request):
    return render(request, 'playground/ht.html')
