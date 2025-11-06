"""1. Clase Libro
Esta es simple. Un libro solo necesita saber quién es y si está disponible.

En el __init__, debe recibir titulo y autor.

Debe tener un atributo disponible que siempre empiece como True.

Crea un método __str__(self) que devuelva f"{self.titulo} por {self.autor}" (¡así se imprimirá bonito!).

2. Clase Socio
Vamos a tomar la clase Socio que creaste ayer (la que hereda de Persona) y le añadiremos algo: la capacidad de recordar los libros que tiene.

Abre el archivo de ayer (el de Persona y Socio).

En el __init__ de Socio, además de super().__init__(...) y self.numero_socio, añade:

self.libros_prestados = [] (una lista vacía).

Crea un método mostrar_libros(self) que imprima los libros que tiene el socio. Si la lista está vacía, debe imprimir "{self.nombre} no tiene libros prestados.". Si tiene libros, debe recorrer la lista e imprimirlos.

3. Clase Biblioteca (La Orquestadora)
Esta es la clase principal. Gestiona los objetos Libro y Socio.

En el __init__, debe crear dos listas vacías:

self.catalogo = [] (para guardar objetos Libro).

self.socios = [] (para guardar objetos Socio).

Método registrar_libro(self, libro):

Recibe un objeto libro.

Lo añade a la lista self.catalogo.

Imprime f"Libro '{libro.titulo}' registrado."

Método registrar_socio(self, socio):

Recibe un objeto socio.

Lo añade a la lista self.socios.

Imprime f"Socio {socio.nombre} registrado."

Método prestar_libro(self, socio, libro):

Recibe un objeto socio y un objeto libro.

Lógica:

Comprueba si el libro está disponible (si libro.disponible es True).

Si lo está:

Cambia libro.disponible a False.

Añade el libro a la lista socio.libros_prestados.

Imprime f"'{libro.titulo}' prestado a {socio.nombre}."

Si no lo está (si es False):

Imprime f"Error: '{libro.titulo}' no está disponible."

Método devolver_libro(self, socio, libro):

Recibe un objeto socio y un objeto libro.

Lógica:

Comprueba si el libro está en la lista socio.libros_prestados.

Si lo está:

Cambia libro.disponible a True.

Elimina el libro de la lista socio.libros_prestados (pista: usa .remove()).

Imprime f"'{libro.titulo}' devuelto por {socio.nombre}."

Si no lo está:

Imprime f"Error: {socio.nombre} no tiene ese libro."

Prueba (Tu if __name__=="__main__":)
Crea un objeto Biblioteca.

Crea dos objetos Libro (ej. libro1 = Libro("1984", "Orwell"), libro2 = Libro("El Quijote", "Cervantes")).

Crea un objeto Socio (ej. socio1 = Socio("Juan", "Pérez", 123)).

Registra los libros y el socio en la biblioteca.

Prueba 1: Presta libro1 a socio1 (debería funcionar).

Prueba 2: Intenta prestar libro1 a socio1 de nuevo (debería fallar, "no disponible").

Prueba 3: Pide a socio1 que muestre sus libros (socio1.mostrar_libros()).

Prueba 4: Devuelve libro1 (debería funcionar).

Prueba 5: Intenta devolver libro1 de nuevo (debería fallar, "no tiene ese libro").

Prueba 6: Pide a socio1 que muestre sus libros (debería estar vacío)."""

# creamos la clase libro que recibe los parametros titulo y autor
class Libro:
    def __init__(self, titulo, autor):
        self.titulo=titulo
        self.autor=autor
        self.disponible=True
    # crea un metodo que devuelva el string de titulo y autor
    def __str__(self):
        return f"{self.titulo} por {self.autor}"


# crea la clase socio (copiada del ejercicio anterior)
"""# crea una clase padre llamada Persona"""
class Persona:
    def __init__(self, nombre, apellido):
        self.nombre=nombre
        self.apellido=apellido
    
    """# metodo para describir a la persona"""
    def describir(self):
        print(f"Nombre: {self.nombre} {self.apellido}")

"""# crea una clase hija llamada Socio que herede de Persona"""
class Socio(Persona):
    def __init__(self, nombre, apellido, numero_socio):
                super().__init__(nombre, apellido)
                self.numero_socio=numero_socio
                # crea una lista vacia
                self.libros_prestados=[]
    """# sobrescribir el metodo describir"""
    def describir(self):
        print(f"Socio Nº {self.numero_socio}: {self.nombre} {self.apellido}")
    # crea un metodo mostrar libros
    def mostrar_libros(self):
        # una lista vacia se considera False
        if not self.libros_prestados:
            print(f"{self.nombre} no tiene libros prestados")
        else:
            print(f"el socio {self.nombre} tiene prestados los siguientes libros:", end=" ")
            """ for libro in self.libros_prestados:
            print(f"{libro}", end=", ")
            print()"""  #este metodo me da como resultado una coma al final y no es lo que queremos
            # para solucionarlo usaremos el metodo str.join(), que coge una lista de strings y los une con el string que yo le diga
            # por eso es importante que lo impreso sea un str

            # primero creamos una lista por comprension usando el meto str de la clase Libro
            lista_libros=[str(libro) for libro in self.libros_prestados]
            #imprimimos los elementos de la lista usando el metodo .join() y hacemos que si hay mas de un elemento se separen por una coma
            print(", ".join(lista_libros))
    
# --------------Se añade socios-vip------------------
class SociosVip(Socio):
    def __init__(self, nombre, apellido, numero_socio):
        super().__init__(nombre, apellido, numero_socio)
        # añadimos el atributo de limite de libros
        self.limite_libros=10
    
    # sobrescribimos el metodo describir
    def describir(self):
        print(f"Socio vip (Nº{self.numero_socio}: {self.nombre} {self.apellido}) (limite:{self.limite_libros} libros)")


#--------------- vamos con la clase principal-------------
class Biblioteca:
    """    #  creamos dos listas vacias para guardar los objetos de Libro y Socio
    def __init__(self, libro, socio):
        self.libro=libro
        self.socio=socio
        self.catalogo=[]
        self.socios=[] """  
    """El objetivo de la clase Biblioteca es ser una "Orquestadora". Es un edificio que, cuando lo "construyes"
    (cuando llamas a __init__), empieza vacío.

    Error 1: Tu __init__ pide un libro y un socio como argumentos. Esto es incorrecto. 
    La biblioteca no se crea con un libro, se crea vacía y luego se le registrar_libro().

    Errores 2 y 3: Estás guardando un único libro en self.libro y un único socio en self.socio. 
    Esto va en contra de la idea de la biblioteca, que debe guardar colecciones (listas) de libros y socios"""
# la manera correcta:
    def __init__(self):
         self.catalogo=[]
         self.socios=[]
    

    # creamos un metodo para registrar libros (.titulo viene del objeto al crearse con la clase libro que le asignamos un parametro llamado titulo)
    def registrar_libro(self, libro):
        self.catalogo.append(libro)
        print(f"Libro '{libro.titulo}' registrado")
    
    # creamos un metodo para registarr un socio
    def registrar_socio(self, socio):
        self.socios.append(socio)
        print(f"Socio {socio.nombre} registrado")

    #crear el metodo prestar libro
    def prestar_libro(self, socio, libro):
        if libro.disponible:
            libro.disponible=False
            socio.libros_prestados.append(libro)
            print(f"{libro.titulo} prestado a {socio.nombre}")
        else:
             print(f"Error: {libro.titulo} no disponible")
    
    # metodo para devolver libro:
    def devolver_libro(self, socio, libro):
        if libro in socio.libros_prestados:
            socio.libros_prestados.remove(libro)
            libro.disponible=True
            print(f"el libro {libro.titulo} ha sido devuelto con exito por {socio.nombre}")
        else:
            print(f"Error: {socio.nombre} no tiene ese libro")




# -----------pasamos a probar el codigo------------------


if __name__=="__main__":
    # creamos la biblioteca
    biblioteca=Biblioteca()

    # creamos los libros y el socio
    libro1 = Libro("1984", "Orwell")
    libro2 = Libro("El Quijote", "Cervantes")
    socio1 = Socio("Juan", "Pérez", 123)

    # los agregamos a la biblioteca
    biblioteca.registrar_libro(libro1)
    biblioteca.registrar_libro(libro2)
    biblioteca.registrar_socio(socio1)

    #intentamos prestar libros
    biblioteca.prestar_libro(socio1, libro1)
    biblioteca.prestar_libro(socio1, libro1)

    # mostramos libros
    socio1.mostrar_libros()

    # devolver libro
    biblioteca.devolver_libro(socio1, libro2)
    biblioteca.prestar_libro(socio1, libro2)
    biblioteca.devolver_libro(socio1, libro1)
    biblioteca.devolver_libro(socio1, libro1)

    # volvemos a mirar los libro del socio
    socio1.mostrar_libros()


