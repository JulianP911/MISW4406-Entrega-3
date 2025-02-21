from dataclasses import dataclass
from saludTech.seedwork.dominio.eventos import EventoDominio


@dataclass
class ArchivoPublicado(EventoDominio):
    url: str = None
    id_paciente: uuid.UUID = None
