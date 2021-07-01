

def f(n):
    """
    Esta funcion representa una funcion que crece de una manera de O(n) o bigO(n)
    en el big o importa el como se comporta la funcion es decir los exponenciales
    """
    #O(n)
    for i in range(n):  

        print(i)
    #O(n)

    for j in range(n):
        print(i)

    # O(n) + O(n)= O(n+n) =O(2n) = O(n) Se reduce 2n a n ya que mientras vaya creciendo al infinito el 2 no importa

    # Funcion n*n

def f(n):
"""
Esta funcion representa una funcion que crece de una manera de O(n) o bigO(n)
en el big o importa el como se comporta la funcion es decir los exponenciales
"""
#O(n)
for i in range(n):  

    print(i)

#O(n*n)

for j in range(n*n):
    print(i)

# O(n) + O(n*n)= O(n+(n*n)) =O(n+n**2) = O(n**2) Se reduce n+n**2 a n**2 
# ya que mientras vaya creciendo al infinito no importa n

# Ley de la Multiplicacion
def f(n):
"""
Esta funcion representa una funcion que crece de una manera de O(n) o bigO(n)
en el big o importa el como se comporta la funcion es decir los exponenciales
"""
#O(n)
for i in range(n):  
    for j in range(n):
        print(i,j)

# O(n) + O(n)= O(n*n) =O(n**2) = O(n**2)

#recursividad Multiple
def fibonacci(n):
    
    if n==0 or n==1:
        return 1
    return fibonacci(n-1)+fibonacci(n-2)

#en este caso es # O(2**n)