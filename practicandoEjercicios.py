#PRACTICANDO PARCIAL
#Ejercicios faciles
#--------------------------------------------------------------------------------------------  
#Pedir un número y decir si es mayor, menor o igual a 0.

#numeroUsuario = int (input("Ingresa un numero: "))

#if numeroUsuario > 0:
#    print (f"{numeroUsuario} es mayor que 0")
#elif numeroUsuario < 0:
#    print (f"{numeroUsuario} es menor que 0")
#elif numeroUsuario == 0:
#    print ("El numero ingresado es igual 0")
#--------------------------------------------------------------------------------------------  
#ingresar una edad y mostrar si la persona es mayor de edad (18 años o más).

#mayorDeEdad = 18
#edadPersona = int (input("Ingresa tu edad: "))

#if edadPersona > mayorDeEdad:
#    print ("Sos mayor de edad")
#elif edadPersona == mayorDeEdad:
#    print ("18. Mayor edad")
#else:
#    print ("Sos menor de edad")
#--------------------------------------------------------------------------------------------  
#Mostrar los números del 1 al 10 usando un while.

#contador = 1
#while contador <= 10:
#    print ("Numeros: ", contador)
#    contador = contador + 1
#--------------------------------------------------------------------------------------------  
#Pedir un número y mostrar su tabla de multiplicar hasta el 10

#contador = 0
#numeroIngresado = int (input("Ingresa un numero: "))

#while contador < 10:
#    contador = contador + 1
#    resultado = contador * numeroIngresado
#    print (numeroIngresado, " X ", contador, " = ", resultado )
#--------------------------------------------------------------------------------------------  
#Pedir dos números y mostrar el mayor.

#num1 = int (input("Ingresa un numero: "))
#num2 = int (input("Ingresa otro numero: "))

#if num1 > num2:
#    print (f"{num1} es mayor que {num2}")
#elif num1 < num2:
#    print (f"{num1} es menor que {num2}")
#else:
#    print (f"{num1} = {num2}")
#--------------------------------------------------------------------------------------------  
#Contar del 10 al 1 (de manera descendente) usando un for

#for numeros in range (10, 0, -1):
#    print (numeros)
#--------------------------------------------------------------------------------------------  
#Crear una lista con los números del 1 al 5 e imprimirla

#listaNumeros = [1, 2, 3, 4, 5]
#print (listaNumeros)
#--------------------------------------------------------------------------------------------  
#EJERCICIOS INTERMEDIOS
#Pedir números al usuario hasta que ingrese un número negativo, y luego mostrar la suma total.

#usuarioNumeros = 0
#sumaTotal = 0
#usuarioNumeros = int (input("Ingresa un numero: ")) #Si se cumple ingresa

#while usuarioNumeros >= 0:
#    sumaTotal = sumaTotal + usuarioNumeros
#    usuarioNumeros = int (input("Ingresa un numero: "))

#print ("La suma total es de:", sumaTotal)
#--------------------------------------------------------------------------------------------  
#Leer 5 números y guardar sólo los números pares en una lista. Mostrar la lista final.

#listaNumeros = []

#for numeros in range (1,6,1):
#    numeros = int (input("Ingresa un numero: "))
#    if numeros % 2 == 0:
#        listaNumeros.append(numeros)

#print (listaNumeros)
#--------------------------------------------------------------------------------------------  
#Dada una lista, mostrar cuántos elementos mayores a 10 contiene.

#numeros = [5, 3, 10, 20, 35]
#contador = 0

#for numero in numeros: #Recorriendo la lista
#    if numero > 10:
#        contador = contador + 1

#print (f"La lista tiene {contador} numeros mayores a 10")
#--------------------------------------------------------------------------------------------  
#Pedir 10 nombres al usuario y guardar solo los que tengan más de 5 letras

#guardarNombres = []

#for nombres in range (1,11,1):
#    nombres = str (input("Ingresa un nombre: "))
    
#    if len(nombres) > 5:
#        guardarNombres.append(nombres)
        
#print (guardarNombres)
#--------------------------------------------------------------------------------------------  
#Crear un programa que recorra una lista de números y cuente cuántos son pares y cuántos impares.

#lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#contadorPar = 0
#contadorImpar = 0

#for numeros in (lista):
#    if numeros % 2 == 0:
#        contadorPar = contadorPar + 1
#    else:
#        contadorImpar = contadorImpar + 1

#print (f"Numeros pares: {contadorPar}")
#print (f"Numeros impares {contadorImpar}")
#--------------------------------------------------------------------------------------------        
#Leer 5 números y mostrar el máximo y el mínimo de la lista.

#lista = []

#for numeros in range (1,6,1):
#    numeros = int (input("Ingresa un numero: "))
#    lista.append(numeros)

#print ("Numero maximo: ",max(lista)) #directamente en el print para sacar el max y el min
#print ("Numero minimo: ",min(lista))
#-------------------------------------------------------------------------------------------- 

#Pedir palabras hasta que el usuario ingrese "salir", luego mostrar todas las palabras juntas en una lista

#palabras = []

#usuarioEntrada = str (input("Ingresa una palabra: "))
#while usuarioEntrada != "salir":
#    usuarioEntrada = str (input("Ingresa una palabra: "))
    
#    if usuarioEntrada != "salir":
#        palabras.append(usuarioEntrada)
#    elif usuarioEntrada == "salir":
#        print ("Hasta luego")

#print ("Palabras ingresadas: ", palabras)
#-------------------------------------------------------------------------------------------- 

#EJERCICIOS AVANZANDOS
#Pedir 10 números y crear dos listas: una con los números mayores a 50 y otra con los números menores o iguales a 50.

#listaMayores50 = []
#listaMenores50 = []

#for numeros in range (1,11,1):
#    numeros = int (input("Ingresa un numero: "))

#    if numeros > 50:
#        listaMayores50.append(numeros)
#    elif numeros <= 50:
#        listaMenores50.append(numeros)

#print (f"Lista mayores: {listaMayores50}")
#print (f"Lista menores: {listaMenores50}")
#--------------------------------------------------------------------------------------------

#Crear una lista de números aleatorios entre 1 y 100 (usar random.randint) y luego ordenarla de menor a mayor.
#import random #importo la libreria para los numeros random

#numerosRandom = []

#for numeros in range (1,11,1):
#    numerosRandom.append(random.randint(1, 100)) #aplico los numeros random con random.randint
#    numerosRandom.sort() #el sort es para ordenar de menor a mayor

#print (numerosRandom)
#--------------------------------------------------------------------------------------------

#Pedir un número y verificar si ese número está en una lista ya definida

#numeros = [1, 5, 112, 28]

#usuarioNumero = int (input ("Ingresa un numero: "))

#if usuarioNumero in numeros:
#        print (f"El numero {usuarioNumero} esta dentro de la lista")
#else:
#        print (f"El numero {usuarioNumero} no esta dentro de la lista")  
#--------------------------------------------------------------------------------------------

#Dada una lista de palabras, crear otra lista que contenga sólo las palabras que empiecen con vocal

#palabras = ["argentina", "valor", "elefante", "oidos", "caca", "programacion"]
#listaVocales = []
#vocales = ("a", "e", "i", "o", "u", "A", "E", "I", "O", "U")

#for i in palabras:
#    if i[0] in vocales:
#        listaVocales.append(i)

#print(listaVocales)
#--------------------------------------------------------------------------------------------

#Simular un carrito de compras: el usuario puede agregar productos a una 
#lista hasta que escriba "terminar", luego mostrar el carrito final y la cantidad de productos.

#listaCompras = []
#usuarioCompras = ""
#acumuladorProductos = 0

#usuarioCompras = str (input("Ingresar producto al carrito: "))
#while usuarioCompras != "terminar":
#    listaCompras.append(usuarioCompras)
#    acumuladorProductos = acumuladorProductos + 1
#    usuarioCompras = str (input("Ingresar producto al carrito: "))

#print ("Carrito final: ", listaCompras)
#print ("Cantidad de productos: ", acumuladorProductos)
#--------------------------------------------------------------------------------------------


#Estructuras secuenciales (1 a 5)
#1)Conversor de temperaturas: Pedí una temperatura en °C y convertí a °F y °K. 
# Mostrá ambas conversiones.

#temperaturaC = int (input("Ingresa una temperatura en °C: "))

#temperaturaF = (temperaturaC * 9/5) + 32
#temperaturaK = temperaturaC + 273.15

#print (f"{temperaturaC} °C")
#print (f"{temperaturaF} °F")
#print (f"{temperaturaK} °K")
#--------------------------------------------------------------------------------------------


#2)Área y perímetro de figuras: Pedí al usuario una figura (círculo, cuadrado, triángulo) y calculá su área y perímetro.

#figura = str (input("Ingresa una figura: "))

#if figura == "circulo":
#    radio = float (input("Ingresa el radio: "))
#    area = 3.14 * radio ** 2
#    perimetro = 2 * 3.14 * radio
#    print (f"circulo: Area {area} Perimetro {perimetro}")
#elif figura == "cuadrado":
#    lado = float (input("Ingresa un lado: "))
#    area = lado * lado
#    perimetro = 4 * lado
#    print (f"cuadrado: Area {area} Perimetro {perimetro}")
#elif figura == "triangulo":
#    base = float (input("Ingresa su base: "))
#    altura = float (input("Ingresa su altura: "))
#    lado1 = float (input("Ingresa un lado: "))
#    lado2 = float (input("Ingresa un lado: "))
#    lado3 = float (input("Ingresa un lado: "))
#    area = (base * altura)/2
#    perimetro = lado1 + lado2 + lado3
#    print (f"triangulo: Area {area} Perimetro {perimetro}")
#else:
#    print ("Figura no valida")
#--------------------------------------------------------------------------------------------

#3)Promedio con decimales: Pedí 3 notas con coma y mostrale al usuario el promedio con dos decimales.
#infoNotas = (input("Ingresa tus notas con coma si es necesario (Apreta enter para continuar)"))
#nota1 = float (input("Nota uno: "))
#nota2 = float (input("Nota dos: "))
#nota3 = float (input("Nota tres: "))

#promedio = (nota1 + nota2 + nota3) //3

#print (f"Promedio: {promedio}")
#--------------------------------------------------------------------------------------------

#4)Descuento aplicado: Pedí precio y porcentaje de descuento, y mostrale el precio final.

#precio = int (input("Ingresa el precio del producto: "))
#porcentajeProducto = int (input("Ingresa el descuento que dice la etiqueta (10%, 20%, 30%): "))

#if porcentajeProducto == 30:
#    precioFinal = precio * (1 - porcentajeProducto /100)
#    print (f"Precio final: {precioFinal}")
#elif porcentajeProducto == 20:
#    precioFinal = precio * (1 - porcentajeProducto /100)
#    print (f"Precio final: {precioFinal}")
#elif porcentajeProducto == 10:
#    precioFinal = precio * (1 - porcentajeProducto /100)
#    print (f"Precio final: {precioFinal}")
#else:
#    print ("Ingresa un porcentaje correcto")
#--------------------------------------------------------------------------------------------

#5)Suma de cifras: Pedí un número de 3 cifras y mostrale la suma de sus cifras (usá int(str(...)[i]) o divisiones).

#numeroUsuario = int (input("Ingresa un numero de tres cifras: "))

#centena = numeroUsuario // 100
#decena = (numeroUsuario // 10) % 10
#unidad = numeroUsuario % 10

#print (f"{numeroUsuario} = {centena} + {decena} + {unidad}")
#--------------------------------------------------------------------------------------------

#Condicionales (6 a 10)
#Par, impar o cero: Pedí un número y decí si es par, impar o cero.

#numeroUsuario = int (input("Ingresa un numero: "))

#if numeroUsuario == 0:
#    print (f"{numeroUsuario} es CERO")
#elif numeroUsuario % 2 == 0:
#    print (f"{numeroUsuario} es PAR")
#else:
#    print (f"{numeroUsuario} es IMPAR")
#--------------------------------------------------------------------------------------------

#7)Mayor y menor de tres: Pedí tres números y decí cuál es el mayor y cuál el menor (sin usar max() ni min()).

#numero1 = int (input("Ingresa un numero: "))
#numero2 = int (input("Ingresa un numero: "))
#numero3 = int (input("Ingresa un numero: "))

#if numero1 > numero2 and numero1 > numero3:
#    print (f"{numero1} es MAYOR que {numero2} y {numero3}")
#elif numero2 > numero1 and numero2 > numero3:
#    print (f"{numero2} es MAYOR que {numero1} y {numero3}")
#elif numero3 > numero1 and numero3 > numero2:
#    print (f"{numero3} es MAYOR que {numero1} y {numero2}")
#--------------------------------------------------------------------------------------------

#8)Evaluador de contraseñas: Compará la contraseña ingresada con una predefinida y permití solo 3 intentos.

#password = "LebronJames"
#intentos = 0
#intentosMaximos = 3

#while intentos < intentosMaximos:
#    claveIngresada = str (input("Ingresa la clave: "))
    
#    if claveIngresada == password:
#        print ("Password correcta. Ingresando...")
#        break
#    else:
#        intentos = intentos + 1
#        print ("Password incorrecto.")

#if intentos == intentosMaximos:
#    print ("Alcanzaste el limite maximo de intentos. Vuelva mas tarde")
#--------------------------------------------------------------------------------------------

#9)Números iguales o distintos: Pedí dos números y mostrale si son iguales, o cuál es mayor y cuál es menor.

#Try intenta ejecutar el codigo y si hay un error (ingresar una letra) salta al bloque except
#Se usa cada vez que el codigo pueda fallar por algo que no controle directamente
#Usar Cada vez que el codigo depende de algo externo, como un usuario que se equivoque.
#try:
#    num1 = int (input("Ingresa el primer numero: "))
#    num2 = int (input("Ingresa el segundo numero: "))

#    if num1 == num2:
#        print (f"{num1} = {num2}")
#    elif num1 > num2:
#        print (f"{num1} es mayor que {num2}")
#    else:
#        print (f"{num1} es menor que {num2}")
#except:
#    print ("Error. Ingresa un numero.")
#--------------------------------------------------------------------------------------------

#10)Aprobado o desaprobado con condiciones: Si el promedio de 3 notas es mayor a 6, aprobado. 
# Pero si alguna es menor a 4, desaprobado igual.
#try:
#    nota1 = int(input("Ingresa la primer nota: "))
#    nota2 = int(input("Ingresa la segunda nota: "))
#    nota3 = int(input("Ingresa la tercer nota: "))

#    promedio = (nota1 + nota2 + nota3)/3

#    if nota1 <= 4 or nota2 <= 4 or nota3 <= 4:
#        print ("Estas DESAPROBADO (Una o mas notas son 4)")
#    elif promedio >= 6:
#        print ("Estas APROBADO")
#except:
#    print ("ERROR. Ingresa un numero.")
#--------------------------------------------------------------------------------------------

#Estructuras repetitivas (11 a 15)
#11) Sumar hasta un número: Pedí un número N y sumá todos los números del 1 al N.

#numero = int (input("Ingresa un numero: "))
#suma = 0

#for i in range (1,numero + 1,1):
#    suma = suma + i

#print (suma)
#--------------------------------------------------------------------------------------------

#12)Contador de pares e impares: Pedí 10 números y contá cuántos son pares y cuántos impares.

#contadorPares = 0
#contadorImpares = 0

#for i in range (1,11,1):
#    numeros = int (input("Ingresa un numero: "))

#    if numeros % 2 == 0:
#        contadorPares = contadorPares + 1
#    else:
#        contadorImpares = contadorImpares + 1

#print (f"Total numeros PARES: {contadorPares}")
#print (f"Total numeros IMPARES: {contadorImpares}")
#--------------------------------------------------------------------------------------------

#13)promedio hasta 'salir': El usuario ingresa notas hasta que escribe "salir". Mostrá el promedio.

#suma = 0
#cantidadNotas = 0

#ingresarNota = input("Ingresa una nota: ")
#while ingresarNota != "Salir":
    
#    ingresarNota = input("Ingresa una nota: ")
#    suma = suma + ingresarNota 
#   promedio = suma / cantidadNotas
    
#print (f"Promedio: {promedio}")
#--------------------------------------------------------------------------------------------

#LISTAS
#14)#Buscar un elemento: Pedí al usuario una lista de palabras y una palabra a buscar. Decí si está en la lista.

#lista = []

#for i in range (1,6,1):
#    palabrasLista = str (input("Ingresa palabras para una lista: "))
#    lista.append(palabrasLista)

#busquedaPalabra = str (input("Ingresa una palabra a buscar dentro de la lista: "))

#if busquedaPalabra in lista:
#    print(f"{busquedaPalabra} esta en la lista")
#else:
#    print (f"{busquedaPalabra} no esta en la lista")
#--------------------------------------------------------------------------------------------

#UTN EJERCICIOS COMPLEMENTARIOS
#Dada una lista de palabras, realizar las siguientes acciones:
#Mostrar cuántas palabras tienen exactamente 7 letras.
#Crear una nueva lista con las palabras que terminan en "o" o en "a".
#Preguntar al usuario una sílaba (por ejemplo, “ar”) y mostrar todas las palabras que la contengan.
#Mostrar la palabra más larga de la lista.
#palabras = ["computadora", "teclado", "pantalla", "ratón", "código", "memoria", "proceso"]

#palabras = ["computadora", "teclado", "pantalla", "raton", "codigo", "memoria", "proceso"]
#contador = 0

#for palabra in palabras: #No hace falta numeros porque ya recorro IN palabras
#    if len(palabra) == 7:
#        contador = contador + 1

#print (f"Cantidad de palabras con 7 letras: {contador}")

#terminanOyA = []

#for terminaciones in palabras:
#    if terminaciones.endswith("a") or terminaciones.endswith("o"):
#        terminanOyA.append(terminaciones)

#print (f"Lista actualizada de palabras que terminan en A/O: {terminanOyA}")

#palabraLarga = max(palabras, key=len)

#print (f"La palabra mas larga de la lista es: {palabraLarga}")
#-------------------------------------------------------------------------------------

#Carga de nombres y búsqueda de repetidos
#Crear un programa que:
#Pida al usuario ingresar nombres hasta que escriba "FIN".
#Agregue los nombres a una lista.
#Luego del ingreso:
#Mostrar cuántos nombres se ingresaron.
#Mostrar los que tienen más de 5 letras.
#Decir si hay nombres repetidos.

#lista = []
#contador = 0

#nombres = str (input("Ingresa nombres: (Si escribis FIN se cierra el programa)"))
#while nombres.lower() != "fin":
#    lista.append(nombres)
#    contador = contador + 1
#    nombres = str (input("Ingresa nombres: (Si escribis FIN se cierra el programa)"))

#print (f"Nombres ingresados: {lista}")

#for nombre in lista:
#    if len(nombre) > 5:
#        print (f"Nombres con mas de 5 letras: {nombre}")

#repetidos = []

#for nombre in lista:
#    if lista.count(nombre) > 1 and nombre not in repetidos:
#        repetidos.append(nombre)

#if repetidos:
#    print("Nombres repetidos:", repetidos)
#else:
#    print("No hay nombres repetidos.")
#-------------------------------------------------------------------------------------

#Lista de compras editable
#Crear un programa que:
#Permita al usuario agregar productos a una lista hasta que escriba "listo".
#Luego, mostrar la lista numerada.
#Preguntar si quiere quitar algún producto y, si sí, permitirlo hasta que escriba "no".
#Mostrar la lista final con un mensaje tipo: "Lista preparada para ir al súper."

#Creaste lista y parate listo
#productos = []
#contador = 0

#usuarioAgregar = str (input("Ingresa un producto - ('listo' para dejar de ingresar):"))
#while usuarioAgregar.lower() != "listo":
#    productos.append(usuarioAgregar)
#    contador = contador + 1
#    usuarioAgregar = str (input("Ingresa un producto - ('listo' para dejar de ingresar):"))

#mostrasdo la lista enumerada
#indice = 1
#for producto in productos:
#    print (f"{indice}){producto}")
#    indice = indice + 1

#Si el usuario quiere quitar un producto o no. Eliminar si asi desea.
#preguntaUsuario = str (input("Queres quitar algun producto: (S/N)"))

#if preguntaUsuario.lower() == "s":
#    productoEliminar = str (input("Ingresa producto a eliminar de la lista: "))
#    if productoEliminar in productos:
#        productos.remove(productoEliminar)
#        print(f"{productoEliminar} fue eliminado de la lista")
#elif preguntaUsuario == "n":
#    print(f"Lista preparada para ir al super: {productos}")
#else:
#    print ("El producto no esta en la lista")
#-------------------------------------------------------------------------------------

#Lista de edades y promedio
#Pedí al usuario 5 edades, guardalas en una lista y mostrá el promedio. 
#Luego, decí cuántos son mayores de edad.

#Lista y pedido de edades. Actualiza lista.
#edades = []

#for recorrer in range (1,6,1):
#    ingresoEdades = int (input("Ingresa una edad: "))
#    edades.append(ingresoEdades)

#Promedio de edades
#promedioEdades = sum(edades) / 5

#Mayor edad, contador y for para ver cuanta cantidad son mayor de edad
#mayorDeEdad = 18
#contador = 0

#for edad in edades:
#    if edad >= mayorDeEdad:
#        contador = contador + 1

#print (f"Edades ingresadas: {edades}")
#print (f"Promedio de edades ingresadas: {promedioEdades}")
#print (f"Mayores de edad: {contador}")
#-------------------------------------------------------------------------------------

#Validador de DNI
#Pedí un número de DNI y validá que tenga entre 7 y 8 cifras. Si no es válido, pedilo de nuevo hasta que lo sea.

#pedirDNI = (input("Ingresa tu DNI: "))
#while len(pedirDNI) != 8:
#    print ("DNI INVALIDO. Debes ingresar 8 numeros")
#    pedirDNI = (input("Ingresa tu DNI: "))
    
#print ("DNI VALIDO")  
#-------------------------------------------------------------------------------------

#Validar fecha de nacimiento
#Pedí el día, mes de nacimiento y anio. Valida si es correcto o no

#ingresoNacimiento = (input("Ingresa tu fecha de nacimiento (Todo junto sin espacios): ")) 

#dia = ingresoNacimiento[0:2]
#mes = ingresoNacimiento[2:4]
#anio = ingresoNacimiento[4:8]

#print(f"{dia}/{mes}/{anio}")

#while len(ingresoNacimiento) != 8:
#    print ("ERROR. Ingresa 8 numeros")
#    ingresoNacimiento = (input("Ingresa tu fecha de nacimiento (Todo junto sin espacios): "))

#validacion = input (f"{ingresoNacimiento} es correcto? Responde S/N: ")

#if validacion.lower() == "s":
#    print ("Fecha de nacimiento ingresada")
#elif validacion.lower() == "n":

    #while validacion.lower() != "s":
#        ingresoNacimiento = (input("Ingresa de nuevo la fecha: "))
#        dia = ingresoNacimiento[0:2]
#        mes = ingresoNacimiento[2:4]
#        anio = ingresoNacimiento[4:8]
#        print(f"{dia}/{mes}/{anio}")
        
#        validacion = input (f"{ingresoNacimiento} es correcto? Responde S/N: ")
#        if validacion.lower() == "s":
#            print ("Fecha de nacimiento ingresada")
#-------------------------------------------------------------------------------------


