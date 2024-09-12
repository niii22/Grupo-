def calcular_fatorial():  
    # Solicita um número inteiro positivo ao usuário  
    numero = int(input("Insira um número inteiro positivo: "))  # insira o número inteiro
    
    # Verifica se o número é positivo  
    if numero < 0:  
        print("Por favor, insira um número positivo.")  
        return  # Encerra a função se o número não for positivo  
    
    fatorial = 1  # Inicializa o fatorial como 1  

    # Calcula o fatorial usando um loop  
    for i in range(1, numero + 1):  
        fatorial *= i  # Multiplica o fatorial pelo número atual  

    # Exibe o resultado  
    print(f"O fatorial de {numero} é: {fatorial}")  

# Chama a função para calcular o fatorial  
calcular_fatorial() # calcular a forma final.