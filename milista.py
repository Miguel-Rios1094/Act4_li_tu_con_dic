# ejemplo de uso de listas
misvecinos=["Juan","Pablo","Fernando"]
misnumeros=[666,777,888]
# Mostrando Mis Vecinos
print(misvecinos)
# Mostrando mis numeros raros
print(misnumeros)
print("---accediendo a los elementos de la lista---")
print(misvecinos[0])
if "Ana" in misvecinos:
  print("Si, 'juan' Esta en la lista de mis vecinos")
else:
  print("Chale no eres mi vecino")
  print("Numero de vecinos")
  Vvecinos=len(misvecinos)
  print(f"Numero de vecinos = {Vvecinos}")
  print("ciclo for en listas")
  posicion=0
  for mivecinote in misvecinos:
    print(posicion," ",mivecinote)
    posicion=posicion+1