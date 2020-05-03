a,b = input().split(" ")
a=int(a)
b=int(b)
x1=4
x2=4.5
x3=5
x4=2
x5=1.5
if a==1:
  print("Total: R$ {:.2f}".format(x1*b))
elif a==2:
  print("Total: R$ {:.2f}".format(x2*b))
elif a==3:
  print("Total: R$ {:.2f}".format(x3*b))  
elif a==4:
  print("Total: R$ {:.2f}".format(x4*b))
elif a==5:
  print("Total: R$ {:.2f}".format(x5*b))