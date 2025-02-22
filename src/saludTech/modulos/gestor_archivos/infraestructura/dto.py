from saludTech.config.db import db
from sqlalchemy.dialects.postgresql import UUID

import uuid

Base = db.declarative_base()

imagen_medica_metadata = db.Table(
    "imagen_medica_metadata",
    db.Model.metadata,
    db.Column("imagen_medica_id", UUID, db.ForeignKey("imagen_medica.id")),
    db.Column("metadata_tipo", db.String),
    db.Column("metadata_formato", db.String),
    db.ForeignKeyConstraint(
        ["metadata_tipo", "metadata_formato"],
        ["metadata.tipo", "metadata.formato"],
    ),
)


class ImagenMedica(db.Model):
    __tablename__ = "imagen_medica"
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    url = db.Column(db.String(255), nullable=False)
    fecha_creacion = db.Column(db.Numeric, nullable=False)
    metadta_tipo = (db.Column("metadata_tipo", db.String),)
    metadata_formato = (db.Column("metadata_formato", db.String),)
    db.ForeignKeyConstraint(
        ["metadata_tipo", "metadata_formato"],
        ["metadata.tipo", "metadata.formato"],
    ),
    metadata = db.relationship(
        "Metadata",
        back_populates="imagenes",
    )


class Metadata(db.Model):
    __tablename__ = "metadata"
    tipo: str = db.Column(
        db.String(255),
        primary_key=True,
        nullable=False,
    )
    formato: str = db.Column(
        db.String(255),
        primary_key=True,
        nullable=False,
    )
    imagenes = db.relationship(
        "ImagenMedica",
        back_populates="metadata",
    )
