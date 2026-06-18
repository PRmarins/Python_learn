salario = float(input())

if salario <= 2000:
    print('Isento')

elif 2000 < salario <= 3000:
    imposto = (salario - 2000) * 0.08
    print (f"R$ {imposto:.2f}")

elif 3000 < salario <= 4500:
    imposto_1 = (salario - 3000) * 0.18
    imposto_2 = 1000 * 0.08
    print(f'R$ {imposto_1+imposto_2:.2f}')

elif salario > 4500:
    imposto_1 = (salario - 4500) * 0.28
    imposto_2 = 1500 * 0.18
    imposto_3 = 1000 * 0.08
    print(f'R$ {imposto_1+imposto_2+imposto_3:.2f}')