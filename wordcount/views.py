from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    return render(request, 'home.html', {'pythondata':'Variable daya'})


def homepage2(request):
    return HttpResponse('<H2>Hello 2</H2>')

def count(request):
    fulltext = request.GET['fulltext']
    words = fulltext.split(' ')
    wordscount = len(words)
    return render(request, 'count.html', {'fulltext':wordscount})
