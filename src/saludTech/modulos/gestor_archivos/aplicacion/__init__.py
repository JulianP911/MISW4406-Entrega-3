from pydispatch import dispatcher

from .handlers import HandlerImagenMedicaIntegracion

from saludTech.modulos.gestor_archivos.dominio.eventos import (
    ArchivoPublicado,
)

dispatcher.connect(
    HandlerImagenMedicaIntegracion.handle_archivo_publicado,
    signal=f"{ArchivoPublicado.__name__}Integracion",
)
