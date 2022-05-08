from time import sleep

def string_para_lista(string: str) -> list[int]:
    lista = string.strip("[]")
    lista = lista.split(sep=",")
    lista = list(map(int,lista))
    return lista

def validar_aula(alunos_minimos: int, tempo_chegada: list[int]) -> None:
    if sum([x <= 0 for x in tempo_chegada]) >= alunos_minimos:
        print("Aula normal")
    else:
        print("Aula cancelada")

if __name__ == "__main__":
    alunos_minimos = int(input("Defina o valor mínimo de alunos presentes (x): "))
    tempo_chegada = input("Informe o tempo de chegada dos alunos: ")
    tempo_chegada = string_para_lista(tempo_chegada)
    validar_aula(alunos_minimos,tempo_chegada)

sleep(10)