class Documento:
    def __init__(self, nombre, usuario, paginas):
        self.nombre = nombre
        self.usuario = usuario
        self.paginas = paginas

    def __str__(self):
        return f"{self.nombre} ({self.paginas} pág.) por {self.usuario}"