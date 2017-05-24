# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from .models import SystemIP
from django.conf import settings
from django.shortcuts import render
from django.views.generic.detail import DetailView

from django.db.models import Q
from django.shortcuts import render_to_response

# Create your views here.

def home(request):
    return render(request, 'index.html')

def updates(request):
    return render(request, 'updates.html')

def info(request):
    return render(request, 'info.html')


################
#Busqueda
def busqueda(request):
    query = request.GET.get('q', '')
    if query:
        qset = (
            Q(nombre__icontains=query) |
            Q(ipv4__icontains=query)
        )
        results = SystemIP.objects.filter(qset).distinct()
    else:
        results = []
    return render_to_response("ip.html", {
        "results": results,
        "query": query
    })

