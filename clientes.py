import csv
import datetime

# Função para criar um novo chamado de manutenção
def criar_chamado():
    chamado = {}
    chamado['ID'] = input("Digite o ID do chamado: ")
    chamado['Descrição'] = input("Digite a descrição do problema: ")
    chamado['Data'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    chamado['Status'] = 'Aberto'
    return chamado

# Função para salvar o chamado em um arquivo CSV
def salvar_chamado(chamado, nome_arquivo='chamados.csv'):
    with open(nome_arquivo, mode='a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=chamado.keys())
        if file.tell() == 0:
            writer.writeheader()
        writer.writerow(chamado)

# Função para visualizar todos os chamados
def visualizar_chamados(nome_arquivo='chamados.csv'):
    try:
        with open(nome_arquivo, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                print(row)
    except FileNotFoundError:
        print("Nenhum chamado encontrado.")

# Menu principal
def menu():
    while True:
        print("\nGerador de Chamados de Manutenção")
        print("1. Criar novo chamado")
        print("2. Visualizar chamados")
        print("3. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            chamado = criar_chamado()
            salvar_chamado(chamado)
            print("Chamado criado com sucesso!")
        elif escolha == '2':
            visualizar_chamados()
        elif escolha == '3':
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()

