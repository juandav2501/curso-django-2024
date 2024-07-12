# tipos de dato:

enteros = 1
flotantes = 2.3

textos = 'Mi nombre'

booleanos = True


# operaciones aritmeticas 

print ( 2 + 9)
print ( 2 - 9)
print ( 2 * 9)
print ( 20 / 9)
print( 2**5 ) 

print( 2+5*8 ) 
print( (2+5)*8 ) 

# condicionales 

if True:
    print('esto es verdad')

validacion = False
if validacion:
    print('esto no se ejecuta, solo se ejecuta cuando es verdad')
else:
    print('esto se ejecuta cuando es falso')


# bucles

for i in range(10):
    print(i)

lista = [2, 4, 6, 8]
for i in lista:
    print(i)


while True:
    bandera = input("ingresa 0 para salir") == "0"
    if bandera:
        break

bandera = True
while bandera:
    bandera = input("ingresa 0 para salir") != "0"


# funciones

def nombre_funcion(parametros):
    print(parametros)
    return 0 

nombre_funcion(123)


def nombre_funcion_multiple_parametros(*arg, **kw):
    print("arg", arg)
    print("kw", kw)
    return 0 

nombre_funcion_multiple_parametros(123)
nombre_funcion_multiple_parametros(123, numero=555)
nombre_funcion_multiple_parametros(123, 456, numero=555)