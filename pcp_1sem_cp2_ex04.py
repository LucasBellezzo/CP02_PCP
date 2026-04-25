# Exercício 4

# Definição das funções
def calcularHorasExtras(salarioBase, horasExtras):
    valorHorasExtras = (salarioBase * 0.015) * horasExtras
    return valorHorasExtras


def calcularDescontosFaltas(salarioBase, faltas):
    descontoFaltas = (salarioBase * 0.02) * faltas
    return descontoFaltas


def calcularBonus(cargo, temBonus):
    if temBonus == "S" or temBonus == "s":
        match cargo:
            case 1:
                bonus = 1000
            case 2:
                bonus = 500
            case 3:
                bonus = 300
            case 4:
                bonus = 100
        return bonus
    else:
        return


def calcularSalarioFinal(salarioBase, valorHorasExtras, bonus, descontoFaltas):
    salarioFinal = salarioBase + valorHorasExtras + bonus - descontoFaltas
    return salarioFinal


# Coleta de informações
nome = input("Nome do funcionário: ")
cargo = int(input("Informe o digito do cargo referente (1 - Gerente; 2 - Analista; 3 - Assistente; 4 - Estagiário): "))
salarioBase = float(input("Salário Base: "))
horasExtras = int(input("Total de horas extras trabalhadas: "))
faltas = int(input("Total de faltas no mês: "))
temBonus = input("Bônus por desempenho (S / N): ")

# Chamada das funções
valorHorasExtras = calcularHorasExtras(salarioBase, horasExtras)
descontoFaltas = calcularDescontosFaltas(salarioBase, faltas)
bonus = calcularBonus(cargo, temBonus)
salarioFinal = calcularSalarioFinal(salarioBase, valorHorasExtras, bonus, descontoFaltas)

# Resultados
print()
print(f"===== Salário final e descontos de {nome} =====")
print(f"Salário bruto: R${salarioBase}")
print(f"Total de acréscimos: R${valorHorasExtras + bonus} | Horas Ext. R${valorHorasExtras} | Bônus: R${bonus}")
print(f"Total de descontos: R${descontoFaltas}")
print(f"Salário Final: R${salarioFinal}")
print("================================================")

