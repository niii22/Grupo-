def calcular_imc(peso, altura):
    """Calcula o IMC e retorna a classificação.

    Args:
        peso (float): Peso da pessoa em quilogramas.
        altura (float): Altura da pessoa em metros.

    Returns:
        str: Classificação do IMC.
    """

    imc = peso / (altura ** 2)

    if imc < 18.5: # se o imc for menor que 18.5 esta abaixo do peso
        return "Abaixo do peso"
    elif 18.5 <= imc < 25:
        return "Peso normal" # igual a 18.5 ou menor de 25 esta com peso normal
    elif 25 <= imc < 30:
        return "Sobrepeso"
    else:
        return "Obesidade"

# Entrada do usuário
peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros: "))

# Chamada da função e exibição do resultado
resultado = calcular_imc(peso, altura)
print(f"Seu IMC é: {resultado}")