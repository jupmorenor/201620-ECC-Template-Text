from __future__ import unicode_literals
from subprocess import call
from textx.metamodel import metamodel_from_file
from textx.export import metamodel_export, model_export

def obtener_metamodelo():
	archivo = "../modelos/modelo.tx"

	metamodelo = metamodel_from_file(archivo)
	metamodel_export(metamodelo, archivo + ".dot")
	call("dot -Tpng -O " + archivo + ".dot")
	return metamodelo

def obtener_modelo(metamodelo):
	archivo = "../modelos/objetos.ttx"
	modelo = metamodelo.model_from_file(archivo)
	model_export(modelo, archivo + ".dot")
	call("dot -Tpng -O " + archivo + ".dot")
	return modelo

if __name__ == '__main__':
	meta = obtener_metamodelo()
	mod = obtener_modelo(meta)
	
