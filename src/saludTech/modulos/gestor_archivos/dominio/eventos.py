from dataclasses import dataclass
from saludTech.seedwork.dominio.eventos import EventoDominio
import uuid


@dataclass
class ArchivoPublicado(EventoDominio):
    id: str = None
    url: str = None
