import pulsar
from pulsar.schema import AvroSchema

from saludTech.modulos.gestor_archivos.infraestructura.schemas.v1.comandos import (
    ComandoAnonimizarImagen,
    ComandoAnonimizarImagenPayload,
)
from saludTech.seedwork.infraestructura import utils

import datetime

epoch = datetime.datetime.utcfromtimestamp(0)


def unix_time_millis(dt):
    return (dt - epoch).total_seconds() * 1000.0


class Despachador:
    def _publicar_mensaje(self, mensaje, topico, schema):
        print("===========MENSAJE===========")
        print(mensaje)
        print("===========MENSAJE===========")

        print("===========TOPICO===========")
        print(topico)
        print("===========TOPICO===========")

        print("===========SCHEMA===========")
        print(schema)
        print("===========SCHEMA===========")

        cliente = pulsar.Client(f"pulsar://{utils.broker_host()}:6650")
        publicador = cliente.create_producer(topico, schema=schema)
        publicador.send(mensaje)
        cliente.close()

    def publicar_comando(self, comando, topico):
        payload = ComandoAnonimizarImagenPayload(id=comando.id, url=comando.url)
        comando_integracion = ComandoAnonimizarImagen(data=payload)

        print("===========PAYLOAD===========")
        print(payload)
        print("===========PAYLOAD===========")

        print("===========COMANDO INTEGRACION===========")
        print(comando_integracion)
        print("===========COMANDO INTEGRACION===========")

        self._publicar_mensaje(
            comando_integracion, topico, AvroSchema(ComandoAnonimizarImagen)
        )
