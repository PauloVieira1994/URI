import math
A,B,C = input().split(" ")
A=float(A)
B=float(B)
C=float(C)
delta = (B**2)-4*A*C
if delta<0 or A==0:
  print("Impossivel calcular")
else:
  x= math.sqrt(delta)
  R1= (-B+x)/ (2*A)
  R2= (-B-x)/ (2*A)
  print("R1 = {:.5f}".format(R1))
  print("R2 = {:.5f}".format(R2))