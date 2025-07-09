from django.shortcuts import render

def dlinked_list_view(request):
    return render(request, 'playground/dlinked_list.html')
