class Construccion:
    def __init__(self, nombre, fecha_inicio, fecha_fin):
        self.nombre = nombre
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin

    def duracion(self):
        return self.fecha_fin - self.fecha_inicio