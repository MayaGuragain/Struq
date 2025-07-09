from django.shortcuts import render

def rope_view(request):
    return render(request, 'playground/rope.html')
