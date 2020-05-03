N = float(input(""))
if 0 < N < 1000000:
  print ("NOTAS:")
  b = N%100
  print("{:.0f} nota(s) de R$ 100,00".format((N-b)/100))
  c = b%50
  print("{:.0f} nota(s) de R$ 50,00".format((b-c)/50))
  d = c%20
  print("{:.0f} nota(s) de R$ 20,00".format((c-d)/20))
  e = d%10
  print("{:.0f} nota(s) de R$ 10,00".format((d-e)/10))
  f = e%5
  print("{:.0f} nota(s) de R$ 5,00".format((e-f)/5))
  g = f%2
  print("{:.0f} nota(s) de R$ 2,00".format((f-g)/2))
  print("MOEDAS:")
  g=float(g*100)
  h = g%100
  print("{:.0f} moeda(s) de R$ 1,00".format((g-h)/100))
  i = h%50
  print("{:.0f} moeda(s) de R$ 0,50".format((h-i)/50))
  j = i%25
  print("{:.0f} moeda(s) de R$ 0,25".format((i-j)/25))
  k=j%10
  print("{:.0f} moeda(s) de R$ 0,10".format((j-k)/10))
  l= k%5
  print("{:.0f} moeda(s) de R$ 0,05".format((k-l)/5))
  m= l%1
  print("{:.0f} moeda(s) de R$ 0,01".format(l-m))