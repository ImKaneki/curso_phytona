# return devuelve valores que podre hacer uso
# crear una funcion que retorne el numero 10, y muestre por terminal si es par
# siempre que el valor retorne mi funcion se utilice en mas sentencias u operaciones hacer uso de return
def diez():
    return 10
if diez()%2==0
    print("es par")
else:
    print("es impar")
#print solo muestra por terminal 
**ejemplo**
# return cuando queremos que nuestra funcion devuelva o retorne un tipo de dato o un tipo de dato estructurado

# crear una funcion que me muestre el producto de dos numeros
def producto(a,b):
    return a*b
print(producto(4,8))

# crear una funcion que me retorne una lista de tres numeros 
def lista_numeros():
    return [3,2,6]
# crear una funcion que  por parametro reciba un nombre y reciba un nombre y retorne un mensaje de bienvenida con el nombre
def mensaje (nombre)
    print(f"hola, {nombre},bienvenido al colegio")
mensaje("jose")

# crear una funcion que reciba por parametro una lista de numeros y me devuelva el numero menor, mostrar por terminal el valor retornado por la funcion
lista=[4,3,6,78,7]
def Min(1)
    minimo=1[0]
    for n in 1:
        if n < minimo:
            minimo=n
        return minimo
print(Min(lista))

# crear una funcion que reciba como parametro el nombre y la edad de una persona mi funcion debera tener 
nombre=input("ingrese su nombre: ")
edad=int(input("ingrese su edad")
def persona(nom,edad):
    # return {
    #   "nombre":nom,
#       "edad":edad
#  }
return dict(
    nombre=nom,
    edad=edad   
)
print(persona(nombre,edad)
    nueva_lista
    nueva_lista
suma(4,7,8,5,2,4)

##ejemplos de lambda
saludo=lambda:"hola"
print(saludo("ruth","castillo"))
# crear un programa anonimo que reciba como parametro una lista de 5 numeros y retorne dos listas una con los numeros pares y otra con numeros impares

def generaPares(m)
 n=5
lista=[]
while n<=m:
lista.append(n*2)
n+=1
return lista
print(generarPares(10))


lista=[4,7,5,3,47,2,10,8,10]
pares=lambda l: [n for n in lista if n%2==0]
impares=lambda l: [n for n in lista if n%2==0]
print(pares(lista))
print(impares(lista))


unt(input())

def mensaje(m)
    print(m)
def pedir_nombre():
    nombre=input("ingresa tu nombre")
    return nombre
mensaje(pedir_nombre())

#MAP
lista=[4,7,8,5,2]
map(lambda x:x+1,lista) #por defecto retorna una lista

# filter
# tengo una lista de alumnos que todos ellos aprobaron y pasan al tercer semestre,
#problema en mi lista todos estan con el segundo semestre por lo que tendremos que crear una solucion que cambie el campo
# de semestre  de 2 a 3

"nombre":"abel",
"edad":36,
"semestre":2

"nombre":"antohny",
"edad":40,
"semestre":2

"nombre":"edith",
"edad":50,
"semestre":2
]
def objeto(e):
    if "semestre" in e:
        e["semestre"]=e["semestre"]+1
    return [
        e
    ]


alumnos_actualizados=list(map(lambda e:e["semestre"]+1,lista_alumnos))
print(alumnos_actualizados)
# filter 
# devolver los numeros pares de una lista
lista=[4,8,2,5,7,10,6,5,3,20]
nueva_lista=list(filter(lambdax:x%2==0,lista))
print(nueva_lista)
lista_alumnos=[
    







       
