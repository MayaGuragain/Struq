from django.shortcuts import render

def pq_view(request):
    return render(request, 'playground/pq.html')
