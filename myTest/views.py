# -*- coding:utf-8 -*-
from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse,Http404
from django.shortcuts import render_to_response
from myTest.forms import *
from django.template import RequestContext
from myTest.models import *


def search_data_baidu_ins(cop_name,product_name):
    try:
        m = baidu_caifu.objects.get(company_name=cop_name,product_name=product_name)
        return unicode(m.product_desc)
    except Exception,e:
        return "sorry, 没找到合适的信息"





def product_search(request):
    if request.method == "POST":
        form = Mybook(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            #print "data",data
            cop_name = data['company_name']
            pro_name = data['product_name']
            #print "title",title
            return HttpResponse(search_data_baidu_ins(cop_name,pro_name))
        else:
            return HttpResponse("抱歉, 没有找到合适的信息! 我们正在努力更新更全的信息")
    form = Mybook()
    return render_to_response("2.html",{'form':form},context_instance=RequestContext(request))

def co_search(request):
    if request.method == "POST":
        form = Mybook(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            #print "data",data
            cop_name = data['company_name']
            pro_name = data['product_name']
            #print "title",title
            return HttpResponse(search_data_baidu_ins(cop_name,pro_name))
        else:
            return HttpResponse("抱歉, 没有找到合适的信息! 我们正在努力更新更全的信息")
    form = Mybook()
    return render_to_response("2.html",{'form':form},context_instance=RequestContext(request))


# def hello1(request, num):
#     try:
#         num = int(num)
#         request._body
#     except ValueError:
#         raise Http404


