from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import json
from pathlib import Path

class Producto(BaseModel):
    id: int
    nombre: str
    precio: float
    categoria: str
    stock: int
    descripcion: Optional[str] = None

class ActualizarStock(BaseModel):
    cantidad: int

app = FastAPI(
    title="API de Inventario - Restaurante",
    description="API para gestionar el inventario de productos del restaurante",
    version="1.0.0"
)

# Datos de ejemplo
PRODUCTOS_INICIALES = [
    {
        "id": 1,
        "nombre": "Hamburguesa Clásica",
        "precio": 12.99,
        "categoria": "Hamburguesas",
        "stock": 50,
        "descripcion": "Hamburguesa con queso, lechuga y tomate"
    },
    {
        "id": 2,
        "nombre": "Pizza Margherita",
        "precio": 15.99,
        "categoria": "Pizzas",
        "stock": 30,
        "descripcion": "Pizza con salsa de tomate, mozzarella y albahaca"
    },
    {
        "id": 3,
        "nombre": "Ensalada César",
        "precio": 9.99,
        "categoria": "Ensaladas",
        "stock": 25,
        "descripcion": "Lechuga romana, crutones, parmesano y aderezo césar"
    }
]

# Simulamos una base de datos con un diccionario
productos = {p["id"]: p for p in PRODUCTOS_INICIALES}

@app.get("/productos/", 
         response_model=List[Producto],
         tags=["productos"],
         summary="Listar todos los productos",
         description="Retorna la lista completa de productos en el inventario")
async def listar_productos():
    return list(productos.values())

@app.get("/productos/{producto_id}", 
         response_model=Producto,
         tags=["productos"],
         summary="Obtener producto por ID",
         description="Retorna los detalles de un producto específico")
async def obtener_producto(producto_id: int):
    if producto_id not in productos:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return productos[producto_id]

@app.post("/productos/{producto_id}/reducir", 
          response_model=Producto,
          tags=["productos"],
          summary="Reducir stock de producto",
          description="Reduce el stock de un producto por la cantidad especificada")
async def reducir_stock(producto_id: int, datos: ActualizarStock):
    if producto_id not in productos:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    
    producto = productos[producto_id]
    if producto["stock"] < datos.cantidad:
        raise HTTPException(status_code=400, detail="Stock insuficiente")
    
    producto["stock"] -= datos.cantidad
    return producto