# Função que determina a situação do aluno com base na média
def calcular_situacao(media):
    # Se a média é 7 ou mais, o aluno está aprovado
    if media >= 7:
        return "Aprovado"
    # Se a média é entre 4 e 7, o aluno está em recuperação
    elif media >= 4:
        return "Recuperação"
    # Se a média é abaixo de 4, o aluno está reprovado
    else:
        return "Reprovado"

# Função para obter e validar as notas do aluno
def obter_notas():
    while True:
        try:
            # Solicita a primeira nota ao usuário
            nota1 = float(input("Digite a primeira nota: "))
            # Solicita a segunda nota ao usuário
            nota2 = float(input("Digite a segunda nota: "))
            # Verifica se as notas estão dentro do intervalo permitido (0 a 10)
            if 0 <= nota1 <= 10 and 0 <= nota2 <= 10:
                return nota1, nota2  # Retorna as notas válidas
            else:
                print("Notas devem estar entre 0 e 10. Tente novamente.")  # Mensagem de erro para notas fora do intervalo
        except ValueError:
            print("Entrada inválida. Por favor, insira números válidos.")  # Mensagem de erro para entradas não numéricas

# Função principal que controla o fluxo do programa
def main():
    while True:
        print("Cadastro de notas de alunos")  # Mensagem de início para o cadastro de notas
        nota1, nota2 = obter_notas()  # Chama a função para obter as notas do aluno
        media = (nota1 + nota2) / 2  # Calcula a média das notas
        situacao = calcular_situacao(media)  # Determina a situação do aluno com base na média
        print(f"Média: {media:.2f} - Situação: {situacao}")  # Exibe a média e a situação do aluno
       
        # Pergunta ao usuário se deseja inserir notas de outro aluno
        continuar = input("Deseja inserir notas de outro aluno? (s/n): ").strip().lower()
        # Se o usuário não responder 's', o loop é encerrado
        if continuar != 's':
            print("Programa encerrado.")  # Mensagem final
            break

# Ponto de entrada do script
if __name__ == "__main__":
    main()  # Chama a função principal para iniciar o programa.