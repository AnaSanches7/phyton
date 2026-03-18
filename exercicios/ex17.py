dias = int(input("Dias de aluguel: "))
km = float(input("Km rodados: "))
diaria = dias*60
percurso = km*0.15
custo = diaria + percurso

print('O total a pagar é de R${:.2f}'.format(custo))