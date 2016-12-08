#from __future__ import unicode_literals
from subprocess import call
from textx.metamodel import metamodel_from_file
from textx.export import metamodel_export, model_export

class OtroTipo(object):
	
	def __init__(self, parent, nombre):
		self.parent = parent
		self.nombre = nombre
		
	def __str__(self):
		return self.nombre

def obtener_metamodelo():
	archivo = "modelo.tx"

	metamodelo = metamodel_from_file(archivo)
	metamodel_export(metamodelo, archivo + ".dot")
	call("dot -Tpng -O " + archivo + ".dot")
	return metamodelo

def obtener_modelo(metamodelo):
	archivo = "objetos.ttx"
	modelo = metamodelo.model_from_file(archivo)
	model_export(modelo, archivo + ".dot")
	call("dot -Tpng -O " + archivo + ".dot")
	return modelo

if __name__ == '__main__':
	meta = obtener_metamodelo()
	mod = obtener_modelo(meta)
	
