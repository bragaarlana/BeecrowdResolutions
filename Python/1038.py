cod_item, q_item= input().split(" ")

if int(cod_item) == 1:
 total = int(q_item) * 4.00

elif int(cod_item) == 2:
 total = int(q_item) * 4.50

elif int(cod_item) == 5:
 total = int(q_item) * 5.00

elif int(cod_item) == 4:
 total = int(q_item) * 2.00

elif int(cod_item) == 5:
 total = int(q_item) * 1.50

print("Total: R$ %.2f" %total)