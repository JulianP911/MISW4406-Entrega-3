from saludTech.modulos.gestor_archivos.dominio.eventos import (
    ArchivoPublicado,
)  # TODO: Revisar porque es un comando
from saludTech.seedwork.aplicacion.handlers import Handler
from saludTech.modulos.gestor_archivos.infraestructura.despachadores import Despachador


class HandlerReservaIntegracion(Handler):

    @staticmethod
    def handle_anonimizar_archivo(comando):
        despachador = Despachador()
        despachador.publicar_comando(comando, "comandos-anonimizar-imagen")
