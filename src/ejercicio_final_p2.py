#!/usr/bin/env python3

""" 
	Autor: Gabriel Reus Rodriguez greus@uoc.edu

	Ejercicio FINAL pregunta 2 del modulo A2 del curso de programacion de python.

	En este ejercicio deberás implementar una función que haga el proceso opuesto, es decir, que
permite desencriptar una cadena previamente encriptada. Para ello debes implementar una función
llamada decrypt(inputValue, keys, token) que reciba una cadena encriptada y realice la
desencriptación. La función recibe tres parámetros:

		● inputValue, que será un string con la cadena encriptada (resultado del proceso anterior).
		● keys, que será un diccionario compuesto por pares donde la clave será una letra y el valor
			correspondiente un número, estos servirán durante la encriptación. Por ejemplo:
			keys = {
				"a" : 1,
				"e" : 2,
				"U" : 3
			}
		● token, que será un carácter que nos permitirá identificar el inicio y fin de una letra
			encriptada. Así mismo los valores válidos para este serà uno de los siguientes caracteres: =*+#%/

	Como resultado, la función devolverá una cadena desencriptada. Para este proceso es necesario
identificar el principio y fin de una letra encriptada el cual está delimitado por el parámetro utilizado
como token.	
	"""

"""

Tests del enunciado

Aquí te mostramos algunos ejemplos:
	● decrypt ("hol*1*", {'a':1},'*') devolvería "hola"
	● decrypt ("M+0+s +3+m+0+gos son G+8+NI+4+L+8+S.", {'i':0,'E':8,'a':3,'A':4},,'+') devolvería "Mis amigos son GENIALES."
	● decrypt ("hol#1# 11", {'a':1}, '#') devolvería "hola 11"
	● decrypt ("16", {'A':1},'%') devolvería "16"
	● decrypt ("/7/ola mi c/5/lular /5/s 09999999", {'e':5,'H':7}, '/') devolvería "Hola mi celular es 09999999"
	● decrypt ("*120**100*ci*20*n q*30**17* *100**17*rmit*17* g*17*n*17*rar*30*na s*20*licit*30*d", {'O':120,'o':20,'e':17,'p':100,'u':30}, '*')
devolvería "Opcion que permite generar una solicitud"
	● decrypt ("Hola mi celular es 09999999", {'9':7,'H':8}, '=') devolvería "No es posible encriptar la cadena. Verifique los parámetros de entrada", esto es
debido a que el parámetro keys tiene un valor numérico.
	● decrypt ("Hola mi celular es 09999999", {'e':7,'H':8}, '¿') devolvería "No es posible desencriptar la cadena. Verifique los parámetros de entrada", esto es debido a que el parámetro token tiene un valor que no es válido.

Restricciones

Las mismas del apartado anterior, únicamente cambiaremos el mensaje por: “No es posible desencriptar la cadena. Verifique los parámetros de entrada”.

	● Para el diccionario keys las claves deben contener solamente letras y los valores relacionados deben ser solamente números, y en ambos casos éstos no pueden estar repetidos.
	● La longitud del campo token es 1.
	● Si el parámetro token difiere de uno de los posibles valores válidos.

"""

def decrypt(inputValue : str , keys : dict, token: str):
	"""
	Encripta el string inputValue segun el diccionario keys y rodenadolo del char token
		>>> decrypt ("hol*1*", {'a':1},'*')
		'hola'
		>>> decrypt ("M+0+s +3+m+0+gos son G+8+NI+4+L+8+S.", {'i':0,'E':8,'a':3,'A':4},'+')
		'Mis amigos son GENIALES.'
		>>> decrypt ("hol#1# 11", {'a':1}, '#')
		'hola 11'
		>>> decrypt ("16", {'A':1},'%')
		'16'
		>>> decrypt ("/7/ola mi c/5/lular /5/s 09999999", {'e':5,'H':7}, '/')
		'Hola mi celular es 09999999'
		>>> decrypt ("*120**100*ci*20*n q*30**17* *100**17*rmit*17* g*17*n*17*rar *30*na s*20*licit*30*d", {'O':120,'o':20,'e':17,'p':100,'u':30}, '*')
		'Opcion que permite generar una solicitud'
		>>> decrypt ("Hola mi celular es 09999999", {'9':7,'H':8}, '=')
		'No es posible desencriptar la cadena. Verifique los parámetros de entrada'
		>>> decrypt ("Hola mi celular es 09999999", {'e':7,'H':8}, '¿')
		'No es posible desencriptar la cadena. Verifique los parámetros de entrada'
	"""

	ERROR_MSG = "No es posible desencriptar la cadena. Verifique los parámetros de entrada"
	if checkDictionary(keys) == False or checkToken(token) == False:
		return ERROR_MSG
	decryptedValue = inputValue
	for character in keys:
		decryptedValue = decryptedValue.replace(token + str(keys[character]) + token, character)
	return decryptedValue

def checkDictionary(keys:dict)->bool:
	NUMERIC_CHARS ="0123456789"
	values = {}
	for keyValue in keys:
		if type(keyValue) != str:
			return False
		#NO pueden haber valores repetidos.
		if keyValue in NUMERIC_CHARS:
			return False
		if keyValue in values:
			return False
		else:
			values[keyValue] = keyValue
	return True

def checkToken(token: str)->bool:
	VALID_CHARS = "=*+#%/"
	#Si tenemos más de un caracter ( el enunciado dice que sea 1 pero no tiene sentido)
	if len(token) != 1:
		return False
	# Si el token no es uno de los carácteres válidos.
	if token not in VALID_CHARS:
		return False
	return True

#def checkInput(inputValue:str, token:str)->bool:
#	#Check que el token NO esté ya incluido en la inputValue.
#	if token in inputValue:
#		return False
#	return True




# A partir de aqui, solo lo ejecutamos si llamamos el script como programa (main).
#   si fuese un import de este fichero, esto no se ejecutaría.
if __name__ == "__main__":
	#Ejecutamos los tests para evitar que en la entrega se ejecute (harán un import del fichero).
	import doctest
#	print(decrypt ("hol*1*", {'a':1},'*'))
	doctest.testmod()