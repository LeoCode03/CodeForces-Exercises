def palabraLarga(p):
    if len(p) > 10:
        return p[0] + str(len(p) - 2) + p[-1]
    else:
        return p

if __name__ == "__main__":
    n = int(input())
    palabras = [input() for _ in range(n)]
    
    for palabra in palabras:
        print(palabraLarga(palabra))
