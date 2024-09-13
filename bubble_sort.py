def bubblesort(S):
  n = len(S)
  print(n)
  for i in range(n):
    print(S) # untuk mengetahui proses yang terjadi
    for j in range(n - 1):
      if S[j] > S[j + 1]:
        S[j], S[j + 1] = S[j + 1], S[j]
        
S = [50,30,40,10,20]
print("Sebelum di sortir", S)
bubblesort(S)
print("Setelah di sortir", S)