salario = float(input())
imposto = 0

if salario <= 2000.00:
    print("Isento")
else:
    if salario > 2000.00 and salario <= 3000.00:
        imposto = imposto + (salario - 2000.00) * 0.08
    elif salario > 3000.00 and salario <= 4500.00:
        imposto = imposto + (3000.00 - 2000.00) * 0.08
        imposto = imposto + (salario - 3000.00) * 0.18
    elif salario > 4500.00:
        imposto = imposto + (3000.00 - 2000.00) * 0.08
        imposto = imposto +(4500.00 - 3000.00) * 0.18
        imposto = imposto +(salario - 4500.00) * 0.28
    
    print("R$ %.2f" %imposto)