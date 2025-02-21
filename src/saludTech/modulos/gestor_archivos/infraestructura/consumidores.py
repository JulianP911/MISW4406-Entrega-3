import pulsar, _pulsar
from pulsar.schema import *
import uuid
import time
import logging
import traceback


from saludTech.modulos.vuelos.infraestructura.schema.v1.eventos import (
    EventoReservaCreada,
)
from saludTech.modulos.vuelos.infraestructura.schema.v1.comandos import (
    ComandoCrearReserva,
)
from saludTech.seedwork.infraestructura import utils


def suscribirse_a_eventos():
    cliente = None
    try:
        cliente = pulsar.Client(f"pulsar://{utils.broker_host()}:6650")
        consumidor = cliente.subscribe(
            "eventos-gestor-archivos",
            consumer_type=_pulsar.ConsumerType.Shared,
            subscription_name="saluTech-sub-eventos",
            schema=AvroSchema(EventoReservaCreada),  # TODO: Revisar
        )

        while True:
            mensaje = consumidor.receive()
            print(f"Evento recibido: {mensaje.value().data}")

            consumidor.acknowledge(mensaje)

        cliente.close()
    except:
        logging.error("ERROR: Suscribiendose al tópico de eventos!")
        traceback.print_exc()
        if cliente:
            cliente.close()
