from saludTech.seedwork.aplicacion.servicios import Servicio
from saludTech.modulos.gestor_archivos.dominio.fabricas import (
    FabricaImagenMedica,
)
from saludTech.modulos.gestor_archivos.infraestructura.fabricas import (
    FabricaRepositorio,
)

from .dto import ImagenMedicaDTO

import asyncio


class ServicioImagenMedica(Servicio):

    def __init__(self):
        self._fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()
        self._fabrica_imagen_medica: FabricaImagenMedica = FabricaImagenMedica()

    def crear_imagen_medica(self, imagen_dto: ImagenMedicaDTO) -> ImagenMedicaDTO:
        pass
