total_animales = int(input())
animales = []
for _ in range(total_animales):
    partes = input().split()
    nombre = partes[0]
    cantidad_características = int(partes[1])
    características = set(partes[2:])
    animales.append(características)
maximo_si_respuestas = 0
for i in range(total_animales):
    for j in range(i+1, total_animales):
        comunes = animales[i] & animales[j]
        maximo_si_respuestas = max(maximo_si_respuestas, len(comunes)+1)
print(maximo_si_respuestas)