from pulsar.schema import Record, String, Long
from saludTech.seedwork.infraestructura.schema.v1.eventos import EventoIntegracion


class ImagenCargadaPayload(Record):
    id = String()
    url = String()


class EventoImagenCargada(EventoIntegracion):
    data = ImagenCargadaPayload()
