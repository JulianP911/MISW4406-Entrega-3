from .entidades import Reserva
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
            reserva: Reserva = mapeador.dto_a_entidad(obj)

            self.validar_regla(MinimoUnItinerario(reserva.itinerarios))
            [
                self.validar_regla(RutaValida(ruta))
                for itin in reserva.itinerarios
                for odo in itin.odos
                for segmento in odo.segmentos
                for ruta in segmento.legs
            ]

            return reserva
