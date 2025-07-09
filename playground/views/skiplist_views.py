from django.shortcuts import render

def skiplist_view(request):
    return render(request, 'playground/skiplist.html')
