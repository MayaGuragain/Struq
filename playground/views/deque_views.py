from django.shortcuts import render

def deque_view(request):
    return render(request, 'playground/deque.html')
