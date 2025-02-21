from __future__ import annotations
from dataclasses import dataclass
from saludTech.seedwork.dominio.objeto_valor import ObjetoValor


@dataclass(frozen=True)
class Metadata(ObjetoValor):
    tipo: str
    formato: str
