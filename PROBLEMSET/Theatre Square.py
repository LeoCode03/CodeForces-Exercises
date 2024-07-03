import math
def calcularTamanio(n, m, a):
    lozas_n = math.ceil(n/a)
    lozas_m = math.ceil(m/a)
    cantidad_lozas = lozas_n * lozas_m
    return cantidad_lozas

if __name__ == "__main__":
    n, m, a = map(int, input().split())
    resultado = calcularTamanio(n, m, a)
    print(resultado)