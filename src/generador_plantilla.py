# -*- coding:utf-8 -*-
from __future__ import unicode_literals
from os import mkdir
from os.path import dirname, join, exists
from jinja2 import Environment, FileSystemLoader
from gen_mod import obtener_metamodelo, obtener_modelo

def obtener_raiz():
	return dirname(dirname(__file__))

def preparar_jinja():
	return Environment(
		loader=FileSystemLoader(obtener_raiz()),
		trim_blocks=True,
		lstrip_blocks=True
	)

def main():
	metamodelo = obtener_metamodelo()
	modelo = obtener_modelo(metamodelo)
	jinja_env = preparar_jinja()
	plantilla = jinja_env.get_template(join(obtener_raiz(), "/modelos/plantilla.txt"))
	carpeta = join(obtener_raiz(), "cartas")
	
	if not exists(carpeta):
		mkdir(carpeta)
	
	for carta in modelo.cartas:
		with open(join(carpeta, carta.nombre + ".txt"), 'w') as f:
			f.write(plantilla.render(carta=carta))
			print carta.nombre, "ok"

if __name__ == '__main__':
	main()