from django.shortcuts import render

def matrix_view(request):
    return render(request, 'playground/matrix.html')
