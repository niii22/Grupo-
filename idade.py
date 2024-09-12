def classificar_idade(idade):
    """Classifica a pessoa com base na idade"""
    if idade < 18:
        return "Menor de idade"
    elif 18 <= idade < 60:
        return "Adulto"
    else:
        return "Idoso"

while True:
    # Pergunta a idade da pessoa
    try:
        idade = int(input("Digite a idade da pessoa (ou digite -1 para parar): "))

        if idade == -1:
            print("Programa encerrado.")
            break  # Sai do laço se o usuário digitar -1
        elif idade < 0:
            print("Idade inválida. Tente novamente.")
        else:
            # Classifica a idade e exibe o resultado
            classificacao = classificar_idade(idade)
            print(f"A pessoa é: {classificacao}")
    except ValueError:
        print("Entrada inválida. Por favor, insira um número inteiro.")
