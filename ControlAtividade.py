import ModelAtividade
import this

valor = 0
opcao = 0

#menu
def menu():
    print('Escolha uma das opções abaixo:\n'
          '1. Exe 1\n'
          '2. Exe 2\n'
          '3. Exe 3\n'
          '4. Exe 4\n'
          '5. Exe 5\n'
          '6. Exe 6\n'
          '7. Exe 7\n'
          '8. Exe 8\n'
          '9. Exe 9')
    this.opcao = int(input())



#Exe2
def inputExer2():
    print('escolha um número:')
    this.valor = float(input())

#EXE3










#Menu
def mostrar():
    menu()
    if (this.opcao == 1):
        print(ModelAtividade.exer1())

    elif (this.opcao == 2):
        inputExer2()
        print('anterior {} e o atual {}'.format(this.valor, ModelAtividade.exer2(this.valor)))


