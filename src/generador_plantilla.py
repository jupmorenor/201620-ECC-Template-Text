from os.path import dirname, join
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

def cargar_plantilla(jinja_env, plantilla):
	return jinja_env.get_template(plantilla)