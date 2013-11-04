# coding: utf-8
# Calcula os preços de combustíveis.

litros_vendidos = input("Insira os litros vendidos: ")
tipo_combustivel = raw_input("Insira o tipo de combustivel [G/A]: ")

if tipo_combustivel == "G":
    if litros_vendidos <= 20:
        valor = litros_vendidos * (2.50*0.96)
        print "Valor e R$%.2f ." % valor
    else:
        valor = litros_vendidos * (2.50*0.94)
        print "Valor e R$%.2f ." % valor
elif tipo_combustivel == "A":
    if litros_vendidos <= 20:
        valor = litros_vendidos * (1.90*0.97)
        print "Valor e R$%.2f ." % valor
    else:
        valor = litros_vendidos * (1.90*0.95)
        print "Valor e R$%.2f ." % valor
else:
    print "Tipo de combustivel errado."
	
raw_input("Pressione qualquer tecla para continuar...")
