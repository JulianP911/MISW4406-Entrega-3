from dataclasses import dataclass, field
from saludTech.seedwork.dominio.fabricas import Fabrica
from saludTech.seedwork.dominio.repositorios import Repositorio, EventPayload
from saludTech.modulos.gestor_archivos.dominio.repositorios import (
    RepositorioImagenMedica,
)
from .repositorios import RepositorioImageneMedicaSQLite
from .excepciones import ExcepcionFabrica
from .schemas.v1.comandos import ComandoAnonimizarImagenPayload


@dataclass
class FabricaRepositorio(Fabrica):
    def crear_objeto(self, obj: type, mapeador: any = None) -> Repositorio:
        if obj == RepositorioImagenMedica.__class__:
            return RepositorioImageneMedicaSQLite()
        else:
            raise ExcepcionFabrica()


@dataclass
class FabricaEventosPayload(Fabrica):
    def crear_objeto(self, obj, mapeador=None) -> EventPayload:
        if obj == ComandoAnonimizarImagenPayload.__class__:
            return ComandoAnonimizarImagenPayload()
        else:
            raise ExcepcionFabrica()
