from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

def stack_view(request):
    stack = request.session.get('stack', [])
    return render(request, 'playground/stack.html', {'stack': stack})

@csrf_exempt
def push(request):
    if request.method == 'POST':
        stack = request.session.get('stack', [])
        value = request.POST.get('value')
        if value:
            stack.append(value)
            request.session['stack'] = stack
        return JsonResponse({'stack': stack})
    return JsonResponse({'error': 'Invalid method'}, status=400)

@csrf_exempt
def pop(request):
    if request.method == 'POST':
        stack = request.session.get('stack', [])
        if stack:
            popped = stack.pop()
            request.session['stack'] = stack
            return JsonResponse({'popped': popped, 'stack': stack})
        return JsonResponse({'message': 'Stack is empty.'}, status=400)
    return JsonResponse({'error': 'Invalid method'}, status=400)

def peek(request):
    stack = request.session.get('stack', [])
    if stack:
        return JsonResponse({'top': stack[-1]})
    return JsonResponse({'message': 'Stack is empty.'}, status=400)
