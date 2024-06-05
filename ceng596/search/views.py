from django.views.generic import View
from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.


class SearchPageView(View):
    url_name = 'doogle_search'

    def get(self, request):
        return render(request, 'doogle_search.html')

    def post(self, request):
        query = request.POST.get('q')
        return redirect('doogle_results', query=query)


class ResultPageView(View):
    url_name = 'doogle_results'

    def get(self, request, query):
        # TODO: get results
        results = [("mahmut", 1), ("xyz", 2)]
        context = {'query': query, 'results': results}
        return render(request, 'doogle_results.html', context)
    
    def post(self, request):
        document_id = request.POST.get('document_id')
        return redirect('doogle_document', document_id=document_id)


class DocumentPageView(View):
    url_name = 'doogle_document'
    def get(self, request, document_id):
        document = f"we re in doc {document_id}"
        return HttpResponse(document)
