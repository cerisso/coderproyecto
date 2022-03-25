from distutils.errors import DistutilsClassError
from re import template
from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context, loader

def primer_vista(request):
    return HttpResponse("hola mundo")

def segunda_vista(request):
    return HttpResponse("<h1>Titulo 1</h1><p> Esto es un parrafo </p>")

def dia_hora(request):
    fecha_hora = datetime.now()
    return HttpResponse (f"<p> tiempo actual {fecha_hora}</p>")

def nombre_usuario(request, nombre):
    return HttpResponse(f"tu nombre es {nombre}")

def edad_usuario(request, edad):
    anio_nacimiento = 2022 - int(edad)
    return HttpResponse (f"usted nacio en el {anio_nacimiento}")

def pagina_inicio (request):
    archivo = open(r"C:\Users\crist\OneDrive\Desktop\Coderhouse\Clase django\coder_proyecto\coder_proyecto\templates\page.html","r")
   
    nombre = "Cristian"
    apellido = "Risso"
    fecha_hora = datetime.now()

    listado_calificaciones = [10, 9, 6 ]

    Dic_context = {"nombre": nombre, "apellido": apellido, "fecha_hora": fecha_hora, "calificaciones": listado_calificaciones}
   
   
    plantilla = Template(archivo.read())

    archivo.close()

    context = Context(Dic_context)

    documento = plantilla.render(context)    

    return HttpResponse(documento)

#def pagina_inicio(request):

    nombre = "Cristian"
    apellido = "Risso"
    fecha_hora = datetime.now()

    listado_calificaciones = [10, 9, 6 ]

    dic_context = {"nombre": nombre, "apellido": apellido, "fecha_hora": fecha_hora, "calificaciones": listado_calificaciones}
    plantilla = loader.get_template("page.html")

    documento = plantilla.render(dic_context)

    return HttpResponse(documento)