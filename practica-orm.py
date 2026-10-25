### 1)

from sqlalchemy import create_engine, Column, Integer, String, Float, Boolean
from sqlalchemy.orm import declarative_base, sessionmaker

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

### -------------------------------------------------------------------------------------------------
### -------------------------------------------------------------------------------------------------

### 2)

# Crear la sesión
Session = sessionmaker(bind=engine)
session = Session()

# Crear los 10 productos
productos = [
    Producto(nombre="Teclado mecanico", categoria="perifericos", precio=8500, stock=15),
    Producto(nombre="Mouse inalambrico", categoria="perifericos", precio=4200, stock=30),
    Producto(nombre="Monitor 24 pulgadas", categoria="monitores", precio=62000, stock=8),
    Producto(nombre="Auriculares bluetooth", categoria="audio", precio=12300, stock=20),
    Producto(nombre="Webcam Full HD", categoria="perifericos", precio=9800, stock=12),
    Producto(nombre="SSD 1TB", categoria="almacenamiento", precio=18500, stock=25),
    Producto(nombre="RAM 16GB", categoria="componentes", precio=15600, stock=18),
    Producto(nombre="Mousepad XL", categoria="perifericos", precio=2100, stock=40),
    Producto(nombre="Hub USB-C", categoria="accesorios", precio=5400, stock=6, activo=False),
    Producto(nombre="Cable HDMI", categoria="accesorios", precio=1800, stock=50)
]

# Agregar los productos a la sesión
session.add_all(productos)

# Guardar los cambios en la base de datos
session.commit()

# Verificar cuántos productos hay
cantidad = session.query(Producto).count()
print("----------------------------------------------------------")
print(f"2) Cantidad de productos en la base de datos: {cantidad}")
print("----------------------------------------------------------")

# Cerrar la sesión
session.close()

### -------------------------------------------------------------------------------------------------
### -------------------------------------------------------------------------------------------------

### 3)

# Traer todos los productos de la categoría "perifericos"
print("3) Nombre y precio de la categoria 'perifericos'")

productos_perifericos = session.query(Producto).filter(
    Producto.categoria == "perifericos"
).all()

# Mostrar nombre y precio
for producto in productos_perifericos:
    print(f"Nombre: {producto.nombre} - Precio: ${producto.precio}")
