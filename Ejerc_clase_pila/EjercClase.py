import tkinter as tk
from tkinter import ttk, messagebox, simpledialog

# La clase Pila no necesita cambios en su lógica interna.
class Pila:
    def __init__(self):
        self.items = []
    def apilar(self, elemento): self.items.append(elemento)
    def desapilar(self): return self.items.pop() if not self.esta_vacia() else None
    def cima(self): return self.items[-1] if not self.esta_vacia() else None
    def esta_vacia(self): return len(self.items) == 0
    def limpiar(self): self.items.clear()
    def __len__(self): return len(self.items)

# --- Clase principal de la Interfaz Gráfica ---
class MultiPilaGUI:
    def __init__(self, master):
        self.master = master
        master.title("Visualizador de Pilas Interactivo (Cima Arriba)")
        master.geometry("1100x750")
        
        self.style = ttk.Style(master)
        self.style.theme_use('clam')

        self.pilas = {}
        self.pila_counter = 0

        # --- Layout Principal ---
        self.control_panel = ttk.Frame(master, width=280)
        self.control_panel.pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=10)
        self.control_panel.pack_propagate(False)

        canvas_frame = ttk.Frame(master)
        canvas_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        self.canvas = tk.Canvas(canvas_frame, bg="#f0f0f0")
        self.canvas.pack(fill=tk.BOTH, expand=True, padx=(0,10), pady=(10,0))
        
        self.status_bar = ttk.Label(canvas_frame, text="Bienvenido al Visualizador de Pilas.", anchor=tk.W, font=("Arial", 10))
        self.status_bar.pack(fill=tk.X, padx=(0,10), pady=(5,10))

        self.setup_control_panel()
        
        self.actualizar_controles()
        self.dibujar_canvas()

    def setup_control_panel(self):
        # ... (El resto del setup_control_panel es idéntico y no necesita cambios)
        # 1. Gestión de Pilas
        gestion_frame = ttk.LabelFrame(self.control_panel, text="Gestión de Pilas")
        gestion_frame.pack(fill=tk.X, pady=10)

        self.listbox_pilas = tk.Listbox(gestion_frame, height=8, exportselection=False)
        self.listbox_pilas.pack(fill=tk.X, padx=5, pady=5)
        self.listbox_pilas.bind('<<ListboxSelect>>', self.actualizar_controles)
        self.listbox_pilas.bind('<Double-1>', self.renombrar_pila)

        btn_crear = ttk.Button(gestion_frame, text="Crear Nueva Pila", command=self.crear_pila)
        btn_crear.pack(fill=tk.X, padx=5, pady=(0,5))
        btn_eliminar = ttk.Button(gestion_frame, text="Eliminar Pila", command=self.eliminar_pila)
        btn_eliminar.pack(fill=tk.X, padx=5, pady=(0,5))

        # 2. Operaciones
        ops_frame = ttk.LabelFrame(self.control_panel, text="Operaciones")
        ops_frame.pack(fill=tk.X, pady=10)

        ttk.Label(ops_frame, text="Elemento:").pack(padx=5)
        self.entry_elemento = ttk.Entry(ops_frame)
        self.entry_elemento.pack(fill=tk.X, padx=5, pady=5)
        self.entry_elemento.bind("<Return>", lambda e: self.apilar())

        self.btn_apilar = ttk.Button(ops_frame, text="Apilar (Push)", command=self.apilar)
        self.btn_apilar.pack(fill=tk.X, padx=5, pady=5)
        self.btn_desapilar = ttk.Button(ops_frame, text="Desapilar (Pop)", command=self.desapilar)
        self.btn_desapilar.pack(fill=tk.X, padx=5, pady=5)
        self.btn_cima = ttk.Button(ops_frame, text="Ver Cima (Peek)", command=self.ver_cima)
        self.btn_cima.pack(fill=tk.X, padx=5, pady=5)
        self.btn_limpiar = ttk.Button(ops_frame, text="Limpiar Pila", command=self.limpiar_pila_seleccionada)
        self.btn_limpiar.pack(fill=tk.X, padx=5, pady=5)

        # 3. Información
        info_frame = ttk.LabelFrame(self.control_panel, text="Información")
        info_frame.pack(fill=tk.X, pady=10)
        self.info_label = ttk.Label(info_frame, text="Seleccione una pila.", wraplength=260)
        self.info_label.pack(padx=5, pady=5)

    def mostrar_mensaje_status(self, msg, duration=3000):
        self.status_bar.config(text=msg)
        if duration:
            self.master.after(duration, lambda: self.status_bar.config(text=""))

    def obtener_pila_seleccionada(self):
        try:
            indice = self.listbox_pilas.curselection()[0]
            nombre_pila = self.listbox_pilas.get(indice)
            return nombre_pila, self.pilas[nombre_pila]
        except IndexError:
            return None, None

    def crear_pila(self):
        # ... (Sin cambios)
        self.pila_counter += 1
        nombre_pila = f"Pila-{self.pila_counter}"
        self.pilas[nombre_pila] = Pila()
        self.listbox_pilas.insert(tk.END, nombre_pila)
        self.listbox_pilas.selection_clear(0, tk.END)
        self.listbox_pilas.selection_set(tk.END)
        self.actualizar_controles()
        self.dibujar_canvas()
        self.mostrar_mensaje_status(f"Pila '{nombre_pila}' creada.")

    def eliminar_pila(self):
        # ... (Sin cambios)
        nombre_pila, _ = self.obtener_pila_seleccionada()
        if nombre_pila and messagebox.askyesno("Confirmar", f"¿Seguro que quieres eliminar '{nombre_pila}'?"):
            del self.pilas[nombre_pila]
            self.listbox_pilas.delete(tk.ACTIVE)
            self.actualizar_controles()
            self.dibujar_canvas()
            self.mostrar_mensaje_status(f"Pila '{nombre_pila}' eliminada.")
    
    def renombrar_pila(self, event):
        # ... (Sin cambios)
        nombre_pila_viejo, pila = self.obtener_pila_seleccionada()
        if not nombre_pila_viejo: return
        nuevo_nombre = simpledialog.askstring("Renombrar", "Introduce el nuevo nombre:", initialvalue=nombre_pila_viejo)
        if nuevo_nombre and nuevo_nombre != nombre_pila_viejo and nuevo_nombre not in self.pilas:
            indice = self.listbox_pilas.curselection()[0]
            self.pilas[nuevo_nombre] = self.pilas.pop(nombre_pila_viejo)
            self.listbox_pilas.delete(indice)
            self.listbox_pilas.insert(indice, nuevo_nombre)
            self.listbox_pilas.selection_set(indice)
            self.dibujar_canvas()
            self.actualizar_controles()
            self.mostrar_mensaje_status(f"Pila renombrada a '{nuevo_nombre}'.")

    def limpiar_pila_seleccionada(self):
        # ... (Sin cambios)
        nombre_pila, pila = self.obtener_pila_seleccionada()
        if pila and not pila.esta_vacia():
            if messagebox.askyesno("Confirmar", f"¿Vaciar todos los elementos de '{nombre_pila}'?"):
                pila.limpiar()
                self.actualizar_controles()
                self.dibujar_canvas()
                self.mostrar_mensaje_status(f"Pila '{nombre_pila}' vaciada.")
    
    def actualizar_controles(self, event=None):
        # ... (Sin cambios)
        nombre, pila = self.obtener_pila_seleccionada()
        estado_activo = tk.NORMAL if pila else tk.DISABLED
        estado_vacio = tk.DISABLED if not pila or pila.esta_vacia() else tk.NORMAL
        self.btn_apilar.config(state=estado_activo)
        self.btn_desapilar.config(state=estado_vacio)
        self.btn_cima.config(state=estado_vacio)
        self.btn_limpiar.config(state=estado_vacio)
        if pila: self.info_label.config(text=f"Pila: '{nombre}'\nElementos: {len(pila)}")
        else: self.info_label.config(text="Seleccione o cree una pila.")

    # --- Operaciones y Animaciones (MODIFICADAS) ---
    def apilar(self):
        nombre_pila, pila = self.obtener_pila_seleccionada()
        elemento = self.entry_elemento.get()
        if not nombre_pila or not elemento: return

        self.entry_elemento.delete(0, tk.END)
        
        i_pila = list(self.pilas.keys()).index(nombre_pila)
        x_final = (self.canvas.winfo_width() / (len(self.pilas) + 1)) * (i_pila + 1)
        y_final = 50 # <-- CAMBIO: La posición final es siempre la cima (arriba)

        bloque = self.canvas.create_rectangle(x_final-60, 0, x_final+60, 40, fill="#3498db", outline="#2980b9", width=2)
        texto = self.canvas.create_text(x_final, 20, text=elemento, font=("Arial", 10, "bold"), fill="white")
        
        # Primero, la pila existente se anima para "hacer espacio"
        self.animar_desplazamiento(nombre_pila, 40) # Desplazar hacia abajo 40px
        
        def animar_caida(y_actual):
            if y_actual >= y_final:
                self.canvas.delete(bloque); self.canvas.delete(texto)
                pila.apilar(elemento)
                self.dibujar_canvas(); self.actualizar_controles()
                self.mostrar_mensaje_status(f"'{elemento}' apilado en '{nombre_pila}'.")
            else:
                self.canvas.move(bloque, 0, 15); self.canvas.move(texto, 0, 15)
                self.master.after(10, lambda: animar_caida(y_actual + 15))
        
        # La animación de caída empieza después de que se haya hecho espacio
        self.master.after(200, lambda: animar_caida(0))

    def desapilar(self):
        nombre_pila, pila = self.obtener_pila_seleccionada()
        if not pila or pila.esta_vacia(): return
        
        elemento = pila.cima()
        
        i_pila = list(self.pilas.keys()).index(nombre_pila)
        x_inicio = (self.canvas.winfo_width() / (len(self.pilas) + 1)) * (i_pila + 1)
        y_inicio = 50 # <-- CAMBIO: El elemento a desapilar siempre está arriba

        # Quitarlo de la lógica primero para la animación de subida
        pila.desapilar() 

        bloque = self.canvas.create_rectangle(x_inicio-60, y_inicio, x_inicio+60, y_inicio+40, fill="#e74c3c", outline="#c0392b", width=2)
        texto = self.canvas.create_text(x_inicio, y_inicio+20, text=elemento, font=("Arial", 10, "bold"), fill="white")
        
        # Animar el resto de la pila para que "suba" y ocupe el espacio
        self.animar_desplazamiento(nombre_pila, -40) # Desplazar hacia arriba 40px

        def animar_subida(y_actual):
            if y_actual <= -50:
                self.canvas.delete(bloque); self.canvas.delete(texto)
                self.mostrar_mensaje_status(f"'{elemento}' desapilado de '{nombre_pila}'.")
                self.dibujar_canvas(); self.actualizar_controles()
            else:
                self.canvas.move(bloque, 0, -15); self.canvas.move(texto, 0, -15)
                self.master.after(10, lambda: animar_subida(y_actual - 15))

        animar_subida(y_inicio)

    def ver_cima(self):
        nombre_pila, pila = self.obtener_pila_seleccionada()
        if not pila or pila.esta_vacia(): return

        id_rect = f"rect_{nombre_pila}_{len(pila)-1}" # La cima es el último en la lista
        
        def flash(count):
            if count > 0 and self.canvas.find_withtag(id_rect):
                original_color = self.canvas.itemcget(id_rect, "fill")
                color_actual = self.canvas.itemcget(id_rect, "fill")
                nuevo_color = "#f1c40f" if color_actual == original_color else original_color
                self.canvas.itemconfig(id_rect, fill=nuevo_color)
                self.master.after(250, lambda: flash(count-1))
        
        flash(4)
        self.mostrar_mensaje_status(f"La cima de '{nombre_pila}' es '{pila.cima()}'.", 2500)
    
    def animar_desplazamiento(self, nombre_pila, dy):
        """Anima el desplazamiento vertical de todos los elementos de una pila, excepto la cima."""
        pila = self.pilas.get(nombre_pila)
        if not pila or len(pila) < 1: return
        
        # Mueve todos los bloques existentes de la pila afectada
        for j in range(len(pila.items)):
             tag = f"rect_{nombre_pila}_{j}"
             text_tag = f"text_{nombre_pila}_{j}"
             self.canvas.move(tag, 0, dy)
             self.canvas.move(text_tag, 0, dy)
    
    # --- Dibujo Principal en Canvas (MODIFICADO) ---
    def dibujar_canvas(self):
        self.canvas.delete("all")
        if not self.pilas:
            self.canvas.create_text(self.canvas.winfo_width()/2, self.canvas.winfo_height()/2, 
                                    text="Crea una pila para comenzar", font=("Arial", 16, "italic"), fill="grey")
            return
            
        total_pilas, canvas_w = len(self.pilas), self.canvas.winfo_width()
        
        for i, (nombre, pila) in enumerate(self.pilas.items()):
            x_centro = (canvas_w / (total_pilas + 1)) * (i + 1)
            y_inicio = 50 # Punto de partida superior para la cima
            
            self.canvas.create_text(x_centro, 20, text=nombre, font=("Arial", 12, "bold"))
            
            if pila.esta_vacia():
                self.canvas.create_text(x_centro, y_inicio, text="(Vacía)", font=("Arial", 10, "italic"), fill="grey")
                continue

            # Invertimos la lista para dibujar la cima (último elemento) arriba
            elementos_invertidos = reversed(list(enumerate(pila.items)))

            for j_inv, (j, elemento) in enumerate(elementos_invertidos):
                y1 = y_inicio + (j_inv * 40)
                y2 = y1 + 40
                
                rect_tag = f"rect_{nombre}_{j}"
                text_tag = f"text_{nombre}_{j}"
                
                self.canvas.create_rectangle(x_centro-60, y1, x_centro+60, y2, 
                                             fill="#aed6f1", outline="#3498db", width=2, tags=rect_tag)
                self.canvas.create_text(x_centro, y1 + 20, text=elemento, font=("Arial", 10, "bold"), tags=text_tag)
                
                # La cima es el primer elemento que dibujamos en este bucle invertido
                if j_inv == 0:
                     self.canvas.create_text(x_centro + 85, y1 + 20, text="<-- Cima", fill="red", font=("Arial", 10, "bold"))

if __name__ == "__main__":
    root = tk.Tk()
    app = MultiPilaGUI(root)
    root.mainloop()
