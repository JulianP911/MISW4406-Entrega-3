import pulsar
from pulsar.schema import *

from saludTech.modulos.vuelos.infraestructura.schema.v1.eventos import (
    EventoReservaCreada,
    ReservaCreadaPayload,
)
from saludTech.modulos.vuelos.infraestructura.schema.v1.comandos import (
    ComandoCrearReserva,
    ComandoCrearReservaPayload,
)

from saludTech.seedwork.infraestructura import utils

import datetime

epoch = datetime.datetime.utcfromtimestamp(0)


def unix_time_millis(dt):
    return (dt - epoch).total_seconds() * 1000.0


class Despachador:
    def _publicar_mensaje(self, mensaje, topico, schema):
        cliente = pulsar.Client(f"pulsar://{utils.broker_host()}:6650")
        publicador = cliente.create_producer(
            topico, schema=AvroSchema(EventoReservaCreada)
        )
        publicador.send(mensaje)
        cliente.close()

    def publicar_comando(self, comando, topico):
        # TODO Debe existir un forma de crear el Payload en Avro con base al tipo del comando
        payload = ComandoCrearReservaPayload(
            id_usuario=str(comando.id_usuario)
            # agregar itinerarios
        )
        comando_integracion = ComandoAnonimizarImagen(data=payload)
        self._publicar_mensaje(
            comando_integracion, topico, AvroSchema(ComandoAnonimizarImagen)
        )
