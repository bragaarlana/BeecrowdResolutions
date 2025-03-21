a, b, c = input().split(" ")
a = float(a)
b = float(b)
c = float(c)

print(type(a))
if a >= (b+c):
    print("NAO FORMA TRIANGULO")
else:
    if pow(a,2) == pow(b,2) + pow(c,2):
        print("TRIANGULO RETANGULO")
    elif pow(a,2) > (pow(b,2) + pow(c,2)):
        print("TRIANGULO OBTUSANGULO")
    elif pow(a,2) < (pow(b,2) + pow(c,2)):
        print("TRIANGULO ACUTANGULO")
    if a == b == c:
        print("TRIANGULO EQUILATERO")
    elif a == b or b==c or a==c:
        print("TRIANGULO ISOSCELES")
