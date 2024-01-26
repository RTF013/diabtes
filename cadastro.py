class Cliente:
    def __init__(self, container, tara, maxcross, lacre, placa_cavalo, placa_carreta, associacao):
        self.container = container
        self.tara = tara
        self.maxcross = maxcross
        self.lacre = lacre
        self.placa_cavalo = placa_cavalo
        self.placa_carreta = placa_carreta
        self.associacao = associacao

    def exibir_informacoes(self):
        print("Container:", self.container)
        print("Tara:", self.tara)
        print("Maxcross:", self.maxcross)
        print("Lacre:", self.lacre)
        print("Placa do Cavalo:", self.placa_cavalo)
        print("Placa da Carreta:", self.placa_carreta)
        print("Associação:", self.associacao)
        print("---------------")


def main():
    lista_clientes = []

    while True:
        print("Cadastro de Clientes")
        container = input("Container: ")
        tara = float(input("Tara: "))
        maxcross = float(input("Maxcross: "))
        lacre = input("Lacre: ")
        placa_cavalo = input("Placa do Cavalo: ")
        placa_carreta = input("Placa da Carreta: ")
        associacao = input("Associação: ")

        novo_cliente = Cliente(container, tara, maxcross, lacre, placa_cavalo, placa_carreta, associacao)
        lista_clientes.append(novo_cliente)

        print("Cliente cadastrado com sucesso!")

        resposta = input("Deseja cadastrar outro cliente? (S/N): ")

        if resposta.upper() != "S":
            break

    print("\nLista de Clientes Cadastrados:")
    for cliente in lista_clientes:
        cliente.exibir_informacoes()


if __name__ == "__main__":
    main()
