from src.Código import PartidaTerminada

def test_gana_fila():
    tab=[[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,1,1,1,1,1]]
    ans=PartidaTerminada(tab,3,1,5)

    assert ans==True

def test_no_gana_fila():
    tab=[[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,1,0,1,1,1]]
    ans=PartidaTerminada(tab,4,1,5)

    assert ans==False

def test_gana_columna():
    tab=[[0,0,0,0,0,0,0],[0,0,0,0,0,2,0],[0,0,0,0,0,2,0],[0,0,0,0,0,2,0],[0,0,0,0,0,2,0],[0,0,0,0,0,2,0]]
    ans=PartidaTerminada(tab,5,2,1)

    assert ans==True

def test_no_gana_columna():
    tab=[[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,2,0],[0,0,0,0,0,2,0],[0,0,0,0,0,2,0]]
    ans=PartidaTerminada(tab,5,2,3)

    assert ans==False

def test_gana_diagonal_decendente():
    tab=[[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,1,2,0,0],[0,0,0,1,1,0,0],[0,0,0,2,2,1,0],[0,0,0,1,2,2,1]]
    ans=PartidaTerminada(tab,3,1,2)

    assert ans==True
