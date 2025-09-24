def analizar_temperaturas_semanales():
   
    temperaturas = []
    dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

    print("Por favor, introduce las temperaturas de la semana:")
    for dia in dias_semana:
        while True:
            try:
                
                temp_dia = float(input(f"Temperatura del {dia}: "))
                temperaturas.append(temp_dia)
                break  
            except ValueError:
                print("Error: Por favor, introduce un número válido.")

    
    promedio = sum(temperaturas) / len(temperaturas)

    
    
    temp_max = max(temperaturas)
    temp_min = min(temperaturas)

    
    dias_superiores = 0
    for temp in temperaturas:
        if temp > promedio:
            dias_superiores += 1

    
    print("\n--- Resultados del Análisis Climático Semanal ---")
    print(f" Temperatura promedio: {promedio:.2f}°C")
    print(f" Temperatura más alta: {temp_max}°C")
    print(f" Temperatura más baja: {temp_min}°C")
    print(f"Días con temperatura superior al promedio: {dias_superiores} día(s)")


analizar_temperaturas_semanales()
