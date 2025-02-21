from __future__ import annotations
from dataclasses import dataclass, field
import uuid

import saludTech.modulos.gestor_archivos.dominio.objetos_valor as ov  # TODO: Revisar cuando haya objeto valor
from saludTech.modulos.gestor_archivos.dominio.eventos import (
    ReservaCreada,
    ReservaAprobada,
    ReservaCancelada,
    ReservaPagada,
)
from saludTech.seedwork.dominio.entidades import Locacion, AgregacionRaiz, Entidad


@dataclass
class ImagenMedica(AgregacionRaiz):
    id: uuid.UUID = field(hash=True, default=None)
    url: str = field(default=None)
    metadata: ov.Metadata = field(default_factory=ov.Metadata)

    def crear_imagen_medica(self, imagenMedica: ImagenMedica):
        self.id = imagenMedica.id
        self.url = imagenMedica.url
        self.metadata = imagenMedica.metadata
