print ('*********************************************')
print ('Bem vindo ao Vidente, seu jogo de adivinhação')
print ('*********************************************')

chute = int(input('Digite seu número: '))

numero_secreto = 7
acertou = chute == numero_secreto
chute_maior = chute > numero_secreto
chute_menor = chute < numero_secreto



print (f'Você  digitou {chute} ')

if(acertou):
    print('Você acertou! Parabéns, tu é vidente.')
else:
    if(chute_maior):
        print('Você errou! Seu número foi maior do que o número secreto')
    elif(chute_menor):
        print('De vidente não tem nada <3, seu número é menor do que o número secreto.')

print('@@@@@@@@@@@')
print('Fim de jogo')
print('@@@@@@@@@@@')