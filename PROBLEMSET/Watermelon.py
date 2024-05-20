
def dividirSandia(w):
    if w>2 and w % 2 == 0:
        return "YES"
    else:
        return "NO"    
    
if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    w = int(input().strip())
    print(dividirSandia(w))