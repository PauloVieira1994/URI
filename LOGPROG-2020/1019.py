N = int(input(""))
a=N%3600
H = (N-a)/3600
b= a%60
M =(a-b)/60
c=b%1
S= b-c
print("{:.0f}:{:.0f}:{:.0f}".format(H,M,S))