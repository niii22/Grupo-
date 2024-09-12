"""
CALCULADORA SIMPLES
"""
while True:
    print("Escolha a operação: ")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Sair")
    
    escolha = input("Digite o número da operação desejada: ") # digite um nu´mero de 1 a 4 para selecionar a operação
    
    if escolha == '5': # Ao escolher o némero 5 a operação ira dar um break
        break
    
    num1 = float(input("Digite o primeiro número: ")) # Digite a primeira variavel
    num2 = float(input("Digite o segundo número: ")) # digete a segunda veriavel
    
    if escolha == '1':
        print(f"Resultado: {num1 + num2}")
    elif escolha == '2':
        print(f"Resultado: {num1 - num2}")
    elif escolha == '3':
        print(f"Resultado: {num1 * num2}")
    elif escolha == '4':
        if num2 != 0:
            print(f"Resultado: {num1 / num2}")
        else:
            print("Erro: Divisão por zero!")
    else:
        print("Escolha inválida!") # alguma coisa esta errado 