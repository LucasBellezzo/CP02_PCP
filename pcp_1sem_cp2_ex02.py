# Exercício 02

a = int(input())
b = int(input())
c = int(input())

a, b, c = sorted([a, b, c], reverse=True)
print(a, b, c)

bc = b + c
bc_square = (b2) + (c2)

if a >= bc:
    print("Não forma triângulo")
else:
    if a2 == bc_square:
        print("Triângulo retângulo")
    elif a2 > bc_square:
        print("Triângulo obtusângulo")
    elif a**2 < bc_square:
        print("Triângulo acutângulo")

    if a == b and a == c:
        print("Triângulo equilátero")
    elif a == b or a == c or b == c:
        print("Triângulo isósceles")
