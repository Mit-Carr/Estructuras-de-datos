def evaluar_expresion(expresion, notacion='posfija'):
    pila = []
    
    if notacion == 'posfija':
        tokens = expresion.split()
    elif notacion == 'prefija':
        tokens = expresion.split()[::-1]
    else:
        raise ValueError("Notación no válida. Use 'posfija' o 'prefija'.")

    for token in tokens:
        try:
            pila.append(float(token))
        except ValueError:
            if len(pila) < 2:
                raise ValueError("Error de sintaxis: Faltan operandos.")

            if notacion == 'posfija':
                operando2 = pila.pop()
                operando1 = pila.pop()
            else:
                operando1 = pila.pop()
                operando2 = pila.pop()

            if token == '+':
                pila.append(operando1 + operando2)
            elif token == '-':
                pila.append(operando1 - operando2)
            elif token == '*':
                pila.append(operando1 * operando2)
            elif token == '/':
                if operando2 == 0:
                    raise ValueError("Error: División por cero.")
                pila.append(operando1 / operando2)
            else:
                raise ValueError(f"Operador desconocido: {token}")

    if len(pila) != 1:
        raise ValueError("Error de sintaxis: Sobran operandos.")

    return pila[0]


expresion_posfija = "3 4 + 2 *"
resultado1 = evaluar_expresion(expresion_posfija, notacion='posfija')
print(f"La expresión posfija '{expresion_posfija}' da como resultado: {resultado1}")

expresion_prefija = "* + 3 4 2"
resultado2 = evaluar_expresion(expresion_prefija, notacion='prefija')
print(f"La expresión prefija '{expresion_prefija}' da como resultado: {resultado2}")

expresion_compleja_posfija = "5 1 2 + 4 * + 3 -"
resultado3 = evaluar_expresion(expresion_compleja_posfija, 'posfija')
print(f"La expresión compleja '{expresion_compleja_posfija}' da como resultado: {resultado3}")

expresion_negativa = "10 -5 + 3 *"
resultado4 = evaluar_expresion(expresion_negativa)
print(f"La expresión con negativos '{expresion_negativa}' da como resultado: {resultado4}")
