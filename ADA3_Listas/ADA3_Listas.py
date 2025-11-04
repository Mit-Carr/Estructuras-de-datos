import tkinter as tk
from tkinter import ttk, messagebox, simpledialog

# ---------------------------
#   ESTRUCTURAS DE DATOS
# ---------------------------

class Postre:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.ingredientes = []

    def agregar_ingrediente(self, ing: str):
        if ing and ing.strip():
            self.ingredientes.append(ing.strip())

    def eliminar_ingrediente(self, ing: str):
        try:
            self.ingredientes.remove(ing)
        except ValueError:
            pass

    def __repr__(self):
        return f"Postre({self.nombre}, {self.ingredientes})"


class Nodo:
    def __init__(self, postre: Postre):
        self.postre = postre
        self.sig = None  # siguiente

    def direccion(self):
        # Dirección simbólica para visualizar (no es memoria real accesible)
        return hex(id(self))


class ListaEnlazada:
    def __init__(self):
        self.cabeza = None
        self._len = 0

    def __len__(self):
        return self._len

    def esta_vacia(self):
        return self.cabeza is None

    def insertar_final(self, postre: Postre):
        nuevo = Nodo(postre)
        if self.esta_vacia():
            self.cabeza = nuevo
        else:
            actual = self.cabeza
            while actual.sig:
                actual = actual.sig
            actual.sig = nuevo
        self._len += 1
        return nuevo

    def buscar_por_indice(self, idx: int) -> Nodo | None:
        if idx < 0 or idx >= self._len:
            return None
        actual = self.cabeza
        i = 0
        while actual and i < idx:
            actual = actual.sig
            i += 1
        return actual

    def eliminar_por_indice(self, idx: int) -> bool:
        if idx < 0 or idx >= self._len:
            return False
        if idx == 0:
            self.cabeza = self.cabeza.sig
            self._len -= 1
            return True
        ant = self.buscar_por_indice(idx - 1)
        if ant and ant.sig:
            ant.sig = ant.sig.sig
            self._len -= 1
            return True
        return False

    def indices_y_nodos(self):
        i = 0
        actual = self.cabeza
        while actual:
            yield i, actual
            i += 1
            actual = actual.sig
    def eliminar_duplicados(self, fusionar_ingredientes=True) -> int:
        """
        Elimina nodos con nombre de postre repetido (case-insensitive).
        Si fusionar_ingredientes=True, mueve ingredientes al primer nodo visto.
        Devuelve la cantidad de nodos eliminados.
        """
        if self.cabeza is None:
            return 0

        # Mapa: nombre_normalizado -> Nodo base (primer aparición)
        mapa = {}
        eliminados = 0

        ant = None
        actual = self.cabeza

        while actual:
            nombre_key = actual.postre.nombre.strip().lower()

            if nombre_key in mapa:
                # Ya vimos un postre con ese nombre -> es duplicado
                if fusionar_ingredientes:
                    base = mapa[nombre_key]
                    # fusionar ingredientes (evitar repetidos simples por texto)
                    for ing in actual.postre.ingredientes:
                        if ing not in base.postre.ingredientes:
                            base.postre.ingredientes.append(ing)

                # quitar el nodo duplicado
                ant.sig = actual.sig
                self._len -= 1
                eliminados += 1
                # avanzar actual sin mover ant (porque ant sigue “pegado” al que queda)
                actual = ant.sig
            else:
                # Primer nodo con ese nombre
                mapa[nombre_key] = actual
                # avanzar ambos punteros
                ant = actual
                actual = actual.sig

        return eliminados





# ---------------------------
#        INTERFAZ UI
# ---------------------------

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Repostería con Lista Enlazada (Tkinter)")
        self.geometry("1000x650")
        self.minsize(980, 600)

        self.lista = ListaEnlazada()

        self._crear_widgets()
        self._layout()
        self._vinculos()
        self._pintar_canvas()

    # ---------- Construcción de UI ----------
    def _crear_widgets(self):
        # Encabezado: nombre de repostería
        self.frame_top = ttk.Frame(self, padding=8)
        self.lbl_rep = ttk.Label(self.frame_top, text="Nombre de la repostería:")
        self.var_rep = tk.StringVar(value="Dulce Enlace")
        self.ent_rep = ttk.Entry(self.frame_top, textvariable=self.var_rep, width=40)
        self.btn_renombrar = ttk.Button(self.frame_top, text="Renombrar", command=self._renombrar)

        # Panel izquierdo: Postres
        self.frame_left = ttk.LabelFrame(self, text="Postres (Nodos)", padding=8)
        self.var_nuevo_postre = tk.StringVar()
        self.ent_postre = ttk.Entry(self.frame_left, textvariable=self.var_nuevo_postre, width=28)
        self.btn_agregar_postre = ttk.Button(self.frame_left, text="Agregar postre", command=self._agregar_postre)
        self.btn_eliminar_postre = ttk.Button(self.frame_left, text="Eliminar postre seleccionado", command=self._eliminar_postre)

        self.lst_postres = tk.Listbox(self.frame_left, height=12, exportselection=False)
        self.scroll_postres = ttk.Scrollbar(self.frame_left, orient="vertical", command=self.lst_postres.yview)
        self.lst_postres.config(yscrollcommand=self.scroll_postres.set)

        # Panel derecho: Ingredientes del postre seleccionado
        self.frame_right = ttk.LabelFrame(self, text="Ingredientes del postre seleccionado", padding=8)
        self.var_nuevo_ingrediente = tk.StringVar()
        self.ent_ingrediente = ttk.Entry(self.frame_right, textvariable=self.var_nuevo_ingrediente, width=28)
        self.btn_agregar_ing = ttk.Button(self.frame_right, text="Agregar ingrediente", command=self._agregar_ingrediente)
        self.btn_eliminar_ing = ttk.Button(self.frame_right, text="Eliminar ingrediente seleccionado", command=self._eliminar_ingrediente)

        self.lst_ingredientes = tk.Listbox(self.frame_right, height=12, exportselection=False)
        self.scroll_ing = ttk.Scrollbar(self.frame_right, orient="vertical", command=self.lst_ingredientes.yview)
        self.lst_ingredientes.config(yscrollcommand=self.scroll_ing.set)

        # Lienzo para visualizar la lista enlazada
        self.frame_canvas = ttk.LabelFrame(self, text="Visualización de la Lista Enlazada", padding=8)
        self.canvas = tk.Canvas(self.frame_canvas, height=220, background="#fafafa", highlightthickness=1, highlightbackground="#ccc")

        self.hscroll = ttk.Scrollbar(self.frame_canvas, orient="horizontal", command=self.canvas.xview)
        self.canvas.config(xscrollcommand=self.hscroll.set)

        # Barra inferior de acciones extra
        self.frame_bottom = ttk.Frame(self, padding=(8, 0, 8, 8))
        self.btn_renombrar_postre = ttk.Button(self.frame_bottom, text="Renombrar postre…", command=self._renombrar_postre)
        self.btn_limpiar_ing = ttk.Button(self.frame_bottom, text="Vaciar ingredientes del postre", command=self._vaciar_ingredientes_postre)
        self.btn_refrescar = ttk.Button(self.frame_bottom, text="Refrescar vista", command=self._refrescar_todo)

        # Estilos
        style = ttk.Style()
        try:
            style.theme_use("clam")
        except:
            pass
        style.configure("TLabelframe", padding=8)
        style.configure("TButton", padding=4)
        self.btn_eliminar_duplicados = ttk.Button(
    self.frame_bottom, text="Eliminar duplicados", command=self._eliminar_duplicados
)


    def _layout(self):
        # Top
        self.frame_top.pack(side="top", fill="x")
        self.lbl_rep.pack(side="left")
        self.ent_rep.pack(side="left", padx=6)
        self.btn_renombrar.pack(side="left")

        # Cuerpo: izquierda/derecha
        self.frame_left.pack(side="left", fill="both", expand=True, padx=(8, 4), pady=8)
        self.frame_right.pack(side="right", fill="both", expand=True, padx=(4, 8), pady=8)

        # Left controls
        row = 0
        ttk.Label(self.frame_left, text="Nuevo postre:").grid(row=row, column=0, sticky="w", pady=(0, 2))
        row += 1
        self.ent_postre.grid(row=row, column=0, sticky="we")
        row += 1
        self.btn_agregar_postre.grid(row=row, column=0, sticky="we", pady=2)
        row += 1
        self.btn_eliminar_postre.grid(row=row, column=0, sticky="we", pady=(2, 8))
        row += 1

        self.frame_left.grid_columnconfigure(0, weight=1)
        self.lst_postres.grid(row=row, column=0, sticky="nsew")
        self.scroll_postres.grid(row=row, column=1, sticky="ns")
        self.frame_left.grid_rowconfigure(row, weight=1)

        # Right controls
        row = 0
        ttk.Label(self.frame_right, text="Nuevo ingrediente:").grid(row=row, column=0, sticky="w", pady=(0, 2))
        row += 1
        self.ent_ingrediente.grid(row=row, column=0, sticky="we")
        row += 1
        self.btn_agregar_ing.grid(row=row, column=0, sticky="we", pady=2)
        row += 1
        self.btn_eliminar_ing.grid(row=row, column=0, sticky="we", pady=(2, 8))
        row += 1

        self.frame_right.grid_columnconfigure(0, weight=1)
        self.lst_ingredientes.grid(row=row, column=0, sticky="nsew")
        self.scroll_ing.grid(row=row, column=1, sticky="ns")
        self.frame_right.grid_rowconfigure(row, weight=1)

        # Canvas
        self.frame_canvas.pack(side="bottom", fill="x", padx=8, pady=(0, 8))
        self.canvas.pack(side="top", fill="x")
        self.hscroll.pack(side="top", fill="x")

        # Bottom actions
        self.frame_bottom.pack(side="bottom", fill="x")
        self.btn_renombrar_postre.pack(side="left", padx=4)
        self.btn_limpiar_ing.pack(side="left", padx=4)
        self.btn_refrescar.pack(side="left", padx=4)

    def _vinculos(self):
        self.lst_postres.bind("<<ListboxSelect>>", self._al_seleccionar_postre)
        self.lst_ingredientes.bind("<Delete>", lambda e: self._eliminar_ingrediente())
        self.ent_ingrediente.bind("<Return>", lambda e: self._agregar_ingrediente())
        self.ent_postre.bind("<Return>", lambda e: self._agregar_postre())
        self.btn_eliminar_duplicados.pack(side="left", padx=4)

    def _eliminar_duplicados(self):
        eliminados = self.lista.eliminar_duplicados(fusionar_ingredientes=True)
        # Tras modificar la estructura, refrescamos TODO y limpiamos selección para evitar índices colgados
        self.lst_postres.selection_clear(0, tk.END)
        self.lst_ingredientes.selection_clear(0, tk.END)
        self._refrescar_todo()

        if eliminados == 0:
            messagebox.showinfo("Duplicados", "No se encontraron postres duplicados.")
        else:
            messagebox.showinfo("Duplicados", f"Se eliminaron {eliminados} postre(s) duplicado(s).")


    # ---------- Lógica de UI ----------
    def _renombrar(self):
        nuevo = self.var_rep.get().strip()
        if not nuevo:
            messagebox.showwarning("Aviso", "El nombre de la repostería no puede estar vacío.")
            return
        self.title(f"{nuevo} — Repostería con Lista Enlazada")
        messagebox.showinfo("Listo", f"Repostería renombrada a: {nuevo}")

    def _agregar_postre(self):
        nombre = self.var_nuevo_postre.get().strip()
        if not nombre:
            messagebox.showwarning("Aviso", "Escribe el nombre del postre.")
            return
        self.lista.insertar_final(Postre(nombre))
        self.var_nuevo_postre.set("")
        self._refrescar_postres()
        self._pintar_canvas()

    def _eliminar_postre(self):
        idx = self._postre_seleccionado_index()
        if idx is None:
            messagebox.showwarning("Aviso", "Selecciona un postre de la lista.")
            return
        nombre = self.lst_postres.get(idx)
        if messagebox.askyesno("Eliminar postre", f"¿Eliminar '{nombre}' y todos sus ingredientes?"):
            self.lista.eliminar_por_indice(idx)
            self._refrescar_postres()
            self._refrescar_ingredientes(None)
            self._pintar_canvas()

    def _renombrar_postre(self):
        idx = self._postre_seleccionado_index()
        if idx is None:
            messagebox.showwarning("Aviso", "Selecciona un postre para renombrar.")
            return
        nodo = self.lista.buscar_por_indice(idx)
        nuevo = simpledialog.askstring("Renombrar postre", f"Nuevo nombre para '{nodo.postre.nombre}':", parent=self)
        if nuevo and nuevo.strip():
            nodo.postre.nombre = nuevo.strip()
            self._refrescar_postres()
            self._pintar_canvas()

    def _agregar_ingrediente(self):
        idx = self._postre_seleccionado_index()
        if idx is None:
            messagebox.showwarning("Aviso", "Selecciona un postre para agregar ingredientes.")
            return
        ing = self.var_nuevo_ingrediente.get().strip()
        if not ing:
            messagebox.showwarning("Aviso", "Escribe un ingrediente.")
            return
        nodo = self.lista.buscar_por_indice(idx)
        nodo.postre.agregar_ingrediente(ing)
        self.var_nuevo_ingrediente.set("")
        self._refrescar_ingredientes(nodo)

    def _eliminar_ingrediente(self):
        idx_postre = self._postre_seleccionado_index()
        if idx_postre is None:
            messagebox.showwarning("Aviso", "Selecciona un postre primero.")
            return
        idx_ing = self._ingrediente_seleccionado_index()
        if idx_ing is None:
            messagebox.showwarning("Aviso", "Selecciona un ingrediente a eliminar.")
            return
        nodo = self.lista.buscar_por_indice(idx_postre)
        ing = self.lst_ingredientes.get(idx_ing)
        nodo.postre.eliminar_ingrediente(ing)
        self._refrescar_ingredientes(nodo)

    def _vaciar_ingredientes_postre(self):
        idx = self._postre_seleccionado_index()
        if idx is None:
            messagebox.showwarning("Aviso", "Selecciona un postre.")
            return
        nodo = self.lista.buscar_por_indice(idx)
        if messagebox.askyesno("Vaciar ingredientes", f"¿Quitar todos los ingredientes de '{nodo.postre.nombre}'?"):
            nodo.postre.ingredientes.clear()
            self._refrescar_ingredientes(nodo)

    def _al_seleccionar_postre(self, _event=None):
        idx = self._postre_seleccionado_index()
        nodo = self.lista.buscar_por_indice(idx) if idx is not None else None
        self._refrescar_ingredientes(nodo)

    def _postre_seleccionado_index(self):
        sel = self.lst_postres.curselection()
        return sel[0] if sel else None

    def _ingrediente_seleccionado_index(self):
        sel = self.lst_ingredientes.curselection()
        return sel[0] if sel else None

    def _refrescar_postres(self):
        self.lst_postres.delete(0, tk.END)
        for _i, nodo in self.lista.indices_y_nodos():
            self.lst_postres.insert(tk.END, nodo.postre.nombre)

    def _refrescar_ingredientes(self, nodo: Nodo | None):
        self.lst_ingredientes.delete(0, tk.END)
        if nodo is None:
            return
        for ing in nodo.postre.ingredientes:
            self.lst_ingredientes.insert(tk.END, ing)

    def _refrescar_todo(self):
        self._refrescar_postres()
        idx = self._postre_seleccionado_index()
        self._refrescar_ingredientes(self.lista.buscar_por_indice(idx) if idx is not None else None)
        self._pintar_canvas()

    # ---------- Dibujo del Canvas ----------
    def _pintar_canvas(self):
        self.canvas.delete("all")

        margen_x = 30
        margen_y = 20
        ancho_nodo = 160
        alto_nodo = 70
        espacio = 40

        x = margen_x
        y = margen_y

        # Título con nombre de repostería
        titulo = self.var_rep.get().strip() or "Repostería"
        self.canvas.create_text(10, 8, anchor="w", text=f"Repostería: {titulo}", font=("Segoe UI", 10, "bold"))

        for i, nodo in self.lista.indices_y_nodos():
            # Caja del nodo
            x1, y1 = x, y
            x2, y2 = x + ancho_nodo, y + alto_nodo
            self.canvas.create_rectangle(x1, y1, x2, y2, fill="#ffffff", outline="#444", width=2)
            # Nombre del postre
            self.canvas.create_text((x1 + x2) / 2, y1 + 18, text=f"{i}. {nodo.postre.nombre}", font=("Segoe UI", 10, "bold"))
            # Texto de ingredientes (resumen)
            resumen = ", ".join(nodo.postre.ingredientes[:2])
            if len(nodo.postre.ingredientes) > 2:
                resumen += f" … (+{len(nodo.postre.ingredientes)-2})"
            self.canvas.create_text((x1 + x2) / 2, y1 + 40, text=resumen if resumen else "(sin ingredientes)", font=("Segoe UI", 9), fill="#555")

            # Dirección simbólica
            self.canvas.create_text((x1 + x2) / 2, y2 + 14, text=f"dir: {nodo.direccion()}", font=("Consolas", 8), fill="#777")

            # Flecha al siguiente
            if nodo.sig:
                x_mid_right = x2
                y_mid = (y1 + y2) / 2
                x_next = x2 + espacio
                self.canvas.create_line(x_mid_right, y_mid, x_next, y_mid, arrow=tk.LAST, width=2)
            x += ancho_nodo + espacio

        # Ajustar scroll horizontal si hay muchos nodos
        total_width = x + margen_x
        self.canvas.config(scrollregion=(0, 0, total_width, 240))
        if total_width > self.canvas.winfo_width():
            # nada especial; el scrollbar ya aparece
            pass


if __name__ == "__main__":
    app = App()
    app.mainloop()
