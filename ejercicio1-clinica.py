# Paso 1: Creamos la clase nodo para representar cada paciente

from Nodo import Nodo
# Creamos la clase Cola
class Cola:
    def __init__(self):
        self.frente = None  # Primer nodo (el que será atendido)
        self.final = None   # Último nodo (el más reciente en llegar)

    # Método para verificar si la cola está vacía
    def esta_vacia(self):
        return self.frente is None

    # Método para agregar un paciente a la cola
    def encolar(self, dato):
        nuevo = Nodo(dato)
        if self.esta_vacia():
            self.frente = self.final = nuevo
        else:
            self.final.siguiente = nuevo
            self.final = nuevo
        print(f"✅ {dato} ha sido registrado en la cola.")

    # Método para atender (eliminar) al siguiente paciente
    def desencolar(self):
        if self.esta_vacia():
            print("⚠️ No hay pacientes en espera.")
        else:
            atendido = self.frente.dato
            self.frente = self.frente.siguiente
            if self.frente is None:
                self.final = None
            print(f"🩺 Se ha atendido a {atendido}.")

    # Método para mostrar la cola actual
    def mostrar(self):
        if self.esta_vacia():
            print("📭 No hay pacientes en la cola.")
        else:
            print("📋 Lista de pacientes en espera:")
            actual = self.frente
            while actual:
                print(f"• {actual.dato}")
                actual = actual.siguiente

# Crear el menu
def mostrar_menu():
    print("\n--- Menú de atención clínica ---")
    print("1. Registrar nuevo paciente")
    print("2. Atender siguiente paciente")
    print("3. Ver lista de espera")
    print("4. Salir")


cola_clinica = Cola()

while True:
    mostrar_menu()
    opcion = input("Seleccione una opción (1-4): ")

    match opcion:
        case '1':
            
            try:
                nombre = input("Ingrese el nombre del paciente: ")
                if not nombre.isalpha():
                    raise ValueError
            except:
                nombre = input("Error. El nombre solo puede contener letras. Introduzca un nuevo nombre: ")
            if nombre.isalpha():
                cola_clinica.encolar(nombre)
            else: 
                print("El nombre no pudo ser registrado, intentelo de nuevo")
        case '2':
            cola_clinica.desencolar()
        case '3':
            cola_clinica.mostrar()
        case '4':
            print("👋 Gracias por usar el sistema de atención.")
            break
        case _:
            print("❌ Opción inválida. Intente de nuevo.")