from django.shortcuts import render

def disjointset_view(request):
    return render(request, 'playground/disjointset.html')
