n1, n2, n3, n4 = input().split(" ")

media = (float(n1)*2 + float(n2)*3 + float(n3)*4 + float(n4)*1)/ 10

print("Media: %.1f" %media)
if media >= 7.0:
    print("Aluno aprovado.")
elif media < 5.0:
    print("Aluno reprovado.")
elif  5<= media <= 6.9:
    print("Aluno em exame.")
    nota_exame = float(input())
    print("Nota do exame: %.1f" %nota_exame)
    
    media = (media + nota_exame)/2

    if media >= 5.0:
        print("Aluno aprovado.")
    elif media < 5.0:
        print("Aluno reprovado.")

print("Media final: %.1f" %media)