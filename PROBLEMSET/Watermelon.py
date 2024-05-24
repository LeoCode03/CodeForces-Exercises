
def dividirSandia(w):
    if w>2 and w % 2 == 0:
        return "YES"
    else:
        return "NO"    
    
if __name__ == "__main__":
    s = int(input())
    print(dividirSandia(s))