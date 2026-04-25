# Exercício 1

estado = int(input("Digite o código do estado de origem (1 a 5): "))
peso_toneladas = float(input("Digite o peso da carga em toneladas: "))
codigo_carga = int(input("Digite o código da carga (10 a 40): "))

peso_kg = peso_toneladas * 1000

if codigo_carga >= 10 and codigo_carga <= 20:
    preco_kg = 100
elif codigo_carga >= 21 and codigo_carga <= 30:
    preco_kg = 250
elif codigo_carga >= 31 and codigo_carga <= 40:
    preco_kg = 340

preco_carga = peso_kg * preco_kg

if estado == 1:
    imposto = preco_carga * 0.35
elif estado == 2:
    imposto = preco_carga * 0.25
elif estado == 3:
    imposto = preco_carga * 0.15
elif estado == 4:
    imposto = preco_carga * 0.05
else:
    imposto = 0

valor_total = preco_carga + imposto

print(f"Peso em quilos: {peso_kg:.2f} kg")
print(f"Preço da carga: R$ {preco_carga:.2f}")
print(f"Valor do imposto: R$ {imposto:.2f}")
print(f"Valor total transportado: R$ {valor_total:.2f}")