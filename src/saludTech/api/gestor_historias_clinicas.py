from flask import redirect, render_template, request, session, url_for
from flask import Response
import json

from saludTech.modulos.gestor_archivos.aplicacion.servicios import ServicioImagenMedica
import saludTech.seedwork.presentacion.api as api
from saludTech.seedwork.dominio.excepciones import ExcepcionDominio
from saludTech.modulos.gestor_archivos.aplicacion.mapeadores import (
    MapeadorImagenMedicaDTOJson,
)

bp = api.crear_blueprint("gestor_archivos", "/gestor_archivos")


@bp.route("/imagen_medica", methods=("POST",))
def crear_imagen_medica():
    try:
        imagen_medica_dict = request.json

        map_imagen_medica = MapeadorImagenMedicaDTOJson()
        imagen_medica_dto = map_imagen_medica.externo_a_dto(imagen_medica_dict)

        servicio_imagen_medica = ServicioImagenMedica()
        dto_final = servicio_imagen_medica.crear_imagen_medica(imagen_medica_dto)

        return map_imagen_medica.dto_a_externo(dto_final)

    except ExcepcionDominio as e:
        return Response(
            json.dumps(dict(error=str(e))), status=400, mimetype="application/json"
        )
