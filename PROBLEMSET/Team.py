def problemasResueltos(n, problemas):
    resueltos = 0
    
    for i in range(n):
        # Leer las opiniones de los tres amigos para el problema i
        petya, vasya, tonya = problemas[i]
        
        # Contar cuántos están seguros sobre la solución
        if petya + vasya + tonya >= 2:
            resueltos += 1
    
    return resueltos

if __name__ == "__main__":
    # Leer el número de problemas
    n = int(input())
    
    # Leer las opiniones para cada problema
    problemas = []
    for _ in range(n):
        problemas.append(list(map(int, input().split())))
    
    # Contar los problemas resueltos
    resultado = problemasResueltos(n, problemas)
    
    # Imprimir el resultados
    print(resultado)
