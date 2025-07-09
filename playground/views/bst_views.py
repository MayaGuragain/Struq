from django.shortcuts import render

def bst_view(request):
    return render(request, 'playground/bst.html')
