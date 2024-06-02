if __name__ == "__main__":
    s1 = input().strip()
    s2 = input().strip()
    
    cadena1 = s1.lower()
    cadena2 = s2.lower()
    
    if cadena1 < cadena2:
        print("-1")
    elif cadena1 > cadena2:
        print("1")
    else:
        print("0")