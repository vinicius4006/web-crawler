def preencher_lista_recursivamente(lista, n):
    if n == 0:
        return  # Caso base: quando n for igual a 0, encerra a recursão
    else:
        lista.append(n)  # Adiciona o valor de n à lista
        preencher_lista_recursivamente(lista, n-1)  # Chamada recursiva com n-1

# Exemplo de uso
minha_lista = []
preencher_lista_recursivamente(minha_lista, 10)

print(minha_lista)