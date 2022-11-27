#função que encriptografa a mensagem
def encrypt():
   message = input("Digite a mensagem a ser criptografada: \n")

   n = int(input("Digite o valor (n) da chave pública: "))

   print("\n")

   e = int(input("Digite o valor (e) da chave pública: "))

   print("\n")

   # transforma a string em array
   message_list = list(message)


   # transforma os valores em char para int
   i = 0  # type: ignore
   while (i < len(message_list)):
    message_list[i] = ord(message_list[i])
    i += 1

   # padroniza os valores em 2 a 28
   i = 0
   while (i < len(message_list)):
    if (message_list[i] > 64 and message_list[i] < 91):
        message_list[i] -= 63
    elif (message_list[i] > 96 and message_list[i] < 123):
        message_list[i] -= 95
    elif (message_list[i] == 32):
        message_list[i] = 28
    i += 1

   # cifra a mensagem
   i = 0
   tmp = 0
   while (i < len(message_list)):
    tmp = pow(message_list[i], e, n) #fast mod pow
    message_list[i] = tmp % n
    i += 1

   # escreve a mensagem cifrada em um arquivo txt
   encrypted_msg = open("mensagem_criptografada.txt", "w")
   for item in message_list:
    encrypted_msg.write("%s " % item)

   encrypted_msg.close()
    



