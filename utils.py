from datetime import datetime


def tratar_entrada_data(entrada):
    hoje = datetime.now()
    ano_atual = hoje.year
    mes_atual = hoje.month

    partes = entrada.split("/")

    if len(partes) == 1:  # Se tiver apenas o dia
        dia = int(partes[0])
        return datetime(ano_atual, mes_atual, dia).strftime("%d/%m/%Y")

    elif len(partes) == 2:  # Se tiver dia e mês
        dia = int(partes[0])
        mes = int(partes[1])
        return datetime(ano_atual, mes, dia).strftime("%d/%m/%Y")

    elif len(partes) == 3:  # Se tiver dia, mês e ano
        dia = int(partes[0])
        mes = int(partes[1])
        ano = int(partes[2])
        return datetime(ano, mes, dia).strftime("%d/%m/%Y")

    else:
        return None  # Formato inválido

if __name__ == "__main__":
    while True:
        # Exemplo de uso:
        entrada_usuario = input("Digite a data: ")
        data_tratada = tratar_entrada_data(entrada_usuario)

        if data_tratada:
            print(f"Data tratada: {data_tratada}")
        else:
            print("Formato de data inválido.")
        print("oi")
