from .entidades import ImagenMedica
from .reglas import MinimoUnItinerario, RutaValida
from .excepciones import TipoObjetoNoExisteEnDominioVuelosExcepcion
from saludTech.seedwork.dominio.repositorios import Mapeador, Repositorio
from saludTech.seedwork.dominio.fabricas import Fabrica
from saludTech.seedwork.dominio.entidades import Entidad
from dataclasses import dataclass


@dataclass
class FabricaImagenMedica(Fabrica):
    def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
        if isinstance(obj, Entidad):
            return mapeador.entidad_a_dto(obj)
        else:
            imagen_medica: ImagenMedica = mapeador.dto_a_entidad(obj)

            return imagen_medica
