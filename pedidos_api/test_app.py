# pedidos_api/test_app.py

from fastapi.testclient import TestClient
from app import app
import os

client = TestClient(app)

def test_crear_pedido():
    response = client.post("/pedidos/", json={
        "items": [{"producto_id": 1, "cantidad": 2, "notas": "Sin cebolla"}],
        "mesa": 5
    })
    assert response.status_code == 201

    # Generar reporte de pruebas
    os.makedirs("test-results", exist_ok=True)
    with open("test-results/pedidos_test_results.xml", "w") as f:
        f.write("<testsuite>")
        f.write("  <testcase name='test_crear_pedido' />\n")
        f.write("</testsuite>")

def test_obtener_pedido():
    response = client.get("/pedidos/1")
    assert response.status_code == 200

    # Generar reporte de pruebas
    os.makedirs("test-results", exist_ok=True)
    with open("test-results/pedidos_test_results.xml", "a") as f:
        f.write("  <testcase name='test_obtener_pedido' />\n")
        f.write("</testsuite>")