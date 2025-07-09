from django.shortcuts import render

def fenwicktree_view(request):
    return render(request, 'playground/fenwicktree.html')
