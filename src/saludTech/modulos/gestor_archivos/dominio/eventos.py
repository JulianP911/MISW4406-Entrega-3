from dataclasses import dataclass
from saludTech.seedwork.dominio.eventos import EventoDominio
import uuid


@dataclass
class ArchivoPublicado(EventoDominio):
    url: str = None
    id_paciente: uuid.UUID = None
