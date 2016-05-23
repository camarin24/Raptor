#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json, sys, cocomo # PELIGRO -- no borrar ##COCOMO##

def insertUser():
	_result = cocomo.query("CALL insertUser ( '" + _POST['id'] + "' )")
	cocomo.printJson(_result, "success")

def insertFAQ():
	_result = cocomo.execute("CALL insertFaq ( " + _POST['id_user'] + " , '" + _POST['comentario'] + "' )")
	cocomo.printJson("Done", "success")
	
def getDownloadUser():
	_result = cocomo.query("CALL getDownloaUser ( " + _POST['id_user'] + " )")
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