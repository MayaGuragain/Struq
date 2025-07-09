from django.shortcuts import render

def redblack_view(request):
    return render(request, 'playground/redblack.html')
