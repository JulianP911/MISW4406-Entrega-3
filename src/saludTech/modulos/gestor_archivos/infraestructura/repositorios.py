from saludTech.config.db import db
from saludTech.modulos.gestor_archivos.dominio.repositorios import (
    RepositorioReservas,
    RepositorioProveedores,
)
from saludTech.modulos.gestor_archivos.dominio.objetos_valor import (  # TODO: Revisar cuando haya dominio
    NombreAero,
    Odo,
    Leg,
    Segmento,
    Itinerario,
    CodigoIATA,
)
from saludTech.modulos.gestor_archivos.dominio.entidades import (
    Proveedor,
    Aeropuerto,
    Reserva,
)  # TODO: Revisar cuando haya dominio
from saludTech.modulos.gestor_archivos.dominio.fabricas import (
    FabricaVuelos,
)  # TODO: Revisar cuando haya dominio
from .dto import ImagenMedica as ImagenMedicaDTO
from .mapeadores import MapeadorImagenMedica
from uuid import UUID


class RepositorioImageneMedicaSQLite(RepositorioProveedores):
    def agregar(self, entity: Reserva):
        # TODO
        raise NotImplementedError


class RepositorioMetadataSQLite(RepositorioProveedores):
    def agregar(self, entity: Reserva):
        # TODO
        raise NotImplementedError
