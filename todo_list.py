from datetime import datetime

from utils import tratar_entrada_data


class Tarefa:
    def __init__(self, action) -> None:
        self.action: str = action
        self.date: str = ""
        self.hour: str = ""
        self.anterior: Tarefa | None = None
        self.proximo: Tarefa | None = None

    def __str__(self) -> str:    # tratar objeto como string
        return f"{self.action}" 

    # def __repr__(self) -> str:   # representar  a classe 
    #     return self.__str__()


class TodoList:
    def __init__(self) -> None:
        self.primeiro: Tarefa | None = None # tipo Tarefa ou tipo None
        self.ultimo: Tarefa | None = None

    def add_tarefa(self, tarefa: Tarefa):
        """
        Adds a task to the task list.

        Args:
            tarefa (Tarefa): The task to be added.
        """

        # Get the current date and time
        date_time_now = datetime.now() # entrar na classe pra pegar uma informação específica 

        # Set the task's date and hour attributes
        tarefa.date = date_time_now.strftime("%d/%m/%Y")
        tarefa.hour = date_time_now.strftime("%H:%M:%S")

        # If the task list is empty, set the first and last tasks to the newly added task
         
        if self.primeiro is None:
            self.primeiro = tarefa
            self.ultimo = tarefa

        # If the task list is not empty, set the next task of the last task to the newly added task
        if self.ultimo is not None:
            self.ultimo.proximo = tarefa

        # Set the previous task of the newly added task to the last task
        tarefa.anterior = self.ultimo

        # If the newly added task is its own previous task, set the previous task to None
        if tarefa.anterior == tarefa:
            tarefa.anterior = None    # apontar as duas pontas para none para não ficar circular

        # If the newly added task is its own next task, set the next task to None
        if tarefa.proximo == tarefa:
            tarefa.proximo = None

        # Update the last task to the newly added task
        self.ultimo = tarefa

        # Show the updated task list
        self.mostrar() # mostrar a lista atualizada 

    def mostrar(self):
        if self.primeiro is None:
            print("Nenhuma tarefa cadastrada")
            return #return vai para o while
        atual = self.primeiro
        while atual:
            proxima_tarefa = atual.proximo
            tarefa_anterior = atual.anterior
            if proxima_tarefa is None:
                proxima_tarefa = "Nenhuma"
            if tarefa_anterior is None:
                tarefa_anterior = "Nenhuma"
            print()
            print(
                f"\tAção: {atual}\n"
                f"\tData: {atual.date}\n"
                f"\tHora: {atual.hour}\n"
                f"\tTarefa anterior: {tarefa_anterior}\n"
                f"\tTarefa seguinte: {proxima_tarefa}\n"
            )
            print()
            atual = atual.proximo #atual

    def remover(self, nome_tarefa: str):
        """
        Remove a task from the task list.

        Args:
            nome_tarefa (str): The name of the task to be removed.
        """
        
        atual = self.primeiro

        
        while atual:
            
            if atual.action.lower() == nome_tarefa.lower():

                if atual.anterior:  
                   
                    atual.anterior.proximo = atual.proximo
                else:
                    
                    self.primeiro = atual.proximo
                   
                    if atual.proximo:
                        atual.proximo.anterior = None

               
                if atual.proximo:
                    atual.proximo.anterior = atual.anterior

                
                print(f'Tarefa "{atual.action}" removida com sucesso.')
                self.mostrar()
                return
            # Mover para o próximo nó na lista
            atual = atual.proximo

        
        print(f'Tarefa "{nome_tarefa}" não encontrada.')

    def buscar(self, tarefa):
        if self.primeiro is None:
            print("Nenhuma tarefa cadastrada")
            return
        atual = self.primeiro
        while atual: #se tiver algo lá dentro da variável
            if tarefa.lower() in atual.action.lower():
                proxima_tarefa = atual.proximo
                tarefa_anterior = atual.anterior
                if proxima_tarefa is None:
                    proxima_tarefa = "Nenhuma"
                if tarefa_anterior is None:
                    tarefa_anterior = "Nenhuma"
                print() #quebra de linha
                print(
                    f"\tAção: {atual.action}\n"
                    f"\tData: {atual.date}\n"
                    f"\tHora: {atual.hour}\n"
                    f"\tTarefa anterior: {tarefa_anterior}\n"
                    f"\tTarefa seguinte: {proxima_tarefa}\n"
                )
                print()
            atual = atual.proximo

    def filtrar_por_data(self, data):
        if self.primeiro is None:
            print("Nenhuma tarefa encontrada")
            return

        data_formatada = datetime.strptime(data, "%d/%m/%Y").strftime("%d/%m/%Y") # recebe data e mapeamento de entrada e depois da saída

        atual = self.primeiro
        while atual:
            if atual.date == data_formatada:
                proxima_tarefa = atual.proximo
                tarefa_anterior = atual.anterior
                if proxima_tarefa is None:
                    proxima_tarefa = "Nenhuma"
                if tarefa_anterior is None:
                    tarefa_anterior = "Nenhuma"
                print()
                print(
                    f"\tAção: {atual.action}\n"
                    f"\tData: {atual.date}\n"
                    f"\tHora: {atual.hour}\n"
                    f"\tTarefa anterior: {tarefa_anterior}\n"
                    f"\tTarefa seguinte: {proxima_tarefa}\n"
                )
                print()
            atual = atual.proximo

    def menu(self):
        while True:
            print(
                "0 - Sair\n1 - Mostrar\n2 - Adicionar\n3 - Remover\n4 - Filtrar por data\n5 - Buscar"
            )

            opcao = input("Opção: ")

            if not opcao.isdigit():
                print(
                    "Você não digitou um número, então criaremos a tarefa automaticamente"
                )
                self.add_tarefa(Tarefa(opcao))
                continue

            try: # tentar execução do bloco
                opcao = int(opcao)
            except ValueError:
                print("Opção inválida. Tente novamente.")
                continue

            if opcao == 1:
                self.mostrar()

            elif opcao == 2:
                tarefa_input = input("Digite a tarefa: ")
                tarefa = Tarefa(tarefa_input)
                self.add_tarefa(tarefa)

            elif opcao == 3:
                tarefa_input = input("Digite a tarefa: ")
                self.remover(tarefa_input)

            elif opcao == 4:
                data_input = input("Digite a data (dd/mm/aaaa): ")
                if not data_input.isdigit() or data_input == 0:
                    print("Opção inválida. Tente novamente.")
                    continue
                data_formatada = tratar_entrada_data(data_input)
                self.filtrar_por_data(data_formatada)

            elif opcao == 5:
                tarefa_input = input("Digite a tarefa: ")
                self.buscar(tarefa_input)

            elif opcao == 0:
                break

            elif opcao > 5 or opcao < 0:
                print("Opção inválida. Tente novamente.")
                continue


if __name__ == "__main__":
    todolist = TodoList()
    todolist.menu()
