from edificio import Edificio
from lugar import Lugar
from construccion import Construccion

Santiago= Lugar("Santiago de Compostela", "Galicia", "España")
Construccion1= Construccion("Construcción Inicial", 1075, 1122)
Construccion2= Construccion("Ampliación Gótica", 1168, 'Nulo')

Catedral_Santiago= Edificio(
    nombre="Catedral de Santiago de Compostela",
    culto="Católico",
    fecha_primeraconsagracion=1128,
    fecha_segundaconsagracion=1211,
    BIC=1896,
    material="Granito",
    estilo="Románico, Gótico, Barroco, Plateresco, Neoclasico"
)