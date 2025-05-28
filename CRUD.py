import redis

r = redis.Redis(host='localhost', port=6379, db=0)

nome_da_lista_de_tarefas = 'lista_de_tarefas'

def atualizar_tarefa():
    listar_tarefas()
    try:
        indice = int(input("Digite o índice da tarefa a ser atualizada (começando do 0): "))
        nova_tarefa = input("Digite a nova descrição da tarefa: ")
        r.lset(nome_da_lista_de_tarefas, indice, nova_tarefa)
        print("Tarefa atualizada com sucesso!")
    except (ValueError, redis.exceptions.ResponseError):
        print("Erro ao atualizar. Verifique se o índice está correto.")

def remover_tarefa_por_indice():
    listar_tarefas()
    try:
        indice = int(input("Digite o índice da tarefa que deseja remover: "))
        tarefa = r.lindex(nome_da_lista_de_tarefas, indice)
        if tarefa:
            r.lrem(nome_da_lista_de_tarefas, 1, tarefa)
            print("Tarefa removida com sucesso!")
        else:
            print("Índice inválido.")
    except ValueError:
        print("Entrada inválida. Digite um número.")

def menu():
    while True:
        print("\nMenu:")
        print("1. Adicionar tarefa (Create)")
        print("2. Listar tarefas (Read)")
        print("3. Atualizar tarefa (Update)")
        print("4. Remover primeira tarefa (Delete)")
        print("5. Remover última tarefa (Delete)")
        print("6. Remover tarefa por índice (Delete)")
        print("7. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            adicionar_tarefa()
        elif escolha == '2':
            listar_tarefas()
        elif escolha == '3':
            atualizar_tarefa()
        elif escolha == '4':
            remover_primeira_tarefa()
        elif escolha == '5':
            remover_ultima_tarefa()
        elif escolha == '6':
            remover_tarefa_por_indice()
        elif escolha == '7':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
