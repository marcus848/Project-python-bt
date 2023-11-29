#COLOCANDO APORTE NA CALCULADORA DE JUROS COMPOSTOS
nome = str(input("Qual é o seu nome? "))
print(f"Olá {nome}, seja muito bem vindo aos juros compostoa! Aqui nós cuidamos da sua aposentadoria: ")

dinheiro_inicial = int(input("Digite a quantidade de dinheiro inicial do investimento: "))
tempo_desejado = int(input("Digite quantos meses você deixará o dinheiro investido: "))
taxa = float(input("Digite, em decimal, qual a taxa mensal de retorno do seu investimento: "))
aporte = int(input("Quanto dinheiro você consegue aportar por mês"))
salario_desejado = int(input("Digite o salário mensal que você quer receber ao se aposentar"))
tempo_decorrido = 0
while tempo_decorrido < tempo_desejado:
    if tempo_decorrido == 0:

        montante = dinheiro_inicial * (1 + taxa) ** 1
        montante = round(montante, 2)
        tempo_decorrido = tempo_decorrido + 1

    else:
        montante = (montante + aporte)* (1 + taxa) ** 1
        montante = round(montante, 2)
        tempo_decorrido = tempo_decorrido + 1
print("---------------------------------------")

print(f"Parabéns {nome}! Ao final do periodo você terá R${montante} ")
salario_mensal = (montante * taxa)
salario_mensal = round(salario_mensal, 2)

if salario_mensal >= salario_desejado:
    print(f"Parabéns, você pode se aposentar! Seu salário mensal com esse montante é de R$ {salario_mensal}")
elif salario_mensal < salario_desejado:
    print(f"Infelizmente se aposentar não será possivel. Com esse montante seu salário mensal é de R$ {salario_mensal}")
breakpoint()
#---------------------------------------