#from django.shortcuts import render
from django.shortcuts import render, get_object_or_404

def index(request):
    return render(request, 'personal/header.html')

def search_results(request):
    search_key = request.POST.get('search_term')
    #query results text that contains what you typed in
    results = filter(text__contains=search_key)
 
    context = {
        "search_term": search_key,
        "results": results,
    }
 
    return render(request, 'templates/search.html', context)
