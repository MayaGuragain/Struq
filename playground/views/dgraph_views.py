from django.shortcuts import render

def dgraph_view(request):
    return render(request, 'playground/dgraph.html')
