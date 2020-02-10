from sys import exit
#para hacer uso de la funcion exit() se importan las librerias
class Archivo:
	def __init__(self,nombre):
		try:
			self.archivo = open(nombre,'r')
			self.nonbre = nombre	
			self.copia = open("copia.txt",'w')
		#El nombre de la excepcion es la siguiente
		except FileNotFoundError:
			print("No se puede abir el archivo ",nombre)
			exit()
	def muestra(self):
		i = 1
		for linea in self.archivo:
			print("{:3}:{}".format(i,linea),end = "")
			i += 1
		#cada vez que se lee el archivo se tiene que pocicionar el puntero al inicio para que no apunte al final del archivo
		self.archivo.seek(0)
	#Funcion encontrar,recibe 2 cadenas la primera es el conjunto donde se buscara, y el segundo es lo que se buscara
	@staticmethod
	def encuentra(cadena,conjunto):
		contador = 0
		for i in range(len(cadena)):
			if cadena[i] in conjunto:
				contador += 1
		#se retorna la cantidad de veces que aparece en la cadena
		return contador
		
	def cuentaVocales(self):
		contador = 0
		# con el for se lee linea por linea
		for linea in self.archivo:
			#para cada linea se busca las vocales com acento y sin acento y mayusculas y minusculas.
			contador += Archivo.encuentra(linea,"aeiouAEIOUáéíóúÁÉÍÓÚ")            
		self.archivo.seek(0)
		return contador
	
	def cuentaConsonantes(self):
		contador = 0
		for linea in (self.archivo):
			contador += Archivo.encuentra(linea,"bcdfghjklmnñpqrstvwxyzBCDFGHJKLMNÑPQRSTVWXYZćǵḱĺḿńṕŕśẃýźĆǴḰĹḾŃṔŔŚǗẂÝŹ")
		self.archivo.seek(0)
		return contador
		
	def cuentaSignosPuntuacion(self):
		contador = 0
		for linea in self.archivo:
			contador += Archivo.encuentra(linea,".:,;\'\"¿?!¡-ćǵḱĺḿńṕŕśẃýźĆǴḰĹḾŃṔŔŚǗẂÝŹáéíóúÁÉÍÓÚ")
		self.archivo.seek(0)
		return contador
	
	def cuentaEspacios(self):
		contador = 0
		for linea in self.archivo:
			contador += Archivo.encuentra(linea," ")
		self.archivo.seek(0)
		return contador
	
	def cuentaPalabras(self):
		palabras = 0
		for linea in self.archivo:
			i = 0
			if len(linea) != 0 and linea[0] != " ":
				palabras += 1
			#se tiene que recorrer todos los espacios en blanco por que pueden que hayan 2 o mas y eso no seria una palabra
			while i < len(linea):
				if linea[i] == " ":
					while i < len(linea) and linea[i] == " ":
						i += 1
					palabras += 1
				i += 1
		self.archivo.seek(0)
		return palabras
		
	def cuentaLineas(self):
		contador = 0
		for linea in self.archivo:
			contador += 1
		self.archivo.seek(0)
		return contador
		
	def cuentaMayusculas(self):
		contador = 0
		for linea in self.archivo:
			contador += Archivo.encuentra(linea,"ABCDEFGHIJKLMNÑOPQRSTUVWXYZÁĆÉǴÍḰĹḾŃÓṔŔŚÚǗẂÝŹ")
		self.archivo.seek(0)
		return contador
		
	def cuentaMayusculas2(self):
		contador = 0
		for linea in self.archivo:
			for i in range(len(linea)):
				if ord(linea[i]) >= 65 and ord(linea[i]) <= 90:
					contador += 1
		self.archivo.seek(0)
		return contador
	
	def cuentaMinusculas(self):
		contador = 0
		for linea in self.archivo:
			contador += Archivo.encuentra(linea,"abcdefghijklmnñopqrstuvwxyzáćéǵíḱĺḿńóṕŕśúǘẃýź")
		self.archivo.seek(0)
		return contador
	
	def cuentaMinusculas2(self):
		contador = 0
		for linea in self.archivo:
			for i in range(len(linea)):
				if ord(linea[i]) >= 97 and ord(linea[i]) <= 122:
					contador += 1
		self.archivo.seek(0)
		return contador
		
	def copiaArchivo(self):
		try:
			#se usa la funcion write para escribir por lineas la copia del archivo
			for linea in self.archivo:
				self.copia.write(linea)
			self.archivo.seek(0)
			#al terminar de usarse se cierran los archivos
			self.copia.close()
			print("Se creo una copia de su archivo, su nombre es copia.txt\nSu contenido es")
			for linea in self.archivo:
				print("  ",linea,end = "")
			self.archivo.seek(0)
		except FileNotFoundError:
			print("No se puede crear el archivo ",nombre)
		
	def convierteAMayusculas(self):
		print("La cadena convertida a mayusculas es ")
		for linea in self.archivo:
			#para convertir a mayusculas se usa la funcion upper
			print("   ",linea.upper(),end = "")
		self.archivo.seek(0)
			
	def convierteAMinusculas(self):
		print("La cadena convertida a minusculas es ")
		for linea in self.archivo:
			#para convertir a minusculas se usa la funcion lower
			print("  ",linea.lower(),end  = "")
		self.archivo.seek(0)
		
	def muestraHexadecimal(self):
		print("La cadena convertida a hexadecimal es ")
		for linea in self.archivo:
			print("  ",linea,end = "")
			for i in range(len(linea)):
				#para mostrar a hexadecimal se usa la funcion hex y la funcion ord
				print(hex(ord(linea[i])),end = "")
			print("")
		self.archivo.seek(0)
	
nombre = input("Da el nombre del archivo ")
archivo = Archivo(nombre)
archivo.muestra()
print("El total de vocales es ",archivo.cuentaVocales())
print("El total de consonantes es ",archivo.cuentaConsonantes())
print("El numero de signos de puntuacion es ",archivo.cuentaSignosPuntuacion())
print("El numero de espacios en blanco es ",archivo.cuentaEspacios())
print("El total de palabras es ",archivo.cuentaPalabras())
print("El total de lineas es ",archivo.cuentaLineas())
print("El total de mayusculas es ",archivo.cuentaMayusculas())
print("El total de minusculas es ",archivo.cuentaMinusculas())
archivo.copiaArchivo()
archivo.convierteAMayusculas()
archivo.convierteAMinusculas()
archivo.muestraHexadecimal()
#es importante cerrar el archivo al final para evitar errores
archivo.archivo.close()
