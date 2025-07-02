import os

tarefas = {
    'tarefas': ['Limpar o quarto', 'Lavar louça'],
    'datas': ['30/06', '30/06']
}

def mostrar_tarefas():
    barra = f'|{"_" * 30}|'
    print(barra)
    print('| Tarefas:')
    for i in range(len(tarefas['tarefas'])):
        print(f"| {i + 1}. {tarefas['tarefas'][i]} - Data: {tarefas['datas'][i]}")
    print(barra)

def adicionar_tarefa():
    tarefa = input('| Digite o nome da tarefa: ')
    data = input('| Digite a data (dd/mm): ')
    tarefas['tarefas'].append(tarefa)
    tarefas['datas'].append(data)
    print('| Tarefa adicionada com sucesso!')

def remover_tarefa():
    mostrar_tarefas()
    try:
        indice = int(input('| Digite o número da tarefa a remover: ')) - 1
        if 0 <= indice < len(tarefas['tarefas']):
            tarefa_removida = tarefas['tarefas'].pop(indice)
            tarefas['datas'].pop(indice)
            print(f'| Tarefa "{tarefa_removida}" removida com sucesso!')
        else:
            print('| Índice inválido.')
    except ValueError:
        print('| Entrada inválida. Digite um número.')

def mostrar_menu():
    while True:
        os.system('cls')
        barra = f'|{"_" * 30}|'
        print(barra)
        print('| Gerenciador de Tarefas')
        print(barra)
        print('| (1) Mostrar tarefas')
        print('| (2) Adicionar tarefa')
        print('| (3) Remover tarefa')
        print('| (4) Sair')
        print(barra)

        try:
            resposta = int(input('| Escolha uma opção: '))
            if resposta == 1:
                os.system('cls')
                mostrar_tarefas()
                input('| Pressione Enter para continuar...')
            elif resposta == 2:
                adicionar_tarefa()
                input('| Pressione Enter para continuar...')
            elif resposta == 3:
                os.system('cls')
                remover_tarefa()
                input('| Pressione Enter para continuar...')
            elif resposta == 4:
                print('| Saindo...')
                break
            else:
                print('| Opção inválida.')
                input('| Pressione Enter para continuar...')
        except ValueError:
            print('| Por favor, digite um número válido.')
            input('| Pressione Enter para continuar...')

mostrar_menu()
