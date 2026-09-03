# EXERCICIO 17
print ("Calculadora de consumo de combustível")
tempo = float(input("Digite o tempo de percurso em horas: "))
velocidade = float(input("Digite a velocidade média em km/h: "))
distancia = tempo * velocidade
litros = distancia / 12
print ("Distância percorrida:", distancia ,"km")
print ("Quantidade de litros gastos:", litros ,"L")