class FilaDeImpresion:
    def __init__(self):
        """
        Constructor: Se ejecuta al crear una nueva fila.
        Inicializa una lista vacía para guardar los documentos.
        """
        self.documentos = []
        print("🖨️  Impresora lista para recibir trabajos.\n")

    def esta_vacia(self):
        """
        Método: Verifica si la cola está vacía.
        Devuelve True si no hay documentos, False en caso contrario.
        """
        return len(self.documentos) == 0

    def agregar(self, documento):
        """
        Método (Encolar): Agrega un documento al final de la cola.
        """
        self.documentos.append(documento)
        print(f"📥 Recibido '{documento}'.")
        self.ver_fila()

    def imprimir_siguiente(self):
        """
        Método (Desencolar): Imprime (elimina) el primer documento de la cola.
        """
        if self.esta_vacia():
            print("✅ No hay documentos en espera.\n")
        else:
            # .pop(0) elimina el elemento en el índice 0 (el primero).
            documento_impreso = self.documentos.pop(0)
            print(f"📤 Imprimiendo '{documento_impreso}'...")
            self.ver_fila()

    def ver_fila(self):
        """Método auxiliar para mostrar el estado actual de la cola."""
        if self.esta_vacia():
            print("   (La fila está vacía)\n")
        else:
            print(f"   Fila actual: {self.documentos}\n")



impresora = FilaDeImpresion()

# Se envían documentos a la impresora
impresora.agregar("Informe_Ventas.docx")
impresora.agregar("Foto_Vacaciones.jpg")
impresora.agregar("Contrato_Final.pdf")


impresora.imprimir_siguiente()
impresora.imprimir_siguiente()

impresora.agregar("Presentacion_Reunion.pptx")


impresora.imprimir_siguiente()
impresora.imprimir_siguiente()
impresora.imprimir_siguiente() 
