cod_peca, num_pecas, valor_un = input().split(" ")
cod_peca2, num_pecas2, valor2_un = input().split(" ")

total = int(num_pecas) * float(valor_un) + int(num_pecas2) * float(valor2_un)
print("VALOR A PAGAR: R$ %.2f" %total)