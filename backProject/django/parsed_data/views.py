from django.shortcuts import render
from django.http import HttpResponse
from .models import schoolData
from .models import blogData
from .models import newsData

def s_list(request):
    s_list = schoolData.objects.order_by('-publishedDate')
    context = {'s_list':s_list}
    return render(request, 'parsed_data/s_list.html', context)
def s_detail(request, s_id):
    s = schoolData.objects.get(id=s_id)
    context = {'s':s}
    return render(request, 'parsed_data/s_detail.html', context)

def b_list(request):
    b_list = blogData.objects.order_by('-publishedDate')
    context = {'b_list':b_list}
    return render(request, 'parsed_data/b_list.html', context)
def b_detail(request, b_id):
    b = blogData.objects.get(id=b_id)
    context = {'b':b}
    return render(request, 'parsed_data/b_detail.html', context)

def n_list(request):
    n_list = newsData.objects.order_by('-id')
    context = {'n_list':n_list}
    return render(request, 'parsed_data/n_list.html', context)
def n_detail(request, n_id):
    n = newsData.objects.get(id=n_id)
    context = {'n':n}
    return render(request, 'parsed_data/n_detail.html', context)