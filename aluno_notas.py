 #Inicializa listas para armazenar os nomes e notas dos alunos
nomes = []
notas = [9]

# Solicita os dados para 5 alunos
for i in range(5):
    nome = input(f"Digite o nome do {i + 1}º aluno: ")  # Recebe o nome do aluno
    nota = float(input(f"Digite a nota de {nome}: "))  # Recebe a nota do aluno e converte para float
    nomes.append(nome)  # Adiciona o nome à lista de nomes
    notas.append(nota)  # Adiciona a nota à lista de notas

# Calcula a média da turma
media = sum(notas) / len(notas)

# Exibe a média da turma
print(f"\nMédia da turma: {media:.2f}")

# Classifica cada aluno como Aprovado ou Reprovado
for i in range(5):
    if notas[i] >= 7:
        resultado = "Aprovado"
    else:
        resultado = "Reprovado"
    
    # Exibe o nome do aluno e seu status
    print(f"Aluno: {nomes[i]}, Nota: {notas[i]:.2f}, Status: {resultado}")