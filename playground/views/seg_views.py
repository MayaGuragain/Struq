from django.shortcuts import render

def seg_view(request):
    return render(request, 'playground/seg.html')
