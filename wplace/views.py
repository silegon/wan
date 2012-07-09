#coding:utf-8
from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from wplace.models import Place
from django.http import HttpResponse
from django.core.urlresolvers import reverse
#from django.core.exceptions import ObjectDoesNotExist
import logging

logger = logging.getLogger('develop')

NO_CONTENT = 0
NO_POSITION = 0 

def index(request, template_name='wplace/place_index.html'):
    wplace_list = Place.objects.all()
    context = {
        'wplace_list':wplace_list
    }
    return render_to_response(template_name, context)

def place_detail(request, wplace_id, template_name='wplace/place_detail.html'):
    context = {}
    wplace = Place.objects.get_place(wplace_id)
    if wplace:
        context.update({'wplace':wplace})
        return render_to_response(template_name, context)
    return HttpResponseRedirect(reverse('wplace.views.index'))

def add_place_detail(request, template_name='wplace/edit_place_detail.html'):
    context = {}
    context.update(csrf(request))
    if request.method == "POST":
        p = request.POST
        wplace_title = p.get('wplace-title','')
        wplace_content = p.get('wplace-content','')
        province = p.get('province','')
        city = p.get('city','')
        area = p.get('area','')
        wplace_address = p.get('wplace-address','')
        wplace_position = p.get('wplace-position','')

        wplace = Place.objects.add_place(title=wplace_title, content=wplace_content,
                province=province, city=city, area=area, 
                address=wplace_address, position=wplace_position)

        if wplace:
            context.update({'wplace':wplace})
            return HttpResponseRedirect(reverse('wplace.views.place_detail', 
                                                args=[wplace.id]))

    return render_to_response(template_name, context)

def edit_place_detail(request, wplace_id,
                      template_name='wplace/edit_place_detail.html'):
    context = {
        "edit":True,
    }
    context.update(csrf(request))
    if request.method == "POST":
        p = request.POST
        wplace_title = p.get('wplace-title','')
        wplace_content = p.get('wplace-content','')
        province = p.get('province','')
        city = p.get('city','')
        area = p.get('area','')
        wplace_address = p.get('wplace-address','')
        wplace_position = p.get('wplace-position','')
        hidden_wplace_id = p.get('hidden-wplace-id','')
        if wplace_id == hidden_wplace_id:

            wplace = Place.objects.update_place(id=wplace_id, title=wplace_title,
                    content=wplace_content,
                    province=province, city=city, area=area, 
                    address=wplace_address, position=wplace_position)
            """
            wplace = Place.objects.update_place(id=wplace_id, title=wplace_title,
                    content=wplace_content,
                    province=province, city=city, area=area, 
                    address=wplace_address, position=wplace_position)
                    """

            if wplace:
                context.update({'wplace':wplace})
                return HttpResponseRedirect(reverse('wplace.views.place_detail', 
                                                args=[wplace.id]))
    wplace = Place.objects.get_place(wplace_id)
    if wplace:
        context.update({'wplace':wplace})
        return render_to_response(template_name, context)
    else:
        return HttpResponseRedirect(reverse('wplace.views.index'))


###############################
from django.http import HttpResponseRedirect
from wplace.forms import UploadForm
from django.views.decorators.csrf import csrf_protect
from django.template import RequestContext

@csrf_protect
def upload_file(request):
   if request.method == 'POST':
       form = UploadForm(request.POST, request.FILES)
       if form.is_valid():
           uploaded_file = request.FILES['file']
           chunk = request.REQUEST.get('chunk', '0')
           chunks = request.REQUEST.get('chunks', '0')
           name = request.REQUEST.get('name', '')

           if not name:
               name = uploaded_file.name

           temp_file = '/tmp/insecure.tmp'
           with open(temp_file, ('wb' if chunk == '0' else 'ab')) as f:
               for content in uploaded_file.chunks():
                   f.write(content)

           if int(chunk) + 1 >= int(chunks):
               form.save(temp_file, name)

           if request.is_ajax():
               response = HttpResponse('{"jsonrpc" : "2.0", "result" : null, "id" : "id"}', mimetype='text/plain; charset=UTF-8')
               response['Expires'] = 'Mon, 1 Jan 2000 01:00:00 GMT'
               response['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0'
               response['Pragma'] = 'no-cache'
               return response
           else:
               return HttpResponseRedirect(reverse('wplace.views.upload_file'))
   else:
       form = UploadForm()

   return render_to_response('wplace/upload_file.html', {'form': form}, context_instance=RequestContext(request))

############################
