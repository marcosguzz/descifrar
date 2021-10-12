from string import ascii_lowercase
import operator


texto = open('texto.txt', 'r')
msj = texto.read()
msjMin = msj.lower()
a = [' ', ',', '.', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '/n']
length = len(msj)
print(length)
for c in a:
    length = length - msj.count(c)   #Se calcula las letras que hay sin contar comas, puntos, espacios y números
Alphabet = ascii_lowercase
FrecT = []
Frec = [['e', 16.78, 100], ['a', 11.96, 100], ['o', 8.69, 100], ['l', 8.37, 100], ['s', 7.88, 100], ['n', 7.01, 100],
        ['d', 6.87, 100], ['r', 4.94, 100], ['u', 4.80, 100], ['i', 4.15, 100], ['t', 3.31, 100], ['c', 2.92, 100],
        ['p', 2.776, 100], ['m', 2.12, 100], ['y', 1.54, 100], ['q', 1.53, 100], ['b', 0.92, 100], ['h', 0.89, 100],
        ['g', 0.73, 100], ['f', 0.52, 100], ['v', 0.39, 100], ['j', 0.30, 100], ['ñ', 0.29, 100], ['z', 0.15, 100],
        ['x', 0.06, 100], ['k', 0, 100], ['w', 0, 100]]
usados = []
for letra in Alphabet:					#recorremos todo el alfabeto
    i = msjMin.count(letra)   			#se cuenta cuantas veces aparece en el texto
    por = [letra, (i / length) * 100]			#se calcula la frecuencia y se guarda [letra, frecuencia]
    FrecT.append(por)					#se añade al array 
FrecT.sort(key=operator.itemgetter(1), reverse=True)
print(length)
i = 0

for letra in Frec:						#se recorre el array de frecuencias inicial
    for letraB in FrecT:					#se recorre el array de frecuencias creadas
        if letraB[0] not in usados:				#si no esta usada (la de frecuencias creadas)
            print(letraB[0], abs(letra[1] - letraB[1]))	#imprime la letra y la diferencia con cada una de las frecuencias
            if letra[2] > abs(letra[1] - letraB[1]):		#si la diferencia de la letra (de frecuencias inicial) es mayor que la calculada
                cambio = letraB[0]				#cambio = esa letra (creada)
                letra[2] = abs(letra[1] - letraB[1])		#se actualiza la diferencia en el array de frecuencias inicial
                print(cambio)
    msjMin = msjMin.replace(cambio, letra[0].upper())	#se reemplaza la letra de cambio por la letra de la frecuencia inicial y se pone en mayúscula para evitar errores
    usados.append(cambio)					#se añade el cambio al array de usados
    print(cambio, letra[0])					#se imprime el cambio 

#manualmente
msjMin = msjMin.replace('P', 's')
msjMin = msjMin.replace('T', 'm')
msjMin = msjMin.replace('K', 'r')
msjMin = msjMin.replace('S', 'n')
msjMin = msjMin.replace('N', 'l')
msjMin = msjMin.replace('C', 'p')
msjMin = msjMin.replace('B', 'q')
msjMin = msjMin.replace('H', 'j')
msjMin = msjMin.replace('V', 'x')
msjMin = msjMin.replace('Y', 'b')
msjMin = msjMin.replace('R', 'c')
msjMin = msjMin.replace('I', 't')
msjMin = msjMin.replace('L', 'i')
msjMin = msjMin.replace('M', 'f')
msjMin = msjMin.replace('Q', 'v/y')
msjMin = msjMin.replace('J', 'z')
msjMin = msjMin.replace('F', 'h')

print(msjMin)
