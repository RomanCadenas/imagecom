import os
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from PIL import Image

class ImageProcessorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Optimizador y Redimensionador de Imágenes")
        self.root.geometry("520x460")
        self.root.resizable(False, False)
        
        self.input_dir = tk.StringVar()
        self.output_dir = tk.StringVar()
        self.scale_var = tk.StringVar(value="80")     # 80% del tamaño original
        self.quality_var = tk.StringVar(value="85")   # Calidad JPEG (1-100)
        
        self.create_widgets()

    def create_widgets(self):
        title_label = tk.Label(self.root, text="Compresor y Redimensionador Masivo", font=("Arial", 14, "bold"))
        title_label.pack(pady=15)

        dir_frame = tk.LabelFrame(self.root, text=" Directorios ", font=("Arial", 10, "bold"), padx=10, pady=10)
        dir_frame.pack(fill="x", padx=20, pady=5)

        tk.Label(dir_frame, text="Carpeta de Origen:").grid(row=0, column=0, sticky="w", pady=5)
        tk.Entry(dir_frame, textvariable=self.input_dir, width=35).grid(row=0, column=1, padx=5, pady=5)
        tk.Button(dir_frame, text="Examinar...", command=self.select_input).grid(row=0, column=2, pady=5)

        tk.Label(dir_frame, text="Carpeta de Destino:").grid(row=1, column=0, sticky="w", pady=5)
        tk.Entry(dir_frame, textvariable=self.output_dir, width=35).grid(row=1, column=1, padx=5, pady=5)
        tk.Button(dir_frame, text="Examinar...", command=self.select_output).grid(row=1, column=2, pady=5)

        param_frame = tk.LabelFrame(self.root, text=" Parámetros de Calidad y Tamaño ", font=("Arial", 10, "bold"), padx=10, pady=10)
        param_frame.pack(fill="x", padx=20, pady=10)

        tk.Label(param_frame, text="Escala de tamaño (%):").grid(row=0, column=0, sticky="w", pady=5)
        tk.Entry(param_frame, textvariable=self.scale_var, width=10).grid(row=0, column=1, sticky="w", padx=5, pady=5)
        tk.Label(param_frame, text="(Ej. 80 reduce al 80% de su dimensión)", fg="gray", font=("Arial", 8)).grid(row=0, column=2, sticky="w")

        tk.Label(param_frame, text="Calidad de Compresión (1-100):").grid(row=1, column=0, sticky="w", pady=5)
        tk.Entry(param_frame, textvariable=self.quality_var, width=10).grid(row=1, column=1, sticky="w", padx=5, pady=5)
        tk.Label(param_frame, text="(Recomendado: 80 - 90)", fg="gray", font=("Arial", 8)).grid(row=1, column=2, sticky="w")

        process_btn = tk.Button(self.root, text="Procesar Imágenes", bg="#4CAF50", fg="white", font=("Arial", 11, "bold"), padx=10, pady=5, command=self.process_images)
        process_btn.pack(pady=15)

    def select_input(self):
        folder = filedialog.askdirectory()
        if folder:
            self.input_dir.set(folder)

    def select_output(self):
        folder = filedialog.askdirectory()
        if folder:
            self.output_dir.set(folder)

    def process_images(self):
        in_dir = self.input_dir.get()
        out_dir = self.output_dir.get()

        if not in_dir or not out_dir:
            messagebox.showerror("Error", "Por favor selecciona ambas carpetas.")
            return

        if not os.path.exists(out_dir):
            os.makedirs(out_dir)

        try:
            scale_factor = float(self.scale_var.get()) / 100.0
            quality_val = int(self.quality_var.get())
        except ValueError:
            messagebox.showerror("Error", "Los valores de escala y calidad deben ser numéricos.")
            return

        valid_extensions = (".jpg", ".jpeg", ".png", ".bmp", ".webp")
        processed_count = 0

        try:
            for filename in os.listdir(in_dir):
                if filename.lower().endswith(valid_extensions):
                    img_path = os.path.join(in_dir, filename)
                    
                    with Image.open(img_path) as img:
                        new_width = int(img.width * scale_factor)
                        new_height = int(img.height * scale_factor)
                        
                        img_resized = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
                        output_path = os.path.join(out_dir, filename)
                        
                        if img.format == "PNG":
                            img_resized.save(output_path, "PNG", optimize=True)
                        else:
                            if img_resized.mode in ("RGBA", "P"):
                                img_resized = img_resized.convert("RGB")
                            img_resized.save(output_path, "JPEG", quality=quality_val, optimize=True)
                            
                        processed_count += 1

            messagebox.showinfo("Proceso Completado", f"Se procesaron con éxito {processed_count} imágenes.")
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error:\n{str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageProcessorApp(root)
    root.mainloop()