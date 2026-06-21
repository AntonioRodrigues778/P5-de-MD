import math


def fatorial_quebrado(n: int):
    # 1. ASSERCAO DE PRE-CONDICAO
    assert isinstance(n, int), "Erro: n deve ser inteiro"
    assert n >= 0, "Erro: n deve ser nao-negativo"

    f = 1
    i = 0

    # 2. ASSERCAO DE INICIALIZACAO (CASO BASE)
    # Invariante: f == i! e 0 <= i <= n
    assert f == math.factorial(
        i) and 0 <= i <= n, "Erro: invariante falhou na inicializacao"

    while i < n:
        velha_variante = n - i
        assert velha_variante >= 0, "Erro: variante violou o limite inferior"

        # BUG original
        f = f * i
        i = i + 1

        # 3. ASSERCAO DE MANUTENCAO (PASSO INDUTIVO)
        assert f == math.factorial(
            i) and 0 <= i <= n, "Erro: invariante violado no corpo do loop"

        # 4. ASSERCAO DE DECREMENTO (PROGRESSO DA TERMINACAO)
        assert n - i < velha_variante, "Erro: loop em execucao infinita"

    # 5. ASSERCAO DE POS-CONDICAO
    assert f == math.factorial(n), "Erro: pos-condicao falhou"

    return f


print(fatorial_quebrado(1))
