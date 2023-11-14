
import random

print("\n\n")
print ("Bem vindo ao jogo da adivinhação.")
print("\n")

numero_secreto = random.randrange(1,301)
numero_de_tentativas = 1

while(numero_de_tentativas < 4):

    print(f"\n*****Tentativa número {numero_de_tentativas} de 3*****")
    chute = int(input ("Por favor informe o número de 1 a 300: "))
    print(f"\nVocê digitou o número {chute}.")

    if ( chute < 1 or chute >300):
        print ("Número inválido. Por favor informe um número de 1 a 300.\n")
        continue
    elif (chute == numero_secreto):
        print("Parabéns, resposta Certa! \n")
        break
    elif (chute < numero_secreto):
        print("Resposta errada.\nO número a ser adivinhado é maior!\n")
    else:
        print ("Resposta errada.\nO número a ser adivinhado é menor!\n")
    
    numero_de_tentativas += 1

print("\nFim de Jogo.")