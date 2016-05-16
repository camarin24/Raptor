#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json, sys, cocomo # PELIGRO -- no borrar ##COCOMO##

# def login():
# 	__object = _POST	
# 	__data = cocomo.query("select * from user where email = '"+__object['user']+"' and pass = '"+__object['password']+"'")
# 	if len(__data) == 0:
# 		cocomo.printJson("Datos no encontrados", "error")
# 	else:
# 		cocomo.printJson(__data, "success")


def insertUser():
	_result = cocomo.query("CALL insertUser ( '" + _POST['id'] + "' )")
	cocomo.printJson(_result, "success")


##COCOMO##COCOMO##COCOMO##COCOMO##COCOMO##COCOMO##COCOMO##COCOMO##COCOMO##COCOMO##COCOMO##
##
## Por favor, no borrar este codigo
## Necesario para el funcionamineto del script dentro del framework
## copie y pege este codigo en cada script que valla a ser utilizado como servicio
_EXECUTE = sys.argv[1] + "()"
_POST = json.loads(sys.argv[2])

def _MAIN():
	try:
		exec _EXECUTE
	except NameError:
		cocomo.printJson("funtion '"+_EXECUTE+"' not found", "error")


if __name__ == "__main__":
	_MAIN()
##
##COCOMO##COCOMO##COCOMO##COCOMO##COCOMO##COCOMO##COCOMO##COCOMO##COCOMO##COCOMO##COCOMO##