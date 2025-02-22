from saludTech.seedwork.aplicacion.handlers import Handler
from saludTech.modulos.gestor_archivos.infraestructura.despachadores import Despachador


class HandlerImagenMedicaIntegracion(Handler):

    @staticmethod
    def handle_archivo_publicado(comando):
        despachador = Despachador()
        despachador.publicar_comando(comando, "comandos-anonimizar-imagen")
