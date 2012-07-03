#coding:utf-8
from django.shortcuts import render_to_response

def index(request, template_name='wan_place/index.html'):
    return render_to_response(template_name)

