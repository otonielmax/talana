from django.conf import settings
from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template.response import TemplateResponse
from django.template.defaultfilters import slugify
from modules.pets.forms import PetsForm

import hashlib, json, random, math, os

# Create your views here.
def home(request):    
    return render_to_response("pets/index.html")

def create(request):
    form = PetsForm()

    if request.method == 'POST':
        form = PetsForm(request.POST, request.FILES)
    
        if form.is_valid():
            model = form.save(commit=False)

            file_name = save_file(request.FILES['picture'])
            model.picture = file_name[0]
            
            model.name = request.FILES['name']
            model.user = request.FILES['user']
            
            modelo.save()
            
            mensaje_exito = 'El registro se ha agregado exitosamente...'
            request.session['mensaje_flash'] = mensaje_exito
            
            return redirect("admin_archivos") 
        
        else:
            mensaje_error = 'Hay un error con los datos del formulario...'
    return TemplateResponse(
        request, 
        "pets/create.html",
        {
            'form' : form
        }
    )

def save_file(f, name = None):
    #datenow = datetime.now().strftime("%Y%m%d%H%M%S")
    rnd =  random.randint(100000, 999999)
    
    directory = settings.BASE_DIR +  '/static/media/archivos/'
    
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    if name == None:
        
        cantidad_actual = 0
        existe_archivo = True
        while existe_archivo:
            name = f.name.encode('utf-8')            
            extension = slugify(name.lower().split(".")[-1])
            
            if cantidad_actual == 0:
                sufijo_nombre = ''
            else:
                sufijo_nombre = '_' + str(cantidad_actual) 
            
            nombre_archivo_solo = slugify(name.split(".")[0] + sufijo_nombre)
            nombre_archivo = nombre_archivo_solo + '.' + extension
            nombre_archivo_thumb = nombre_archivo_solo + '_thumb.' + extension
            
            if os.path.exists(directory + nombre_archivo):
                cantidad_actual = cantidad_actual + 1
                existe_archivo = True
            else:
                existe_archivo = False
        
    else:
        
        cantidad_actual = 0
        existe_archivo = True
        while existe_archivo:
            name = name.encode('utf-8')
            extension = slugify(name.lower().split(".")[-1])
            
            if cantidad_actual == 0:
                sufijo_nombre = ''
            else:
                sufijo_nombre = '_' + str(cantidad_actual)
            
            nombre_archivo_solo = slugify(name.split(".")[0] + sufijo_nombre)
            nombre_archivo = nombre_archivo_solo + '.' + extension
            nombre_archivo_thumb = nombre_archivo_solo + '_thumb.' + extension
            
            if os.path.exists(directory + nombre_archivo):
                cantidad_actual = cantidad_actual + 1
                existe_archivo = True
            else:
                existe_archivo = False
    
    
    with open(directory + nombre_archivo, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
            
    print("Se guardo")
            
    return nombre_archivo, nombre_archivo_thumb, nombre_archivo_solo