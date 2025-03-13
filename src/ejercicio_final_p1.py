#!/usr/bin/env python3

""" 
	Autor: Gabriel Reus Rodriguez greus@uoc.edu

	Ejercicio FINAL pregunta 1 del modulo A2 del curso de programacion de python.
	
	En este ejercicio, deberás implementar una función llamada encrypt(inputValue, keys, token)
que reciba una cadena y realice la encriptación. Realizaremos una encriptación básica, basada en
sustitución de caracteres, pero te permitirá trabajar los conceptos fundamentales del curso. La
función recibe tres parámetros:
	
	● inputValue, que será un string con la cadena a encriptar.
	● keys, que será un diccionario compuesto por pares donde la clave será una letra y el valor
		correspondiente un número, estos servirán durante la encriptación. Por ejemplo:
			keys= {
				"a" : 1,
				"e" : 2,
				"U" : 3
			}
	● token, que será un carácter que nos permitirá identificar el inicio y fin de una letra
		encriptada. Así mismo los valores válidos para este serà uno de los siguientes caracteres: = *
		+ # % /

	El mecanismo de encriptación será el siguiente. Dado una cadena de caracteres que corresponden al
parámetro inputValue, si existe una letra en la cadena que corresponda con una clave del
diccionario keys, esta deberá ser reemplazada con el valor numérico que le corresponda y será
delimitado al principio y al final con el carácter utilizado como token.
"""
""" 
	Restricciones
	Para las siguientes restricciones siempre deberá finalizar la ejecución del programa y mostrar el
		siguiente mensaje de error: “No es posible encriptar la cadena. Verifique los parámetros de entrada “.
		
		● Para el diccionario keys las claves deben contener solamente letras y los valores
			relacionados deben ser solamente números, y en ambos casos éstos no pueden estar
			repetidos.
		● La longitud del campo token es 1.
		● Si una cadena previamente tiene incluido el carácter del parámetro token deberá mostrar el
			mensaje de error.
		● Si el parámetro token difiere de uno de los posibles valores válidos.
"""

"""
Tests del enunciado

	● encrypt (“hola”, {'a':1},'*') devolvería “hol*1*”
	● encrypt (“Mis amigos son GENIALES.”, {'i':0,'E':8,'a':3,'A':4},'+')
		devolvería “M+0+s +3+m+0+gos son G+8+NI+4+L+8+S.”
	● encrypt (“hola 11”, {'a':1}, '#') devolvería “hol#1# 11”
	● encrypt (“16”, {'A':1},'%') devolvería “16”
	● encrypt (“Hola mi celular es 09999999”, {'e':5,'H':7}, '/') devolvería “/7/ola
		mi c/5/lular /5/s 09999999”
	● encrypt (“Opcion que permite generar una solicitud”,
		{'O':120,'o':20,'e':17,'p':100,'u':30}, '*') devolvería “*120**100*ci*20*n
		q*30**17* *100**17*rmit*17* g*17*n*17*rar *30*na s*20*licit*30*d”
	● encrypt (“Hola mi celular es 09999999”, {'9':7,'H':8}, '=') devolvería “No es
		posible encriptar la cadena. Verifique los parámetros de entrada”, esto es
		debido a que el parámetro keys tiene un valor numérico.
	● encrypt (“Hola mi celular es 09999999”, {'e':7,'H':8}, ‘¿’) devolvería “No es
		posible encriptar la cadena. Verifique los parámetros de entrada”, esto es
		debido a que el parámetro token tiene un valor que no es válido.
	● encrypt (“Hola ** mi celular es 09999999”, {'e':7,'H':8}, '*') devolvería “No
		es posible encriptar la cadena. Verifique los parámetros de entrada”, esto
		es debido a que la cadena de entrada inputValue, tiene incluido en su texto
		caracteres iguales al parámetro token.

"""

def encrypt(inputValue : str , keys : dict, token: str):
	"""Encripta el string inputValue segun el diccionario keys y rodenadolo del char token
		>>> encrypt("", {"a":1, "e": 2, "U":3, "1":4}, '+')
		'No es posible encriptar la cadena. Verifique los parámetros de entrada'
		>>> encrypt("Hola mundo!", {"p":1, "e": 2, "U":3, "t":4}, '*')
		'Hola mundo!'
		>>> encrypt("Hola mund1o!", {"a":1, "e": 2, "U":3, "t":4}, '+')
		'Hol+1+ mund1o!'
		>>> encrypt ("hola", {'a':1},'*')
		'hol*1*'
		>>> encrypt ("Mis amigos son GENIALES.", {'i':0,'E':8,'a':3,'A':4},'+')
		'M+0+s +3+m+0+gos son G+8+NI+4+L+8+S.'
		>>> encrypt ("hola 11", {'a':1}, '#')
		'hol#1# 11'
		>>> encrypt ("16", {'A':1},'%')
		'16'
		>>> encrypt ("Hola mi celular es 09999999", {'e':5,'H':7}, '/')
		'/7/ola mi c/5/lular /5/s 09999999'
		>>> encrypt ("Opcion que permite generar una solicitud", {'O':120,'o':20,'e':17,'p':100,'u':30}, '*')
		'*120**100*ci*20*n q*30**17* *100**17*rmit*17* g*17*n*17*rar *30*na s*20*licit*30*d'
		>>> encrypt ("Hola mi celular es 09999999", {'9':7,'H':8}, '=')
		'No es posible encriptar la cadena. Verifique los parámetros de entrada'
		>>> encrypt ("Hola mi celular es 09999999", {'e':7,'H':8}, '¿')
		'No es posible encriptar la cadena. Verifique los parámetros de entrada'
		>>> encrypt ("Hola ** mi celular es 09999999", {'e':7,'H':8}, '*')
		'No es posible encriptar la cadena. Verifique los parámetros de entrada'

	"""
	ERROR_MSG = "No es posible encriptar la cadena. Verifique los parámetros de entrada"
	if checkDictionary(keys) == False or checkToken(token) == False or checkInput(inputValue, token) == False:
		return ERROR_MSG
#	encryptedValue = inputValue
#	for character in keys:
#		encryptedValue = encryptedValue.replace(character, token + str(keys[character]) + token)
	encryptedValue =""
	for character in inputValue:
		if character in keys:
			encryptedValue += token + str(keys[character]) + token
		else:
			encryptedValue += character
	return encryptedValue

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

def checkInput(inputValue:str, token:str)->bool:
	#Check que el token NO esté ya incluido en la inputValue.
	if token in inputValue:
		return False
	return True


# A partir de aqui, solo lo ejecutamos si llamamos el script como programa (main).
#   si fuese un import de este fichero, esto no se ejecutaría.
if __name__ == "__main__":
	#Ejecutamos los tests para evitar que en la entrega se ejecute (harán un import del fichero).
	import doctest
	doctest.testmod()
#	print(encrypt ("hola 11", {'a':1}, '#'))