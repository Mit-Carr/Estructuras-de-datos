import pandas as pd
import numpy as np
#Carrillo Uicab Mitchel
#
# los que se usaran para crear el dataframe ---
departamentos = ['Ropa', 'Deportes', 'Juguetería']
meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 
         'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']

# Creamos el DataFrame (la tabla) inicializado con ceros.
ventas_df = pd.DataFrame(0.0, index=departamentos, columns=meses)

# --- 2. MÉTODOS ---
def insertar_venta(df, depto, mes, monto):
    """Inserta o actualiza un monto en la tabla."""
    df.loc[depto, mes] = monto
    print(f" Venta registrada con éxito: [{depto}, {mes}] = ${monto:,.2f}")

def buscar_venta(df, depto, mes):
    """Busca y muestra una venta en particular."""
    monto = df.loc[depto, mes]
    if monto == 0.0:
        print(f"No hay venta registrada para [{depto}, {mes}].")
    else:
        print(f"Venta encontrada: [{depto}, {mes}] = ${monto:,.2f}")

def eliminar_venta(df, depto, mes):
    """Elimina una venta particular, estableciéndola en 0."""
    # "Eliminar" en este contexto significa volver a poner el valor en 0.
    df.loc[depto, mes] = 0.0
    print(f"🗑️ Venta eliminada para [{depto}, {mes}]. La venta ahora es $0.00")

def mostrar_tabla(df):
    """Muestra la tabla de ventas completa."""
    print("\n--- Tabla de Ventas Actual ---")
    print(df.to_string(float_format="%.2f"))

# menu principal ---
if __name__ == "__main__":
    while True:
        print("\n===== GESTIÓN DE VENTAS =====")
        print("1. Ingresar Venta")
        print("2. Buscar Venta")
        print("3. Eliminar Venta")
        print("4. Mostrar Tabla Completa")
        print("5. Salir")
        
        opcion = input("Elige una opción (1-5): ")

        # --- Lógica para Ingresar Venta ---
        if opcion == '1':
            print("\n--- Departamentos Disponibles:", ", ".join(departamentos))
            depto_usuario = input("Introduce el departamento: ").strip().capitalize()
            if depto_usuario not in departamentos:
                print(f" Error: Departamento no válido.")
                continue

            print("--- Meses Disponibles:", ", ".join(meses))
            mes_usuario = input("Introduce el mes: ").strip().capitalize()
            if mes_usuario not in meses:
                print(f" Error: Mes no válido.")
                continue

            try:
                monto_str = input(f"Introduce el monto para [{depto_usuario}, {mes_usuario}]: ")
                monto = float(monto_str)
                insertar_venta(ventas_df, depto_usuario, mes_usuario, monto)
            except ValueError:
                print(" Error: El monto debe ser un número.")

        # --- Lógica para Buscar o Eliminar ---
        elif opcion in ['2', '3']:
            print("\n--- Departamentos Disponibles:", ", ".join(departamentos))
            depto_usuario = input("Introduce el departamento: ").strip().capitalize()
            if depto_usuario not in departamentos:
                print(f" Error: Departamento no válido.")
                continue

            print("--- Meses Disponibles:", ", ".join(meses))
            mes_usuario = input("Introduce el mes: ").strip().capitalize()
            if mes_usuario not in meses:
                print(f"Error: Mes no válido.")
                continue

            if opcion == '2':
                buscar_venta(ventas_df, depto_usuario, mes_usuario)
            elif opcion == '3':
                eliminar_venta(ventas_df, depto_usuario, mes_usuario)

        elif opcion == '4':
            mostrar_tabla(ventas_df)
        
        elif opcion == '5':
            print("Saliendo del programa.")
            break
        
        else:
            print(" Opción no válida. Por favor, elige un número del 1 al 5.")