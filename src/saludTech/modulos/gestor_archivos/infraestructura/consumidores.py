from _pulsar import ConsumerType
from pulsar import Client
from pulsar.schema import AvroSchema
import logging
import traceback


from saludTech.modulos.gestor_archivos.infraestructura.schemas.v1.eventos import (
    EventoImagenCargada,
)
from saludTech.seedwork.infraestructura import utils


def suscribirse_a_eventos():
    cliente = None
    try:
        cliente = Client(f"pulsar://{utils.broker_host()}:6650")
        consumidor = cliente.subscribe(
            "eventos-gestor-archivos",
            consumer_type=ConsumerType.Shared,
            subscription_name="saludTech-sub-eventos",
            schema=AvroSchema(EventoImagenCargada),
        )

        while True:
            mensaje = consumidor.receive()
            print(f"Evento recibido: {mensaje.value().data}")

            consumidor.acknowledge(mensaje)
    except:
        logging.error("ERROR: Suscribiendose al tópico de eventos!")
        traceback.print_exc()
        if cliente:
            cliente.close()
