from django.shortcuts import render

def bt_view(request):
    return render(request, 'playground/bt.html')
