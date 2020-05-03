a,b,c = input().split(" ")
d,e,f = input().split(" ")
m1 = int(b)*float(c)
m2 = int(e)*float(f)
t = m1+m2
print ("VALOR A PAGAR: R$ {:.2F}".format(t))