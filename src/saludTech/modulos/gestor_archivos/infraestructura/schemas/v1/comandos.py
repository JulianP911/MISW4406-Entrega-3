from pulsar.schema import *
from dataclasses import dataclass, field
from saludTech.seedwork.infraestructura.schema.v1.comandos import ComandoIntegracion


class ComandoAnonimizarImagenPayload(ComandoIntegracion):
    id_imagen = String()
    id_paciente = String()
    url = String()
    fecha_creacion = Long()


class ComandoAnonimizarImagen(ComandoIntegracion):
    data = ComandoAnonimizarImagenPayload()
