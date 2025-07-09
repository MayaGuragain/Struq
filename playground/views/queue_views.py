from django.shortcuts import render

def queue_view(request):
    return render(request, 'playground/queue.html')
