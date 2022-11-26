# função que calcula uma exponencial através do resto
def expo_mod(base, expoente, modulo):
   counter = 1
   while (expoente > 0):
      counter = ((counter * base) % modulo)
      expoente -= 1
   return counter

def find_t(arrayofquoc, quocCounter):
    i = 0
    tmp = 0
    t = 1
    new = 0

    while(i < quocCounter):
        new = (arrayofquoc[i] * t) + tmp
        tmp = t
        t = new
        i += 1

    if (quocCounter % 2 == 0):
        return t
    else:
        return t * (-1)
   
def invmod(numA, numB):
    tmp = 0
    quoc = []
    counter = 0
    initialnumB = numB

    while (numB != 0):
        tmp = numB
        quoc.append(numA // numB)
        numB = numA % numB
        numA = tmp
  

    inverso = find_t(quoc, len(quoc) - 1)
    
    while (inverso < 0):
        inverso = inverso + initialnumB
        #print(inverso)
    
    return inverso

def decrypt():
    print("Digite dois números 'p' e 'q' e o expoente 'e'\n")
    p = int(input())
    q = int(input())
    e = int(input())

    totiente = ((p - 1) * (q - 1))

    n = p * q 

    d = invmod(totiente, e)

    encrypted_msg = open("mensagem_criptografada.txt", "r") 

    buffer = []

    for line in encrypted_msg:
        for letter in line.split():
            buffer.append(letter)
    
    decrypted_msg = open("mensagem_descriptografada.txt", "w")      
    
    for letter in buffer:
        tmp = pow(int(letter), d, n)
        if(tmp != 28):
            tmp += 63
        else:
            tmp = 32
        decrypted_msg.write("%c" % tmp)





