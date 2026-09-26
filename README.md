# Optimizador y Redimensionador Masivo de Imágenes

Aplicación de escritorio desarrollada en Python con interfaz gráfica (`Tkinter`) y `Pillow` para procesar, redimensionar y comprimir imágenes de forma masiva en lote.

---

## 📌 Requisitos del Proyecto

### 1. Requisitos del Sistema
- **Sistema Operativo:** Windows, macOS o Linux.
- **Python:** Versión **3.7** o superior.

### 2. Dependencias de Software
El proyecto hace uso de las siguientes librerías de Python:

- **`tkinter`**: Interfaz gráfica de usuario (UI). *(Viene integrada por defecto con la mayoría de las instalaciones de Python en Windows/macOS. En Linux se puede instalar mediante `sudo apt-get install python3-tk`)*.
- **`Pillow` (PIL)**: Librería para la manipulación y procesamiento de imágenes (`pip install Pillow`).

---

## 🚀 Instalación y Configuración

1. **Clonar o descargar el repositorio** en tu equipo local.

2. **Crear y activar un entorno virtual (Opcional pero recomendado):**
   - En **Windows (PowerShell)**:
     ```powershell
     python -m venv venv
     .\venv\Scripts\Activate.ps1
     ```
   - En **Linux / macOS**:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

3. **Instalar dependencias:**
   ```bash
   pip install Pillow
   ```
   *(o `pip install -r requirements.txt` si existe el archivo)*.

---

## 💻 Uso de la Aplicación

1. Ejecuta la aplicación iniciando `app.py`:
   ```bash
   python app.py
   ```

2. **Interfaz de usuario:**
   - **Carpeta de Origen:** Selecciona la carpeta que contiene las imágenes que deseas procesar.
   - **Carpeta de Destino:** Selecciona la carpeta donde se guardarán las imágenes optimizadas.
   - **Escala de tamaño (%):** Porcentaje para escalar las dimensiones (por ejemplo, `80` escala las imágenes al 80% de su tamaño original).
   - **Calidad de Compresión (1-100):** Nivel de calidad JPEG deseado (Recomendado: 80 - 90).
   - Haz clic en **Procesar Imágenes**.

---

## 📂 Formatos de Imagen Soportados

- `.jpg` / `.jpeg`
- `.png` (con optimización de compresión)
- `.bmp`
- `.webp`

---

## 🛠️ Estructura del Proyecto

```text
imagecom/
├── app.py              # Código principal de la aplicación con la interfaz Tkinter
├── requirements.txt    # Lista de dependencias del proyecto
└── README.md           # Documentación y requisitos del proyecto
```
