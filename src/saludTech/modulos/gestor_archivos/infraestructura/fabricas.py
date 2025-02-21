from dataclasses import dataclass, field
from saludTech.seedwork.dominio.fabricas import Fabrica
from saludTech.seedwork.dominio.repositorios import Repositorio
from saludTech.modulos.gestor_archivos.dominio.repositorios import (
    RepositorioProveedores,
    RepositorioReservas,
)  # TODO: Cambiar
from .repositorios import RepositorioReservasSQLite, RepositorioProveedoresSQLite
from .excepciones import ExcepcionFabrica


@dataclass
class FabricaRepositorio(Fabrica):
    def crear_objeto(self, obj: type, mapeador: any = None) -> Repositorio:
        if obj == RepositorioReservas.__class__:
            return RepositorioReservasSQLite()
        elif obj == RepositorioProveedores.__class__:
            return RepositorioProveedoresSQLite()
        else:
            raise ExcepcionFabrica()
