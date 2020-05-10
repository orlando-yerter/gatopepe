from django.http import HttpResponse
import datetime 
from django.template import Template,Context

class persona(object):
	def __init__(self,nombre,apellido):
	   self.nombre=nombre
	   self.apellido=apellido
	   
	


def saludo(request):
	
	p1=persona("profesor juan","Diaz")
	
	nombre="juan"
	ahora=datetime.datetime.now()
	
	doc_externo=open("/home/orlando/gatopepe/gatopepe/plantillas/miplantilla.html" )
	
	plt=Template(doc_externo.read())
	doc_externo.close()
	
	ctx=Context({"nombre_persona":nombre})
	
	#ctx=Context({"nombre_persona":"juan","apellido_persona":"diaz","momento_actual":ahora})
	#ctx=Context({"nombre_persona":p1.nombre,"apellido_persona":p1.apellido,"momento_actual":ahora})
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
	
	
		
