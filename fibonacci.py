def fibonacci(n):
    a = 0
    b = 1
    
    # Check if n is less than 0
    if n < 0:
        print("Incorrect input")
        
    # Check if n is equal to 0
    elif n == 0:
        return 0
      
    # Check if n is equal to 1
    elif n == 1:
        return b
    else:
        for i in range(1, n):
            c = a + b
            a = b
            b = c
        return b


print(fibonacci(18))

def fibonacci_recursivo(n):
  # Caso base 1: si n es 0, el resultado es 0.
  if n == 0:
    return 0
  
  # Caso base 2: si n es 1, el resultado es 1.
  elif n == 1:
    return 1
    
  # Caso recursivo: para cualquier otro número,
  # es la suma de los dos números de Fibonacci anteriores.
  else:
    return fibonacci_recursivo(n-1) + fibonacci_recursivo(n-2)

# --- Pruebas ---
print(f"Fibonacci de 9 es: {fibonacci_recursivo(9)}")   # Salida: 34
print(f"Fibonacci de 18 es: {fibonacci_recursivo(18)}") # Salida: 2584
