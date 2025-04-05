Numeros=[10,6,11,5,3,1]
print(Numeros)
for i in range(1,len(Numeros)):
 extract=Numeros[i]
 j=i-1
 while j>=0 and Numeros[j]>extract:
  Numeros[j+1]=Numeros[j]
  j-=1
  
  
 Numeros[j+1] = extract
 
 print(Numeros)