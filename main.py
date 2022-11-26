import chaves
import criptografar
import descriptografar
import os

def clear():
    os.system("clear")

clear()    

operation_flag = 0
    
while(True):
    print("########## CRIPTOGRAFIA RSA ##########\n")
    print("Escolha uma opção:\n")
    print("1 -> Gerar chaves\n")
    print("2 -> Criptografar\n")
    print("3 -> Descriptografar\n")
    print("4 -> Sair\n")
    
    if(operation_flag == 1):
        print("Escolha uma opção válida")
    elif(operation_flag == 2):
        print("Chave gerada no 'arquivo chave_publica.txt'")
    elif(operation_flag == 3):
        print("Mensagem criptografada gerada no arquivo 'mensagem_criptografada.txt'")
    elif(operation_flag == 4):
        print("Mensagem descriptografada gerada no arquivo 'mensagem_descriptografada.txt'")
        
    opcao = input()

    match(opcao):
        case '1':
            operation_flag = 2
            clear()
            chaves.gerar_chaves()   
        case '2':
            operation_flag = 3
            clear()
            criptografar.encrypt()
        case '3':
            operation_flag = 4
            clear()
            descriptografar.decrypt()
        case '4':
            exit()
        case other:
            operation_flag = 1
