import math
    
def checa_primo(numero):
    if (numero == 0 or numero == 1):
        return 0
    
    divisor = 3

    while (divisor <= math.sqrt(numero)):
        if (numero % divisor == 0):
            return 0
        divisor += 2
    
    return 1

def euclides(num1, num2):
    if (num1 < num2):
        temp = num1
        num1 = num2
        num2 = temp
    
    while (num2 != 0):
        resto = num1 % num2
        num1 = num2
        num2 = resto
    
    return num1

def gerar_chaves():
    print("Gerar chaves:\n")

    print("Digite dois números 'p' e 'q' e um expoente 'e' coprimo de 'p' * 'q'\n")

    p = int(input())
    q = int(input())
    e = int(input())

    if (checa_primo(p) == 0 or checa_primo(q) == 0):
        print("p e/ou q não são primos\n")
        return
    
    n = p * q
    phi = (p - 1) * (q - 1)

    if (euclides(phi, e) != 1):
        print("e não é um expoente válido\n")
        return
    
    chave_publica = open("chave_publica.txt", "w")
    chave_publica.write("n = " + str(n) + "\n")
    chave_publica.write("e = " + str(e) + "\n")
    chave_publica.close()