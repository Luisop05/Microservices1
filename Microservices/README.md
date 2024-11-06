Sistema de Gestión de Restaurante
Este proyecto implementa un sistema de gestión de restaurante con dos microservicios:

API de Pedidos (Puerto 8000): Gestiona los pedidos de los clientes
API de Inventario (Puerto 8001): Gestiona el inventario de productos

Estructura del Proyecto
Microservices/
├── pedidos_api/
│   ├── Dockerfile
│   ├── requirements.txt
│   └── app.py
├── inventario_api/
│   ├── Dockerfile
│   ├── requirements.txt
│   └── app.py
├── docker-compose.yml
└── README.md

Requisitos

Docker
Docker Compose

Instalación y Ejecución

Clonar el repositorio: 

Levantar los contenedores:

docker-compose up --build

Documentación de APIs
API de Pedidos (http://localhost:8000)
Endpoints Disponibles:

POST /pedidos/

Crea un nuevo pedido
Verifica el inventario disponible
Actualiza automáticamente el stock

GET /pedidos/{pedido_id}

Obtiene los detalles de un pedido específico


PUT /pedidos/{pedido_id}/estado

Actualiza el estado de un pedido
Estados disponibles: pendiente, en_preparacion, completado, cancelado



API de Inventario (http://localhost:8001)
Endpoints Disponibles:

GET /productos/

Lista todos los productos disponibles


GET /productos/{producto_id}

Obtiene detalles de un producto específico


POST /productos/{producto_id}/reducir

Reduce el stock de un producto



Ejemplos de Uso
1. Crear un nuevo pedido:
POST http://localhost:8000/pedidos/ \
body:
'{
  "items": [
    {
      "producto_id": 1,
      "cantidad": 2,
      "notas": "Sin cebolla"
    }
  ],
  "mesa": 5
}'
2. Consultar inventario:

curl http://localhost:8001/productos/

3. Actualizar estado de pedido:
 PUT http://localhost:8000/pedidos/1/estado \
-H "Content-Type: application/json" \
-d '"en_preparacion"'

Documentación Swagger

API de Pedidos: http://localhost:8000/docs
API de Inventario: http://localhost:8001/docs



El sistema implementa un caso real de gestión de restaurante. Aquí está la explicación detallada:
1. API de Pedidos (Puerto 8000)
Endpoints:

POST /pedidos/

Crea un nuevo pedido
Verifica disponibilidad en inventario
Calcula el total
Actualiza el stock automáticamente
Ejemplo de cuerpo de solicitud:

jsonCopy{
  "items": [
    {
      "producto_id": 1,
      "cantidad": 2,
      "notas": "Sin cebolla"
    }
  ],
  "mesa": 5
}

GET /pedidos/{pedido_id}

Obtiene detalles de un pedido específico
Retorna toda la información del pedido incluyendo estado y total


PUT /pedidos/{pedido_id}/estado

Actualiza el estado del pedido
Estados disponibles:

pendiente
en_preparacion
completado
cancelado





2. API de Inventario (Puerto 8001)
Endpoints:

GET /productos/

Lista todos los productos disponibles
Incluye información de stock y precios


GET /productos/{producto_id}

Obtiene información detallada de un producto
Incluye stock actual y precio


POST /productos/{producto_id}/reducir

Reduce el stock de un producto
Verifica disponibilidad antes de reducir
Ejemplo de cuerpo de solicitud:

jsonCopy{
  "cantidad": 2
}

// documentación adicional
Documentación Swagger
Ambas APIs incluyen documentación Swagger completa accesible en:

API de Pedidos: http://localhost:8000/docs
API de Inventario: http://localhost:8001/docs

La documentación incluye:

Descripción de cada endpoint
Esquemas de datos
Ejemplos de solicitudes y respuestas
Códigos de estado posibles
Modelos de datos utilizados

Comunicación entre Servicios

Cuando se crea un pedido:

La API de Pedidos consulta el inventario
Verifica disponibilidad de productos
Reduce el stock automáticamente
Calcula el total basado en precios del inventario


La comunicación se realiza a través de la red Docker restaurant-net

Flujo de Trabajo Típico:

El cliente hace un pedido:
POST http://localhost:8000/pedidos/

El sistema verifica el inventario:
GET http://localhost:8001/productos/{id}

Si hay stock suficiente:

Se crea el pedido
Se reduce el stock
Se retorna confirmación



Detener los servicios
Para detener los contenedores:
 docker-compose down