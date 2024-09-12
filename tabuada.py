# Solicita um número ao usuário
numero = int(input("Digite um número maior que 0: "))

# Verifica se o número inserido é maior que 0
if numero > 0:
    # Se o número é válido, imprime a tabuada
    print(f"Tabuada do {numero}:")
    for i in range(1, 11):  # Loop para valores de 1 a 10
        print(f"{numero} x {i} = {numero * i}")  # Calcula e imprime o resultado da multiplicação
else:
    # Se o número não for maior que 0, exibe uma mensagem de erro
    print("Número inválido! Por favor, insira um número maior que 0.")