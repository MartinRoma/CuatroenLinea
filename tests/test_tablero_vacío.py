#python -m py.test
from src.Código import GenerarTableroVacio

def test_tablero_vacio_tiene_6_filas():
    tablero=GenerarTableroVacio([7,6])

    assert len(tablero)==6
def test_tablero_vacio_tiene_7_columnas():
    tablero=GenerarTableroVacio([7,6])

    assert len(tablero[:])==6
