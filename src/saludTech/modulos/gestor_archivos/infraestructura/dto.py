from saludTech.config.db import db
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, ForeignKey, Integer, Table
from sqlalchemy.dialects.postgresql import UUID

import uuid

Base = db.declarative_base()


class ImagenMedica(db.Model):
    __tablename__ = "imagen_medica"
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    url = db.Column(db.String(255), nullable=False)


class Metadata(db.Model):
    __tablename__ = "metadata"
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    imagen_medica_id = db.Column(UUID(as_uuid=True), ForeignKey("imagen_medica.id"))
    tipo: str = db.Column(db.String(255), nullable=False)
    formato: str = db.Column(db.String(255), nullable=False)
