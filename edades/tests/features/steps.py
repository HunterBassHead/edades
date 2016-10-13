# -*- coding: utf-8 -*-
from lettuce import step, world
from edades import Edades


@step(u'cuando consulto mi mensaje')
def cuando_consulto_mi_mensaje(step):
	pass


@step(u'Dado que ingreso la edad "([^"]*)"')
def dado_que_ingreso_la_edad_group1(step, edad1):
   edad = Edades()
   world.mensaje = edad.mensaje(int(edad1))

@step(u'entonces veo "([^"]*)"')
def entonces_veo_group1(step, mensaje_esperado):
    assert world.mensaje == mensaje_esperado, \
    'mensaje esperado ' +mensaje_esperado+' y se obtuvo'+world.mensaje

