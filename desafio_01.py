from time import sleep

def reverte_numero(numero: int) -> int:
    numero_str = str(numero)    
    reverso = int(numero_str[::-1])
    return reverso

def valida_numero(numero: int) -> bool:
    numero_str = str(numero)
    return numero_str[-1] != "0"

def listar_reversiveis(limite: int) -> list:
    reversiveis = []
    for numero in range(limite):
        if not valida_numero(numero):
            continue
        soma = numero + reverte_numero(numero)
        if (soma % 2 == 1) and (soma < limite):
            reversiveis.append(numero)
    return reversiveis

if __name__ == "__main__":
    limite = 1_000_000
    lista_n = listar_reversiveis(limite)
    print(lista_n)

sleep(10)