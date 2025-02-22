from .entidades import ImagenMedica
from .excepciones import TipoObjetoNoExisteEnDominioVuelosExcepcion
from saludTech.seedwork.dominio.repositorios import Mapeador, Repositorio
from saludTech.seedwork.dominio.fabricas import Fabrica
from saludTech.seedwork.dominio.entidades import Entidad
from dataclasses import dataclass


@dataclass
class _FabricaImagenMedica(Fabrica):
    def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
        if isinstance(obj, Entidad):
            return mapeador.entidad_a_dto(obj)
        else:
            imagen_medica: ImagenMedica = mapeador.dto_a_entidad(obj)

            return imagen_medica


@dataclass
class FabricaImagenMedica(Fabrica):
    def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
        if mapeador.obtener_tipo() == ImagenMedica.__class__:
            fabrica_imagen_medica = _FabricaImagenMedica()
            return fabrica_imagen_medica.crear_objeto(obj, mapeador)
        else:
            raise TipoObjetoNoExisteEnDominioVuelosExcepcion()

    def __call__(self, obj: any, mapeador: Mapeador) -> any:
        return self.crear_objeto(obj, mapeador)
