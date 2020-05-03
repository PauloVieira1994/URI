A,B,C = input().split(" ")
A = float (A)
B = float (B)
C = float (C) 
TRIANGULO = A*C/2
print("TRIANGULO: {:.3f}".format(TRIANGULO))
CIRCULO = 3.14159*(C**2)
print("CIRCULO: {:.3F}".format(CIRCULO))
TRAPEZIO = ((A + B)*C)/2
print("TRAPEZIO: {:.3f}".format(TRAPEZIO))
QUADRADO = B**2
print("QUADRADO: {:.3f}".format(QUADRADO))
RETANGULO = A * B
print("RETANGULO: {:.3f}".format(RETANGULO))