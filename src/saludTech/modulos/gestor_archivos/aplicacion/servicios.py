from saludTech.seedwork.aplicacion.servicios import Servicio
from saludTech.modulos.gestor_archivos.dominio.entidades import ImagenMedica
from saludTech.modulos.gestor_archivos.infraestructura.repositorios import (
    RepositorioImagenMedica,
)
from saludTech.modulos.gestor_archivos.dominio.fabricas import (
    FabricaImagenMedica,
)
from saludTech.modulos.gestor_archivos.infraestructura.fabricas import (
    FabricaRepositorio,
)

from saludTech.seedwork.infraestructura.uow import UnidadTrabajoPuerto as uow

from .dto import ImagenMedicaDTO
from .mapeadores import MapeadorImagenMedica

import asyncio


class ServicioImagenMedica(Servicio):

    def __init__(self):
        self._fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()
        self._fabrica_imagen_medica: FabricaImagenMedica = FabricaImagenMedica()

    @property
    def fabrica_repositorio(self):
        return self._fabrica_repositorio

    @property
    def fabrica_imagenes_medicas(self):
        return self._fabrica_imagen_medica

    def crear_imagen_medica(self, imagen_dto: ImagenMedicaDTO) -> ImagenMedicaDTO:

        print("===========imagen_dto===========")
        print(imagen_dto)
        print("===========imagen_dto===========")

        imagen_medica: ImagenMedica = self.fabrica_imagenes_medicas.crear_objeto(
            imagen_dto,
            MapeadorImagenMedica(),
        )

        print("===========imagen_medica===========")
        print(imagen_medica)
        print("===========imagen_medica===========")

        imagen_medica.crear_imagen_medica(imagen_medica)

        repositorio = self.fabrica_repositorio.crear_objeto(
            RepositorioImagenMedica.__class__
        )
        # uow.clean()  # TODO Eliminar cuando funcione todo
        uow.registrar_batch(repositorio.agregar, imagen_medica)
        uow.savepoint()
        uow.commit()

        return self.fabrica_imagenes_medicas.crear_objeto(
            imagen_medica, MapeadorImagenMedica()
        )
