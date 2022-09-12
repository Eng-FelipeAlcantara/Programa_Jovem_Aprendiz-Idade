#Programa para definir um intervalo de idade em que o estudante tenha prioridade no Programa Jovem Aprendiz
nome = input("Digite o nome: ")
idade = int(input("Digite a idade: "))
prioritario = "NÃO"
if idade >= 14 and idade <= 16:
    prioritario: "SIM"
else: idade: "NÃO"
print("O estudante", nome, "possui atendimento prioritario para o Programa Jovem Aprendiz?", prioritario)
