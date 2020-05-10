#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 23:38:00 2020

@author: orlando
"""

from django.http import HttpResponse
import datetime 
from django.template import Template,Context



class persona(object):
	def __init__(self,nombre,apellido):
	   self.nombre=nombre
	   self.apellido=apellido



def saludo(recuest):
    #return HttpResponse("ej1 con git simple texto hola")
    
    doc_externo=open("/home/orlando/gatopepe/ej1/plantillas/miplantilla.html" )
    plt=Template(doc_externo.read())
    doc_externo.close()
    ctx=Context()
    documento=plt.render(ctx)
    #documento=doc_externo.render({"nombre_persona":p1.nombre,"apellido_persona":p1.apellido,"momento_actual":ahora})
    return HttpResponse(documento)

def saludo2(recuest): # ej video 6 
    #return HttpResponse("ej1 con git simple texto hola")
    nombre="juan"
    ahora=datetime.datetime.now()
    
    doc_externo=open("/home/orlando/gatopepe/ej1/plantillas/miplantilla2.html" )
    plt=Template(doc_externo.read())
    doc_externo.close()
    ctx=Context({"nombre_persona":nombre,"momento_actual":ahora})
    documento=plt.render(ctx)
    #documento=doc_externo.render({"momento_actual":ahora})
    return HttpResponse(documento)
    
def saludo3(recuest): # ej video 6 poo
    ahora=datetime.datetime.now()
    p1=persona("profesor juan","Diaz")
    doc_externo=open("/home/orlando/gatopepe/ej1/plantillas/miplantilla3.html" )
    plt=Template(doc_externo.read())
    doc_externo.close()
    ctx=Context({"nombre_persona":p1.nombre,"apellido_persona":p1.apellido,"momento_actual":ahora})
    documento=plt.render(ctx)
    return HttpResponse(documento)    

    
def ver_fecha(request):
	fecha_actual=datetime.datetime.now()
	documento="""<html>
	<body> 
	<h1>
	fecha y hora actuales %s
	</h1>
	</body> 
	</html>""" % fecha_actual
	return HttpResponse(documento)
