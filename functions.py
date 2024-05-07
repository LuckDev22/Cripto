from datetime import datetime, timezone
from criptomoeda import Criptomoeda


def listar_criptomoedas(criptomoedas):
    print("\nListagem de Criptomoedas:")
    print("ID | symbol  | lastPrice  | nextFundingTime")
    for i, criptomoeda in enumerate(criptomoedas, start=1):
        symbol = (
            criptomoeda.symbol[:3] + "..."
            if len(criptomoeda.symbol) > 3
            else criptomoeda.symbol
        )
        next_funding_time_formatted = "N/A"
        if criptomoeda.nextFundingTime and criptomoeda.nextFundingTime != "0":
            if "/" in criptomoeda.nextFundingTime:
                next_funding_time_formatted = criptomoeda.nextFundingTime
            else:
                next_funding_time_seconds = float(criptomoeda.nextFundingTime) / 1000
                next_funding_time_datetime = datetime.fromtimestamp(
                    next_funding_time_seconds, tz=timezone.utc
                )
                next_funding_time_formatted = next_funding_time_datetime.strftime(
                    "%d/%m/%Y"
                )
        print(
            f"{i} | {symbol} | {criptomoeda.lastPrice} | {next_funding_time_formatted}"
        )


def adicionar_criptomoeda(criptomoedas):
    print("\nAdicionar Nova Criptomoeda:")
    symbol = input("Digite o símbolo da criptomoeda: ").strip().upper()
    last_price = input("Digite o último preço da criptomoeda: ").strip()
    next_funding_time = input(
        "Digite o próximo horário de financiamento da criptomoeda (formato DD/MM/YYYY): "
    ).strip()

    nova_criptomoeda = Criptomoeda(symbol, last_price, next_funding_time)
    criptomoedas.append(nova_criptomoeda)

    print("Criptomoeda adicionada com sucesso!")


def editar_criptomoeda(criptomoedas):
    print("\nEditar Criptomoeda:")
    listar_criptomoedas(criptomoedas)
    id_criptomoeda = input("Digite o ID da criptomoeda que deseja editar: ")

    try:
        id_criptomoeda = int(id_criptomoeda)
        if id_criptomoeda < 1 or id_criptomoeda > len(criptomoedas):
            raise ValueError
    except ValueError:
        print("ID inválido!")
        return

    criptomoeda = criptomoedas[id_criptomoeda - 1]

    print(
        f"\nEditar Criptomoeda: {criptomoeda.symbol} | {criptomoeda.lastPrice} | {criptomoeda.nextFundingTime}"
    )

    symbol = input("Digite o novo símbolo da criptomoeda: ").strip()
    last_price = input("Digite o novo último preço da criptomoeda: ").strip()
    next_funding_time = input(
        "Digite o novo horário de financiamento da criptomoeda (formato DD/MM/YYYY): "
    ).strip()

    criptomoeda.symbol = symbol
    criptomoeda.lastPrice = last_price
    criptomoeda.nextFundingTime = next_funding_time

    print("Criptomoeda editada com sucesso!")


def remover_criptomoeda(criptomoedas):
    print("\nRemover Criptomoeda:")
    listar_criptomoedas(criptomoedas)
    id_criptomoeda = input("Digite o ID da criptomoeda que deseja remover: ")

    try:
        id_criptomoeda = int(id_criptomoeda)
        if id_criptomoeda < 1 or id_criptomoeda > len(criptomoedas):
            raise ValueError
    except ValueError:
        print("ID inválido!")
        return

    criptomoeda_removida = criptomoedas.pop(id_criptomoeda - 1)
    print(f"Criptomoeda {criptomoeda_removida.symbol} removida com sucesso!")
