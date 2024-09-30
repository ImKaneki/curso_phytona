# crear una clase de alumnos con los atributos que usted crea por conveniente
# luego instanciara a 4 alumnos

#ejercicio del profesor
class Alumno:
  def init(self, nombre,dni,edad,email,programa_estudio="APSTI"):
    self.nombre=nombre
    self.dni=dni
    self.email=email
    self.programa_estudio=programa_estudio

maricielo=Alumno("maricielo",76493681,14,"yo@gmail")
print(maricielo.programa_estudio)
mercedes=Alumno("meche",62628787,15,"tu@gmail.com","enfermeria")
print(mercedes.programa_estudio)

#metodos
def escribir(self):
  print("estoy escribiendo")
def tarea(self,nombre_docente):
  print("haciendo la tarea de:",nombre_docente)
def terminar_tarea(self):
print("terminando tarea anterior")

maricielo=Alumno("maricielo",75869321,14),"yo@gmail.com"
maricielo.tarea("alicia")
maricielo.terminar_tarea()
maricielo.tarea("alvarez")
print(maricielo.programa_estudio)
mercedes=alumno(meche,62628787,15,"tu@gmail.com","enfermeria")
print(mercedes.programa_estudio)    |


