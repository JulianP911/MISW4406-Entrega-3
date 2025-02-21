# TODO: Completar cuando haya domino

from saludTech.seedwork.dominio.repositorios import Mapeador
from saludTech.modulos.gestor_archivos.dominio.entidades import ImagenMedica


class MapeadorImagenMedica(Mapeador):
    def obtener_tipo(self) -> type:
        return ImagenMedica.__class__

    def entidad_a_dto(self, entidad: ImagenMedica) -> any:
        return {
            "id": str(entidad.id),
            "id_paciente": str(entidad.id_paciente),
            "id_estudio": str(entidad.id_estudio),
            "id_imagen": str(entidad.id_imagen),
            "url": entidad.url,
            "fecha_creacion": unix_time_millis(entidad.fecha_creacion),
        }

    def dto_a_entidad(self, dto: any) -> ImagenMedica:
        return ImagenMedica(
            id=UUID(dto["id"]),
            id_paciente=UUID(dto["id_paciente"]),
            id_estudio=UUID(dto["id_estudio"]),
            id_imagen=UUID(dto["id_imagen"]),
            url=dto["url"],
            fecha_creacion=datetime.datetime.utcfromtimestamp(
                dto["fecha_creacion"] / 1000
            ),
        )


class MapeadorMetadata(Mapeador):
    def obtener_tipo(self) -> type:
        return ImagenMedica.__class__

    def entidad_a_dto(self, entidad: ImagenMedica) -> any:
        return {
            "id": str(entidad.id),
            "id_paciente": str(entidad.id_paciente),
            "id_estudio": str(entidad.id_estudio),
            "id_imagen": str(entidad.id_imagen),
            "url": entidad.url,
            "fecha_creacion": unix_time_millis(entidad.fecha_creacion),
        }

    def dto_a_entidad(self, dto: any) -> ImagenMedica:
        return ImagenMedica(
            id=UUID(dto["id"]),
            id_paciente=UUID(dto["id_paciente"]),
            id_estudio=UUID(dto["id_estudio"]),
            id_imagen=UUID(dto["id_imagen"]),
            url=dto["url"],
            fecha_creacion=datetime.datetime.utcfromtimestamp(
                dto["fecha_creacion"] / 1000
            ),
        )
