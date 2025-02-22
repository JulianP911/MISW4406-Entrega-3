from saludTech.config.db import db
from saludTech.modulos.gestor_archivos.dominio.repositorios import (
    RepositorioImagenMedica,
)
from saludTech.modulos.gestor_archivos.dominio.entidades import ImagenMedica
from .dto import ImagenMedica as ImagenMedicaDTO
from .mapeadores import MapeadorImagenMedica
from uuid import UUID


class RepositorioImageneMedicaSQLite(RepositorioImagenMedica):
    def agregar(self, entity: ImagenMedica):
        raise NotImplementedError
