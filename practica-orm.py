### 1)

from sqlalchemy import create_engine, Column, Integer, String, Float, Boolean
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Producto(Base):
    __tablename__ = "productos"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String, nullable=False)
    categoria = Column(String, nullable=False)
    precio = Column(Float, nullable=False)
    stock = Column(Integer, nullable=False)
    activo = Column(Boolean, default=True)

engine = create_engine("sqlite:///productos.db")

Base.metadata.create_all(engine)