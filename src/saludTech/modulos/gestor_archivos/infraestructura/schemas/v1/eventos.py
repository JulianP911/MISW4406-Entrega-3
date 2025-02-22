from pulsar.schema import Record, String, Long
from saludTech.seedwork.infraestructura.schema.v1.eventos import EventoIntegracion


class ImagenCargadaPayload(Record):
    id_imagen = String()
    id_paciente = String()
    url = String()
    fecha_creacion = Long()


class EventoImagenCargada(EventoIntegracion):
    data = ImagenCargadaPayload()
