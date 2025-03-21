h_inicial, min_inicial, h_final, min_final = input().split(" ")
h_inicial = int(h_inicial)
min_inicial = int(min_inicial)
h_final = int(h_final)
min_final = int(min_final)

hora = h_final - h_inicial
min = min_final - min_inicial

print(f"O JOGO DUROU {hora} HORA(S) E {min} MINUTOS(S)")
