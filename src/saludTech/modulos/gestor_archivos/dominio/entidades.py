from __future__ import annotations
from dataclasses import dataclass, field
import uuid

import saludTech.modulos.gestor_archivos.dominio.objeto_valor as ov
from saludTech.seedwork.dominio.entidades import AgregacionRaiz


@dataclass
class ImagenMedica(AgregacionRaiz):
    id: uuid.UUID = field(hash=True, default=None)
    url: str = field(default=None)
    fecha_creacion: str = field(default=None)
    metadata: ov.Metadata = field(default_factory=ov.Metadata)

    # TODO: Revisar si es necesario
    def crear_imagen_medica(self, imagenMedica: ImagenMedica):
        self.id = imagenMedica.id
        self.url = imagenMedica.url
        self.fecha_creacion = imagenMedica.fecha_creacion
        self.metadata = imagenMedica.metadata
