# EXERCICIO 16
print ("Cálculadora do salário líquido")
horas = float(input("Digite a quantidade de horas trabalhadas: "))
valor_hora = float(input("Digite o valor por hora: R$ "))
perc_desc = float(input("Digite o percentual de desconto: "))
dependentes = int(input("Digite o número de dependentes: "))
sal_bruto = horas * valor_hora
desconto = sal_bruto * perc_desc / 100
sal_liquido = sal_bruto - desconto
sal_liquido = sal_liquido + (dependentes * 100)
print ("Salário: R$", sal_liquido)