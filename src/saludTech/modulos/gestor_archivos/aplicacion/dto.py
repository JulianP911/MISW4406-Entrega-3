from dataclasses import dataclass, field
from saludTech.seedwork.aplicacion.dto import DTO


@dataclass(frozen=True)
class MetadataDTO(DTO):
    tipo: str
    formato: str


@dataclass(frozen=True)
class ImagenMedicaDTO(DTO):
    id: str = field(default=None)
    url: str = field(default=None)
    metadata: MetadataDTO = field(default_factory=MetadataDTO)
    fecha_creacion: str = field(default_factory=str)
    fecha_actualizacion: str = field(default_factory=str)
