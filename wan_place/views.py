#coding:utf-8
from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from wan_place.models import Address, wanPosition, wanPlace, Content
from django.http import HttpResponse

import logging

logger = logging.getLogger('develop')

def index(request, template_name='wan_place/place_index.html'):
    return render_to_response(template_name)

def place_detail(request, template_name='wan_place/place_detail.html'):
    return render_to_response(template_name)

def add_place_detail(request, template_name='wan_place/edit_place_detail.html'):
    context = {}
    context.update(csrf(request))
    if request.method == "POST":
        p = request.POST
        article_title = p['article-title']
        article_content = p['article-content']
        article_address = p['article-address']
        article_position = p['article-position']
        content = Content(content=article_content)
        content.save()
        address = Address(address=article_address)
        address.save()
        position = wanPosition(gps_position=article_position, address_id=address.id)
        position.save()
        wan_place = wanPlace(title=article_title, wan_position_id=position.id, 
                             content_id=content.id)
        wan_place.save()

        return HttpResponse('OK')

    else:
        return render_to_response(template_name, context)

def edit_place_detail(request,
                      template_name='wan_place/edit_place_detail.html'):
    return render_to_response(template_name)

