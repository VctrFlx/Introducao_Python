# EXERCICIO 05
print ("Calculadora de raízes reais via Bhaskara")
a = float(input("Digite o valor de A: "))
b = float(input("Digite o valor de B: "))
c = float(input("Digite o valor de C: "))
delta = b ** 2 - 4 * a * c
x1 = (-b + (delta ** 0.5)) / (2 * a)
x2 = (-b - (delta ** 0.5)) / (2 * a)
print("X1 =", x1)
print("X2 =", x2)