class Edificio:
    def __init__(self, nombre, culto,fecha_primeraconsagracion, fecha_segundaconsagracion, BIC, material, estilo):
        self.nombre = nombre
        self.culto = culto
        self.fecha_primeraconsagracion = fecha_primeraconsagracion  
        self.fecha_segundaconsagracion = fecha_segundaconsagracion
        self.BIC = BIC
        self.material = material
        self.estilo = estilo
        self.lugar=None
        self.estapas_construccion=[]

    def agregar_lugar(self, lugar):
        self.lugar = lugar

    def agregar_etapa_construccion(self, etapa):
        self.estapas_construccion.append(etapa) 

    def __str__(self):
        Texto= (
            f"Nombre: {self.nombre}\n"
            f"Culto: {self.culto}\n"
            f"Fecha Primera Consagración: {self.fecha_primeraconsagracion}\n"
            f"Fecha Segunda Consagración: {self.fecha_segundaconsagracion}\n"
            f"BIC: {self.BIC}\n"
            f"Material: {self.material}\n"
            f"Estilo: {self.estilo}\n"
        )
        if self.lugar:
            Texto += f"Lugar: {self.lugar}\n"
        if self.estapas_construccion:
            Texto += "Etapas de Construcción:\n"
            for etapa in self.estapas_construccion:
                Texto += f"  - {etapa}\n"