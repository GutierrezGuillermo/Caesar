def cripto(palabra,clave):
	e = list(palabra)
	z = []
	for i in e:
		z.append((chr(((ord(i)- 96) + clave ) % 26 + 96)))
	new = ""
	for x in z:
		new += x
	return new
	
bandera = True
while bandera:
	hola = cripto(input("Inserte palabra o 's': "), int(input("Inserte clave o '0': ")))
	if hola == 's':
		bandera = False
	else:
		print(hola)
	
