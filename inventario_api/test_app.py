# inventario_api/test_app.py

from fastapi.testclient import TestClient
from app import app
import os

client = TestClient(app)

def test_listar_productos():
    response = client.get("/productos/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

    # Generar reporte de pruebas
    os.makedirs("test-results", exist_ok=True)
    with open("test-results/inventario_test_results.xml", "w") as f:
        f.write("<testsuite>")
        f.write("  <testcase name='test_listar_productos' />\n")
        f.write("</testsuite>")

def test_obtener_producto_existente():
    response = client.get("/productos/1")
    assert response.status_code == 200

    # Generar reporte de pruebas
    os.makedirs("test-results", exist_ok=True)
    with open("test-results/inventario_test_results.xml", "a") as f:
        f.write("  <testcase name='test_obtener_producto_existente' />\n")
        f.write("</testsuite>")