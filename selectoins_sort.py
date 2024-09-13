def bubblesort(S):
  n = len(S)
  for i in range(n):
    print(S) # untuk mengetahui proses yang terjadi
    smallest = i
    for j in range(i + 1,n):
      if S[j] < S[smallest]:
        smallest = j
    S[i], S[smallest] = S[smallest], S[i]
        
S = [50,30,40,10,20]
print("Sebelum di sortir", S)
bubblesort(S)
print("Setelah di sortir", S)