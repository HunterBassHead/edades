# -*- coding: utf-8 -*-
class Edades:
	def mensaje(self, edad):
		if edad <0:
			return "no existes"
		elif edad < 12 and edad > 0:
			return u"eres niño"
		elif edad <18 and edad >12:
			return u"eres adolescente"
		elif edad <65 and edad >18:
			return u"eres adulto"
		elif edad <120 and edad >65:
			return u"eres adulto mayor"
		elif edad > 120 :
			return u"eres mumm-ra"