from Nodo import Nodo
from Documento import Documento
# Clase Cola para manejar la cola de impresión
class Cola:
    def __init__(self):
        # Inicializa la cola con el frente y el final en None
        self.frente = None
        self.final = None

    def Insertar(self, dato):
        # Agrega un nuevo documento a la cola
        nuevo = Nodo(dato)
        if self.final is None:
            # Si la cola está vacía, el nuevo nodo es tanto el frente como el final
            self.frente = self.final = nuevo
        else:
            # Agrega el nuevo nodo al final de la cola
            self.final.siguiente = nuevo
            self.final = nuevo
            print(f"Elemento '{dato}' insertado")

    def Eliminar(self):
        # Elimina el documento en el frente de la cola
        if self.frente is None:
            print("La cola está vacía!")
            return None
        eliminar = self.frente.dato
        self.frente = self.frente.siguiente

        if self.frente is None:
            # Si la cola queda vacía, también se actualiza el final
            self.final = None
        print(f"Elemento '{eliminar}' eliminado")
        return eliminar

    def Imprimir(self):
        # Imprime todos los documentos en la cola
        if self.frente is None:
            print("Cola está vacía")
        else:
            print("Contenido de la cola desde frente a final:")
            actual = self.frente
            while actual is not None:
                print(actual.dato)
                actual = actual.siguiente

    def DocumentoActual(self):
        # Muestra el documento que se está imprimiendo actualmente
        if self.frente is None:
            print("No hay documento imprimiendo actualmente")
        else:
            print(f"Documento actual: {self.frente.dato}")



# Función para solicitar datos al usuario y agregar un documento a la cola
def solicitar_documento():
    nombre = input("Ingrese el nombre del documento: ")
    usuario = input("Ingrese el nombre del usuario: ")
    paginas = int(input("Ingrese el número de páginas: "))
    return Documento(nombre, usuario, paginas)


# Ejemplo de uso
cola_impresion = Cola()

# Solicitar datos para agregar documentos a la cola
while True:
    cola_impresion.Insertar(solicitar_documento())
    continuar = input("¿Desea agregar otro documento? (s/n): ")
    if continuar.lower() != 's':
        break

# Imprimir el contenido de la cola y el documento actual
cola_impresion.Imprimir()
cola_impresion.DocumentoActual()

# Procesar documentos en la cola
while cola_impresion.frente is not None:
    cola_impresion.Eliminar()
    cola_impresion.DocumentoActual()