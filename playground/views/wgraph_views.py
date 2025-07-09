from django.shortcuts import render

def wgraph_view(request):
    return render(request, 'playground/wgraph.html')
