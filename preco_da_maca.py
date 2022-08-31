macasCompradas = int(input("Digite o número de maças compradas: "))

if macasCompradas < 12:
    print("O total gasto fica: ", "R$", macasCompradas * 1.30)
    
else:
    print("O total gasto fica: ", "R$", macasCompradas * 1.00)