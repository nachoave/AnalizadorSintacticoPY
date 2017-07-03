
def lexer(cadena):
	cadena+=" "
	i=0
	j=0
	aux=""
	tokens=[]
	cParentesis=0

	while True:
		if i<len(cadena):
			if cadena[i]=='"':
				#Armando el auxiliar con cada token
				while cadena[i+j]!='"':
					if i+j==len(cadena):
						print("ERROR 0")
						break
					aux+=cadena[i+j]
					j+=1
				if cadena[i+j+1] not in [" ", "(", ")", "="]:
					print("ERROR 1")
					break
				else:
					tokens.append("<CADENA>")
			#Chequeo de palabra/s
			elif cadena[i].isalpha():
				while cadena[i+j].isalpha():
					aux+=cadena[i+j]
					j+=1
				if cadena[i+j] not in [" ", "(", ")", "=", ">", "<"]:
					print("ERROR 2")
					break
				else:
					#Palabras Reservadas
					if aux in ["and", "or", "not"]:
						tokens.append("<OPLOG>")
					elif aux in ["true", "false"]:
						tokens.append("<BOOL>")
					elif aux=="define":
						tokens.append("<DEFINE>")
					elif aux=="if":
						tokens.append("<IF>")
					elif aux=="set":
						tokens.append("<SET>")
					#Identificador
					else:
						tokens.append("<ID>")
			#Chequeo de números	
			elif cadena[i].isdigit():
				while cadena[i+j].isdigit():
					aux+=cadena[i+j]
					j+=1
				if cadena[i+j] not in [" ", "(", ")", "=", ">", "<", "+", "*", "^"]:
					print("ERROR 3")
					break
					else:
					tokens.append("<NUM>")
			#Operadores de Relación
			elif cadena[i] in ["<", ">", "="]:
				if cadena[i+1]=="=":
					j=2
				else:
					j=1
				tokens.append("<OPREL>")
			#Operadores Matemáticos
			elif cadena[i] in ["+", "*", "^"]:
				j=1
				tokens.append("<OPMAT>")
			#Paréntesis abierto
			elif cadena[i]=="(":
				j=1
				cParentesis+=1
				tokens.append("<(>")
			#Paréntesis cerrado con chequeo
			elif cadena[i]==")":
				if cParentesis<1:
					print("ERROR 4")
					break
				else:
					j=1
					cParentesis-=1
					tokens.append("<)>")

			else:
				j=1

			i+=j
			j=0
			aux=""

		else:
			print(tokens)
			break

cadena="((set (x 1)) (if (x<=10) (pepe=true)"
lexer(cadena)
