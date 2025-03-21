N = int(input())
notas = [100, 50, 20, 10, 5, 2, 1]
q_notas = []

for nota in notas:
        quantidade = N // nota
        q_notas.append(quantidade)
        N = N % nota


for i in range(len(notas)):
    print(f"{q_notas[i]} nota(s) de R$ {notas[i]},00")