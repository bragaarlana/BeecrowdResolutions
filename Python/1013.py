A,B,C = map(int, input().split())

maiorAB = (A+B+abs(A-B))/2
maior = (maiorAB+C+abs(maiorAB-C))/2

print(f"{maior:.0f} eh o maior")