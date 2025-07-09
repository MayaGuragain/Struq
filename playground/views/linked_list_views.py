from django.shortcuts import render

def linked_list_view(request):
    return render(request, 'playground/linked_list.html')
