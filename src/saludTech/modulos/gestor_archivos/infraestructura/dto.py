from saludTech.config.db import db
from sqlalchemy.dialects.postgresql import UUID

import uuid

Base = db.declarative_base()

imagen_medica_metadata = db.Table(
    "imagen_medica_metadata",
    db.Model.metadata,
    db.Column(
        "imagen_medica_id", db.Text(length=36), db.ForeignKey("imagen_medica.id")
    ),
    db.Column("metadata_tipo", db.String),
    db.Column("metadata_formato", db.String),
    db.ForeignKeyConstraint(
        ["metadata_tipo", "metadata_formato"],
        ["imagen_metadata.tipo", "imagen_metadata.formato"],
    ),
)


class ImagenMedica(db.Model):
    __tablename__ = "imagen_medica"
    id = db.Column(
        "id", db.Text(length=36), default=lambda: str(uuid.uuid4()), primary_key=True
    )
    url = db.Column(db.String(255), nullable=False)
    imagen_metadata = db.relationship(
        "ImagenMetadata", secondary=imagen_medica_metadata, back_populates="imagenes"
    )


class ImagenMetadata(db.Model):
    __tablename__ = "imagen_metadata"
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
        secondary=imagen_medica_metadata,
        back_populates="imagen_metadata",
    )
