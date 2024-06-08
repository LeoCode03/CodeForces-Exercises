def ordenarCreciente(cad):
    separandoCadena = cad.split('+') # Divide la cadena usando como separador +
    separandoCadena.sort() # Ordenar la lista de numeros en forma ascendente
    return '+'.join(separandoCadena) # Une la lista usando + como separador entre cada elemento
if __name__ == "__main__":
    cad = input()
    print(ordenarCreciente(cad))
