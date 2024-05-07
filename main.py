from api import get_data
from functions import (
    listar_criptomoedas,
    adicionar_criptomoeda,
    editar_criptomoeda,
    remover_criptomoeda,
)


def main():
    criptomoedas = get_data()
    listar_criptomoedas(criptomoedas)

    while True:
        print("\nOpções:")
        print("1 - Listar criptomoedas")
        print("2 - Adicionar nova criptomoeda")
        print("3 - Editar criptomoeda")
        print("4 - Remover criptomoeda")
        print("5 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            listar_criptomoedas(criptomoedas)
        elif opcao == "2":
            adicionar_criptomoeda(criptomoedas)
        elif opcao == "3":
            editar_criptomoeda(criptomoedas)
        elif opcao == "4":
            remover_criptomoeda(criptomoedas)
        elif opcao == "5":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")


if __name__ == "__main__":
    main()
