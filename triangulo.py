
# Função para calcular a área de um triângulo
def calcular_area_triangulo(x1, y1, x2, y2, x3, y3):
    area = abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2)
    return area

# Só será executado pelo pytest
assert calcular_area_triangulo(1,2,4,5,7,1) == 10.5
assert calcular_area_triangulo(1,2,1,5,1,1) == 0
assert calcular_area_triangulo(0,0,0,0,0,0) == 0

# Exemplo de uso
area = calcular_area_triangulo(1, 2, 4, 5, 7, 1)
print(f"A área do triângulo é: {area}")