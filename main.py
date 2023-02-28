'''
cambios
'''

def imprimirArreglo (arreglo):
  for i in range (len(arreglo)):
    print(f"[{arreglo [i]}]", end='')

def algoritmo_Burbuja(arreglo):
  for i in range (len(arreglo)-1):
    for j in range (len(arreglo)-1-i):
      if arreglo[j]>arreglo[j+1]:
        aux=arreglo[j]
        arreglo[j]=arreglo[j+1]
        arreglo[j+1]=aux


listaSueldos=[20.8,54.56,80.14,56.12]
imprimirArreglo(listaSueldos)
algoritmo_Burbuja(listaSueldos)
print("\nLa lista de sueldos ordenado es:\n\n")
imprimirArreglo(listaSueldos)







