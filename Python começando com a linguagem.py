
print("\n\n")
print ("Bem vindo ao jogo da adivinhação.")
print("\n\n")

numero_secreto = 43
numero_de_tentativas = 1

while(numero_de_tentativas < 4):

    print(f"***Tentativa número {numero_de_tentativas} de 3***")
    chute = int(input ("Por favor informe o número inteiro positivo: "))
    print(f"\nVocê digitou o número {chute}. \n")
    
    if (chute == numero_secreto):
        print("Parabéns, resposta Certa!\n")
        break
    elif (chute < numero_secreto):
        print("Resposta errada.\nO número a ser adivinhado é maior\n!")
    else:
        print ("Resposta errada.\nO número a ser adivinhado é menor!\n")
    
    numero_de_tentativas += 1

print("Fim de Jogo.\n")