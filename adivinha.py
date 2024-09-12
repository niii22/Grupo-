import random # # Importa o módulo random para gerar números aleatórios

def adivinhacao(): # esta variavel ira adivinhar numeros
    numero = random.randint(1, 50) # escolha um número aleatorio entre 1 e 50
    tentativas = 5 # define o número de tentativas
    
    print("Bem-vindo ao jogo de adivinhação!") # mensagem de boas vindas
    print("Tente adivinhar o número entre 1 e 50.") # instrui o usuario sobre o objetivo do jogo
    
    for tentativa in range(tentativas):# loop que permite até 5 tentativas
        palpite = int(input(f"Tentativa {tentativa + 1}/{tentativas}: ")) #pede ao usuario um palpite e converte para inteiro
        
        if palpite < numero: # Verifica se o palpite é menor que o número escolhido
            print("O número é maior.") #  Informa ao usuário que o número é maior
        elif palpite > numero:
            print("O número é menor.") # Informa ao usuário que o número é menor
        else:
            print(f"Parabéns! Você acertou o número {numero}!") # Informa que o usuário acertou
            break
    else:
        print(f"Você perdeu! O número era {numero}.") # Informa ao usuário que ele perdeu e mostra o número correto


adivinhacao() # Chama a função para iniciar o jogo
