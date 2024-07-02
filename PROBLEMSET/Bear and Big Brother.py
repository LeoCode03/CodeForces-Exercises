def calcular_anios(l, b):
    contador = 0
    while l <= b:
        l *= 3
        b *= 2
        contador += 1
    return contador

if __name__ == "__main__":
    l, b = map(int, input().split())
    resultado = calcular_anios(l, b)
    print(resultado)
