from django.shortcuts import render
from django.http import HttpResponse
import os
import sys
sys.path.append('./engine')
import Search_engine
engine = Search_engine.Search_engine()

def index(request):
    return render(request, 'search_web/index.html')

def search(request):
    if request.method == 'GET':
        query = request.GET.get('query')
        # svd = request.GET.get('svd')
        # results = [os.getcwd()]
        if query:
            results = engine.search(query)
        else:
            results = []

        context = {
            'query': query,
            'results': results,
        }
        return render(request, 'search_web/search_results.html', context)

    return HttpResponse("Method not allowed")


