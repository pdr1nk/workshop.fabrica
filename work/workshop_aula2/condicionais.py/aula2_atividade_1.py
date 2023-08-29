n=input("digite um numero: ")
n1=0
n0=0

try:
    n1=int(n)+1
    n0=int(n)-1
    print(f"o sucessor desse numero é {n1} e o antecessor é {n0}")
except ValueError:
    raise ValueError("digite um numero valido")