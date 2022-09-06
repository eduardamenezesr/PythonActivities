import math
n = float(input("Entre com um número:\n"))
raiz = math.sqrt(2*(math.pi)*n)
e =  2.718281828459045
x = (n / e) ** n
fat = raiz * x

print("O fatorial do número", n, "é",fat)