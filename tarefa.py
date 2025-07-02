import os 

tarefas = {
    'tarefas': ['Limpar o quarto', 'Lavar louça'],
    'datas': ['30/06', '30/06']
}

def mostrar_tarefa():
    barra = f'|'-'*30|'
    print(barra)
    print('| tarefas:')
    for i in range(len(tarefas['tarefas']))
        print(f"|{i + 1}. {tarefas['tarefas'][i]}" - Data: {tarefas['datas'][i]})
    print(barra)

def adicionar_tarefa():
    tarefa = input('| Digite o nome da tarefa: ')
    data = input('| Digite a data (dd/mm): ')
    tarefas 
    