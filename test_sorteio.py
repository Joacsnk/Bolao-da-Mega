from main import gerar_cartela 

def test_quantidade_de_jogos():
    jogos = gerar_cartela(6, 5)
    assert len(jogos) == 5

def test_quantidade_de_dezenas():
    jogos = gerar_cartela(6, 1)
    assert len(jogos[0]) == 6

def test_numeros_no_intervalo():
    jogos = gerar_cartela(6, 1)
    for num in jogos[0]:
        assert 1 <= num <= 60