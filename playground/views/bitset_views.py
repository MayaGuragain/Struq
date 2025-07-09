from django.shortcuts import render

def bitset_view(request):
    return render(request, 'playground/bitset.html')
