def suma(n1, n2):
    n=n1+n2
    print("La suma de" , n1 , "y" , n2 , "es" , n)

def numero(n1):
    n2=int(input("Introduzca un segundo numero:"))
    suma(n1,n2)

n1=int(input("Introduzca un numero:"))
numero(n1)