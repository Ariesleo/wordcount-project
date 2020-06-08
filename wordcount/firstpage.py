from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
    return  render(request, 'home.html')


def admin(request):
    fulltext = request.GET['fulltext']
    #full = request.GET['full']
    
    sepword = fulltext.split()
    totalword = len(sepword)

    dictwords = {}
    #sortval = dictwords.sort()
    for word in sepword:
        if word != '--':
            if word in dictwords:
                dictwords[word] += 1
            else:
                dictwords[word] = 1
        else:
            continue

    sortedwords = sorted(dictwords.items(), key=operator.itemgetter(1), reverse=True)
   
    return render(request, 'view.html', {'fulltext': fulltext, 'totalword':totalword, 'displaydata':sortedwords})