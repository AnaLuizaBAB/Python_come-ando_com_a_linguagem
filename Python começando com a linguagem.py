
print("\n\n")
print ("Bem vindo ao jogo da adivinhação.")
print("\n\n")

numero_secreto = 43
chute = int(input ("Informe o número inteiro positivo: "))

print(f"\n\nVocê digitou o número {chute}.")

if (chute == numero_secreto):
    print("Parabéns resposta Certa! \n")
else:
    print("Resposta errada.\n")