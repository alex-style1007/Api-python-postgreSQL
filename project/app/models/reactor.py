from sqlalchemy import Column, String, Integer, Numeric, ForeignKey, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class TipoReactor(Base):
    __tablename__ = 'tipos_reactor'
    __table_args__ = {'schema': 'examen'}

    id = Column(Integer, primary_key=True)
    tipo = Column(String(50), nullable=False)

class Pais(Base):
    __tablename__ = 'paises'
    __table_args__ = {'schema': 'examen'}

    id = Column(Integer, primary_key=True)
    pais = Column(String(50), nullable=False, unique=True)

class Ubicacion(Base):
    __tablename__ = 'ubicacion'
    __table_args__ = {'schema': 'examen'}

    id = Column(Integer, primary_key=True)
    ciudad = Column(String(50))
    id_pais = Column(Integer, ForeignKey('examen.paises.id'))

class Estado(Base):
    __tablename__ = 'estados'
    __table_args__ = {'schema': 'examen'}

    id = Column(Integer, primary_key=True)
    estado = Column(String(50), nullable=False, unique=True)

class Reactor(Base):
    __tablename__ = 'reactores'
    __table_args__ = {'schema': 'examen'}

    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)
    potencia_termica = Column(Numeric, nullable=False)
    primera_fecha_reaccion = Column(DateTime)
    id_tipo_reactor = Column(Integer, ForeignKey('examen.tipos_reactor.id'))
    id_ubicacion = Column(Integer, ForeignKey('examen.ubicacion.id'))
    id_estado = Column(Integer, ForeignKey('examen.estados.id'))