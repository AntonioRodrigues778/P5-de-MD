def soma_esperada(k: int) -> int:
    return k * (k + 1) // 2


def soma_naturais(n: int) -> int:
    # 1. Pré-condição
    assert isinstance(n, int), "Erro: n deve ser inteiro"
    assert n >= 0, "Erro: pre-condicao violada! n deve ser >= 0"

    s = 0
    i = 0

    # 2. Inicialização do invariante
    assert s == soma_esperada(i) and 0 <= i <= n,         "Erro: invariante falhou na inicializacao"

    while i < n:
        # Função variante
        velha_variante = n - i
        assert velha_variante >= 0,             "Erro: variante violou o limite inferior"

        # Corpo correto
        i = i + 1
        s = s + i

        # 3. Manutenção do invariante
        assert s == soma_esperada(i) and 0 <= i <= n,             "Erro: invariante violado no corpo do loop"

        # 4. Decremento da variante
        assert n - i < velha_variante,             "Erro: loop em execucao infinita"

    # 5. Pós-condição
    assert s == soma_esperada(n),         "Erro: pos-condicao falhou"

    return s


# Testes
print(soma_naturais(0))
print(soma_naturais(1))
print(soma_naturais(5))
print(soma_naturais(10))
