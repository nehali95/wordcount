from django.http import HttpResponse
from django.shortcuts import render
import operator
def homepage(request):
    return render(request,'home.html' )

def count(request):
    data = request.GET['fulltextarea']
    word_list = data.split()
    list_len = len(word_list)
    word_dict = {}

    for word in word_list:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1
    sorted_list = sorted(word_dict.items() , key = operator.itemgetter(1) , reverse=True)
    return render(request,'count.html',{'fulltext':data, 'words': list_len , 'SameWords': sorted_list})

def aboutpage(request):
    return render (request , 'about.html')
