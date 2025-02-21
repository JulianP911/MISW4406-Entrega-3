from pulsar.schema import *
from dataclasses import dataclass, field
from saludTech.seedwork.infraestructura.schema.v1.comandos import ComandoIntegracion


class ComandoCrearReserva(ComandoIntegracion):
    data = ComandoAnonimizarImagen()  # TODO: Revisar
