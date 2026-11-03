from datetime import datetime
from sqlalchemy import Column, Float, ForeignKey, Integer, String, Text, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()


class Equipo(Base):
  __tablename__ = 'equipos'

  id = Column(Integer, primary_key=True)
  nombre = Column(String(100), nullable=False)  # Ej: Traje CaboSub 3/2mm
  tipo = Column(
      String(50), nullable=False
  )  # Ej: Neopreno, Máscara, Lastre, etc.
  observaciones = Column(Text, nullable=True)

  # Relación con inmersiones
  inmersiones = relationship('Inmersion', back_populates='equipo_utilizado')


class Inmersion(Base):
  __tablename__ = 'inmersion'

  id = Column(Integer, primary_key=True)
  fecha = Column(
      String(50), default=lambda: datetime.now().strftime('%Y-%m-%d %H:%M')
  )
  profundidad_max = Column(
      Float, nullable=False
  )  # En metros (ej: 8.5 m en Calafquén)
  tiempo_apnea = Column(Integer, nullable=False)  # En segundos
  temperatura_agua = Column(Float, nullable=True)  # En grados Celsius
  ubicacion = Column(String(100), default='Lago Calafquén')
  notas = Column(Text, nullable=True)

  # Clave foránea para vincular el equipo usado
  equipo_id = Column(Integer, ForeignKey('equipos.id'), nullable=True)
  equipo_utilizado = relationship('Equipo', back_populates='inmersiones')


# Configuración de la base de datos local SQLite
DATABASE_URL = 'sqlite:///hydrocalafquen.db'
engine = create_engine(DATABASE_URL)


def inicializar_base_datos():
  """Crea las tablas en la base de datos si no existen."""
  Base.metadata.create_all(engine)
  print('¡Base de datos SQLite inicializada correctamente!')


if __name__ == '__main__':
  inicializar_base_datos()