# Funciones
matematicamente una funcion es una ioperacion que toma uno o mas valores llamados a ´argumentos´ y produce un valor denominado ´resultado´
# FUNCIONES
matematicamente una funcion es una operacion 
que toma uno om mas valores llamados´argumentos´
y produce un valor denominado resultado.
f(x)=x/1+x**2
>[!NOTE]
>todos los lenguajes de programacion tienen 
funciones incorporadas (funciones internas), y funciones creadas por el usuario (fuciones externas)
en programacion una funcion es un subprograma, es una estrutura que nos permite agrupar codigo y sus principales objetivos son 
-´no repetir´ fragmetos de codigos 
-reutilizar´ el codigo en distitos esenarios 
## estrutura de una funcion
Una funcion viene "definida" por un nombre , sus parametros y su valor de retorno.
una ves creada la funcion podremos solicitar su ejecucion invocando la funcion por su nombre.
## definir una funcion en phyton
Para definir una funcion en phyton primero utilizaremos la palabra reservada ´def´ seguida por el nom,bre de la funcion. a continuacion especificaremos los parametros con () si es una funcion sin parametros, si se tuviera ,mas de un parametros iran separados por , , finalizaremos la linea con : , en la siguiente linea sin olvidar el identado , comenzara el cuerpo de la funcion (micro programa) que puede contener 1 o mas sentencias , finalmente devera retornar un resultadoo con la palabra reservada ´return´
> [!INFO]
> como retorno tambien se puede utilizar la ´funcion interna´, print (, para depuracion de codigo no es recomendable usarlo en produccion.
> **ejemplo:**
> ```python
> def saludo():
>   saludo="hola chivo"
>   saludo_dos="como estas"
>   return f"{saludo}, {saludo_dos}"+
> print(saludo)))
> # saludo()
> ## invocar una funcion 
> para invocar una funcion (o llamar,ejecutar) una funcion solo tendremos que escribir el´´nombre´ de la funcion seguido por ´()´ parentesis 
> ```phyton
> def saludo():
>   print("hola")
> # invocar la funcion 
> saludo()
> ```
> ## retornar un valor
> las funciones pueden retornar (o devolver) un valor.
> ```phyton
> def uno():
>   return 1
> uno()
> ```
> [!WARNING]
> no confundir "print()" con "return", el valor reornado por "return" nos permite usarlo fuera de su contexto. y "print" solo mostara el literal por terminal.
> **ejemplo**
> * en el archivo ´lecture.py´
> ## Retornando multiples valores
> el secreto es hacerlo mediante un tipo de dato estructurado.
> ```python
> def varios():
>   return 2,3,4
> varios ()
> # retorna (2,3,4 )
> def lista():
>   return ["hola",45]
>
> ## Parametros y argumentos 
> si una funcion no dispusiera de valores de entrada estaria limitada en su actuacion es por ello que los parametros los permiten variar los datos que consumen una funcion para obtener distintos resultados 
> ** ejemplo
> * creatr una funcion que recibe un valor numerico y retorna su raiz cuadrado*
> python
> def sqrt(valor):
>   return valor**(1/2)
> ## NOTA: en este caso el valor 4 es un argumento de la funcion 
> > sqrt(4)
    ```
> > Cuando llamamos a una funcion con `argumentos`, los valores de estos argumentos se copian en los correspondientes `parametros` dentro de la funcion.
> ```python
def ejm(a,b,c):
    return a+b+c
ejm(4,5,6)
```

### Argumentos nominales

En esta aproximacion los argumentos no son copiados en un orden especifico si no que **se asignan en cada parametro** , ellos nos permite evitar el problema de cococer o recordar cual es el orden de los parametros en la definicion de la funcion.
para utilizarlo, basta con realizar una asginacion de cada argumento en la propia llamada a la funcion.

**ejemplo**
```python
def build_cpu(familia,num,core,frecuencia):
    print(f"""
        la cpu es de la familia {familia},
        con {num_core} cores y con una 
        frecuencia de {frecuencia}
    """)
build_cpu(num_core=4,familia="Intel",frecuencia=2,7)
```
### Argumentos posicionales
Los argumentos son copiados en un orden especifico , en este caso debemos conocer o recordar cual es el orden de los parametros 

**ejemplo**
```python
def build_cpu(familia,num,core,frecuencia):
    print(f"""
        la cpu es de la familia {familia},
        con {num_core} cores y con una 
        frecuencia de {frecuencia}
    """)
# haciendo uso de argumentos posicionales 
build_cpu("intel",4,2.7)
``` 
## Parametros por defecto
es posible especificar **valores por defecto** en los parametros de una funcion , en el caso de que no se poroporcione un valor al argumento en la llamada a la funcion , el parametro correspondiente tomara el valor definido por defecto.
*+ejemplo**
```python
def alumnos(nom,app,estado="aprobado")

alumnos("ruth","castillo")
alumnos("anthony","cruces","desaprobado")
```
## Desempaquetado/Empaquetado de argumentos(tarea)
desempaquetado y empaquetado de argumentos se refiere a la forma en que se manejan los argumentos de una función en algunos lenguajes de programación, como Python.
 
Empaquetado de Argumentos:
 
En el empaquetado de argumentos, se pueden pasar múltiples argumentos a una función como una sola variable. Esto se logra utilizando el operador  *  antes del nombre de la variable en la definición de la función. Por ejemplo:
 
python
 Copiar
def sumar(*numeros):
    total = 0
    for num in numeros:
        total += num
    return total

resultado = sumar(1, 2, 3, 4)
print(resultado)  # Salida: 10
 
 
En este ejemplo, la función  sumar  puede recibir cualquier cantidad de argumentos y los trata como una tupla llamada  numeros .
 
Desempaquetado de Argumentos:
 
El desempaquetado de argumentos se utiliza cuando se quiere pasar una lista o tupla de valores como argumentos individuales a una función. Esto se logra utilizando el operador  *  antes del nombre de la lista o tupla al llamar a la función. Por ejemplo:
 
python
 Copiar
def saludar(nombre, apellido):
    return f"Hola {nombre} {apellido}!"

datos = ["Juan", "Perez"]
mensaje = saludar(*datos)
print(mensaje)  # Salida: Hola Juan Perez!
 
 
En este caso, la lista  datos  se desempaqueta y se pasa como dos argumentos individuales a la función  saludar .
 
El empaquetado y desempaquetado de argumentos son útiles para trabajar con un número variable de argumentos en funciones y para pasar valores contenidos en listas o tuplas como argumentos individuales.
## Funciones internas de phyton (tareas)
En Python, las funciones internas son funciones predefinidas en el lenguaje que están disponibles para su uso sin necesidad de importar ningún módulo adicional. Algunas de las funciones internas más comunes en Python son  print() ,  len() ,  type() ,  range() ,  max() ,  min() , entre otras.
 

Ejemplos de Funciones Internas de Python:
 
1. Función  print() : Imprime un mensaje en la consola.
 
python
 Copiar
print("Hola, mundo!")
 
2. Función  len() : Devuelve la longitud de un objeto (por ejemplo, una lista, tupla, cadena, etc.).
 
python
 Copiar
lista = [1, 2, 3, 4, 5]
print(len(lista))  # Salida: 5
 
3. Función  type() : Devuelve el tipo de un objeto.
 
python
 Copiar
numero = 10
print(type(numero))  # Salida: <class 'int'>
 
4. Función  range() : Genera una secuencia de números.
 
python
 Copiar
for i in range(1, 5):
    print(i)
# Salida: 1, 2, 3, 4
 
5. Función  max()  y  min() : Devuelven el valor máximo y mínimo de una secuencia de números.
 
python
 Copiar
numeros = [10, 5, 20, 15]
print(max(numeros))  # Salida: 20
print(min(numeros))  # Salida: 5
 
 
Estas son solo algunas de las muchas funciones internas útiles que Python proporciona de forma predeterminada. Puedes explorar más funciones internas en la documentación oficial de Python.

## Tipos de funciones
def saludo (nombre)
    print(f#bienvenido {nombre}")
### Funciones anonimas /Funciones lambdass
### funciones callback

### programacion Funcional
la progrmacion funcional no requiere que sepas cmo se desarrolla y ejecutra el procesamiento de la informacion
**ejemplo**
```phyton
#### averiguar sobre map(), filter(), reduce()

# MAP

Map es un contenedor que almacena elementos en pares clave-valor. Es similar a las colecciones en Java, los arreglos asociativos en PHP, o los objetos en JavaScript. Aquí están los principales beneficios de usar map : map solo almacena claves únicas, y las propias claves están ordenadas.

#include <iostream>
#include <map>

using namespace std;

int main (){
  map<char,int> primero;
  
  //inicializando
  primero['a']=10;
  primero['b']=20;
  primero['c']=30;
  primero['d']=40;
  
   map<char, int>::iterator eso;
   for(eso=primero.begin(); eso!=primero.end(); ++eso){
      cout << eso->primero << " => " << eso->segundo << '\n';
   }
   
  return 0;
}

#FILTER 

El método filter en JavaScript, al igual que el método forEach y el método map, es una función que pertenece al objeto array y por ende nos permite manipular sus elementos. Ya hemos visto antes que el método forEach nos permite recorrer los elementos de un array y aplicar a cada uno de ellos una función.

const numeros = [ -5, 7, -10, 22, 3, -1];

    
#REDUCE

El método reduce es un método de arrays en JavaScript que te permite reducir un array a un solo valor, este array puede contener cualquier tipo de dato un número, un cadena de texto, un objeto o incluso un nuevo array.


  let valores = [1, 2, 3, 4, 5];
  let resultado = valores.reduce((a,b) => a+b);
  console.log(resultado);

```
### ACTIVIDAD 
## AVERIGUAR SOBRE MODULOS Y PAQUETES EN PHYTON
Los módulos y paquetes en Python son elementos fundamentales para organizar y estructurar el código de un programa de manera eficiente. Aquí te proporciono información detallada sobre módulos y paquetes en Python, junto con ejemplos ilustrativos:
 
Módulos en Python:
 
- Un módulo en Python es un archivo que contiene definiciones y declaraciones de Python, como funciones, clases y variables.
- Los módulos permiten organizar el código de forma modular para facilitar su reutilización y mantenimiento.
- Para utilizar un módulo en Python, se puede importar utilizando la palabra clave  import .
 
Ejemplo de un módulo en Python llamado  mimodulo.py :
 
python
 Copiar
# mimodulo.py
def saludar(nombre):
    print(f"Hola, {nombre}!")

def sumar(a, b):
    return a + b
 
 
Paquetes en Python:
 
- Un paquete en Python es una colección de módulos relacionados que se almacenan en un directorio.
- Los paquetes permiten organizar y estructurar el código de manera jerárquica.
- Para indicar que un directorio es un paquete en Python, debe contener un archivo especial llamado  _init_.py .
 
Ejemplo de un paquete en Python llamado  mipaquete  que contiene los módulos  modulo1.py  y  modulo2.py :
 

 Copiar
mipaquete/
    _init_.py
    modulo1.py
    modulo2.py
 
 
Contenido del archivo  modulo1.py :
 
python
 Copiar
# modulo1.py
def restar(a, b):
    return a - b
 
 
Contenido del archivo  modulo2.py :
 
python
 Copiar
# modulo2.py
def multiplicar(a, b):
    return a * b
 
 
Para importar y utilizar los módulos y paquetes en Python, se pueden realizar las siguientes operaciones:
 
python
 Copiar
# Importar un módulo
import mimodulo

mimodulo.saludar("Cici")
resultado = mimodulo.sumar(3, 5)
print(resultado)

# Importar un módulo desde un paquete
from mipaquete import modulo1

resultado_resta = modulo1.restar(10, 3)
print(resultado_resta)

# Importar un paquete y un módulo desde el paquete
from mipaquete import modulo2

resultado_multiplicacion = modulo2.multiplicar(4, 6)
print(resultado_multiplicacion)

# DIFERENCIA ENTRE MODULOS Y PAQUETES

En Python, los términos "módulos" y "paquetes" son fundamentales para organizar y estructurar el código de un programa de manera eficiente. Aquí te explico las diferencias entre ambos con ejemplos:
 
Módulos en Python:
 
- Un módulo en Python es un archivo que contiene definiciones y declaraciones de Python. Puede contener funciones, clases y variables.
- Los módulos permiten organizar el código de forma modular para facilitar su reutilización y mantenimiento.
- Para utilizar un módulo en Python, se puede importar utilizando la palabra clave  import .
 
Ejemplo de un módulo en Python llamado  mimodulo.py :
 
python
 Copiar
# mimodulo.py
def saludar(nombre):
    print(f"Hola, {nombre}!")

def sumar(a, b):
    return a + b
 
 
Paquetes en Python:
 
- Un paquete en Python es una colección de módulos relacionados que se almacenan en un directorio.
- Los paquetes permiten organizar y estructurar el código de manera jerárquica.
- Para indicar que un directorio es un paquete en Python, debe contener un archivo especial llamado  _init_.py .
 
Ejemplo de un paquete en Python llamado  mipaquete  que contiene los módulos  modulo1.py  y  modulo2.py :
 

 Copiar
mipaquete/
    _init_.py
    modulo1.py
    modulo2.py
 
 
Contenido del archivo  modulo1.py :
 
python
 Copiar
# modulo1.py
def restar(a, b):
    return a - b
 
 
Contenido del archivo  modulo2.py :
 
python
 Copiar
# modulo2.py
def multiplicar(a, b):
    return a * b
 
 
Para importar y utilizar los módulos y paquetes en Python, se pueden realizar las siguientes operaciones:
 
python
 Copiar
# Importar un módulo
import mimodulo

mimodulo.saludar("Cici")
resultado = mimodulo.sumar(3, 5)
print(resultado)

# Importar un módulo desde un paquete
from mipaquete import modulo1

resultado_resta = modulo1.restar(10, 3)
print(resultado_resta)

# Importar un paquete y un módulo desde el paquete
from mipaquete import modulo2

resultado_multiplicacion = modulo2.multiplicar(4, 6)
print(resultado_multiplicacion)



                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              