from itertools import combinations_with_replacement as comb
from time import sleep

def string_para_lista(string: str) -> list[int]:
    lista = string.strip("[]")
    lista = lista.split(sep=",")
    lista = list(map(int,lista))
    return lista

def validar_combinacao(grupos: list[tuple], valor) -> None:
    if all([(sum(x) > valor) for x in grupos]):
        print(f"Não há como chegar no valor {valor} utilizando os valores do vetor {vetor}.")
        sleep(10)
        raise Exception()

def elementos_minimos(valor: int, vetor: list[int]) -> list[list]:
    numero_elementos = 0
    conjunto_minimo =[]
    while True:
        numero_elementos += 1
        grupos = list(comb(vetor, numero_elementos))
        validar_combinacao(grupos, valor)
        for subconjunto in grupos:
            if sum(subconjunto) == valor:
                conjunto_minimo.append(subconjunto)
        if len(conjunto_minimo) > 0:
            return conjunto_minimo

if __name__ == "__main__":
    valor_soma = int(input("Defina o valor de N: "))
    vetor = input("Informe o vetor de números (V): ")
    vetor = set(string_para_lista(vetor))
    conjunto_minimo = elementos_minimos(valor_soma,vetor)
    print(valor_soma)
    [print(list(x)) for x in conjunto_minimo]

sleep(10)
