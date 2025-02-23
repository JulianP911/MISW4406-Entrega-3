from saludTech.seedwork.aplicacion.dto import Mapeador as AppMap
from saludTech.seedwork.dominio.repositorios import Mapeador as RepMap
from saludTech.modulos.gestor_archivos.dominio.entidades import ImagenMedica
from saludTech.modulos.gestor_archivos.dominio.objeto_valor import Metadata
from .dto import MetadataDTO, ImagenMedicaDTO


class MapeadorImagenMedicaDTOJson(AppMap):
    def externo_a_dto(self, externo: dict) -> ImagenMedicaDTO:
        imagen_medica_dto = ImagenMedicaDTO(
            url=externo["url"],
            metadata=MetadataDTO(
                tipo=externo["metadata"]["tipo"],
                formato=externo["metadata"]["formato"],
            ),
        )

        return imagen_medica_dto

    def dto_a_externo(self, dto: ImagenMedicaDTO) -> dict:
        return dto.__dict__


class MapeadorImagenMedica(RepMap):
    _FORMATO_FECHA = "%Y-%m-%dT%H:%M:%SZ"

    def _procesar_metadata(self, metadata_dto: MetadataDTO) -> Metadata:
        return Metadata(metadata_dto.tipo, metadata_dto.formato)

    def obtener_tipo(self) -> type:
        return ImagenMedica.__class__

    def entidad_a_dto(self, entidad: ImagenMedica) -> ImagenMedicaDTO:
        print("=========DESDE MAPEADOR IMAGEN MEDICA==========")
        print(entidad)
        print("=========DESDE MAPEADOR IMAGEN MEDICA==========")
        fecha_creacion = None
        fecha_actualizacion = entidad.fecha_actualizacion.strftime(self._FORMATO_FECHA)

        return ImagenMedicaDTO(
            entidad.id,
            entidad.url,
            entidad.metadata,
            fecha_actualizacion=fecha_actualizacion,
            fecha_creacion=fecha_creacion,
        )

    def dto_a_entidad(self, dto: ImagenMedicaDTO) -> ImagenMedica:
        return ImagenMedica(
            id=dto.id,
            url=dto.url,
            metadata=MetadataDTO(
                dto.metadata.tipo,
                dto.metadata.formato,
            ),
        )
