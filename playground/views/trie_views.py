from django.shortcuts import render

def trie_view(request):
    return render(request, 'playground/trie.html')
