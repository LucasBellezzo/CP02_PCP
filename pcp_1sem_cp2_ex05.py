# Exercício 5

def pode_aprovar(idade, renda, valor):
    if idade > 18 and valor <= renda * 20:
        return True
    else:
        return False


def definir_taxa(parcelas):
    if parcelas <= 6:
        return 0.05
    elif parcelas <= 12:
        return 0.08
    else:
        return 0.10


def calcular_parcela(valor, taxa, parcelas):
    parcela = valor * (taxa * (1 + taxa) ** parcelas) / ((1 + taxa) ** parcelas - 1)
    return parcela


def calcular_total(parcela, parcelas):
    total = parcela * parcelas
    return total


def calcular_juros(total, valor):
    juros = total - valor
    return juros


print("Sistema de financiamento do banco")

nome = input("Digite o nome do cliente: ")
idade = int(input("Digite a idade: "))
renda = float(input("Digite a renda mensal: R$ "))
valor = float(input("Digite o valor desejado do empréstimo: R$ "))
parcelas = int(input("Digite o número de parcelas entre 3 e 24: "))

if parcelas < 3 or parcelas > 24:
    print("Número de parcelas inválido.")
else:
    aprovado = pode_aprovar(idade, renda, valor)

    if aprovado == True:
        taxa = definir_taxa(parcelas)
        parcela = calcular_parcela(valor, taxa, parcelas)
        total = calcular_total(parcela, parcelas)
        juros = calcular_juros(total, valor)

        print("\nEmpréstimo aprovado!")
        print("Nome do cliente:", nome)
        print("Valor financiado: R$", round(valor, 2))
        print("Taxa de juros aplicada:", taxa * 100, "% ao mês")
        print("Valor da parcela: R$", round(parcela, 2))
        print("Valor total pago: R$", round(total, 2))
        print("Total de juros pagos: R$", round(juros, 2))

    else:
        print("\nEmpréstimo negado.")
        print("O cliente não atende aos requisitos do banco.")