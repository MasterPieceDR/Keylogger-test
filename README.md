Keylogger — Actividad Educativa

Advertencia importante — lectura obligatoria
Este repositorio contiene material con fines exclusivamente educativos para comprender cómo funcionan técnicamente los programas que registran eventos del teclado y los riesgos que representan. No utilices, redistribuyas ni modifiques este código para fines maliciosos o sin el consentimiento explícito y por escrito de todas las personas afectadas. El autor y colaboradores no se responsabilizan por un uso indebido.

Objetivo

Implementar en un entorno controlado un programa que registre pulsaciones (keylogger) para fines pedagógicos: entender cómo se capturan eventos de teclado, cómo se registran y cómo se mitigan/gestionan estos riesgos en ciberseguridad defensiva.

Estructura del repositorio
Keylogger-test/
│
├── main.py            # Código principal (registro de teclas)
├── requirements.txt   # Dependencias (pip)
├── README.md          # Este archivo
├── .gitignore         # Archivos ignorados por git
└── log.txt            # (Generado en ejecución; NO subir al repo)


IMPORTANTE: El archivo log.txt contiene datos sensibles y no debe subirse a GitHub. Está incluido en .gitignore.

Requisitos

Python 3.10+ (recomendado).

Sistema operativo: Windows (recomendado para keyboard) o Linux real / VM.

No se recomienda WSL para keyboard (no funciona correctamente en WSL).

Permisos: en Linux, el paquete keyboard puede requerir ejecución como root o acceso a /dev/input/*.

Paquetes Python: listados en requirements.txt.

Contenido sugerido de requirements.txt
keyboard


(Usa pip install -r requirements.txt para instalar.)

Instalación (Windows — PowerShell)

Abrir PowerShell (no WSL) y ejecutar los comandos:

# 1. Clona el repositorio (si aún no lo hiciste)
git clone https://github.com/USUARIO/REPO.git
cd REPO

# 2. Crea y activa un entorno virtual
python -m venv venv
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
.\venv\Scripts\Activate.ps1

# 3. Actualiza pip e instala dependencias
python -m pip install --upgrade pip
pip install -r requirements.txt

Nota sobre WSL y Linux

WSL: La librería keyboard no funciona correctamente en WSL porque WSL no expone los dispositivos físicos del teclado. No intentes ejecutar el keylogger con keyboard dentro de WSL.

Linux nativo / VM: Si usas Linux real (o una VM con acceso a dispositivos), probablemente necesites ejecutar el script como sudo para que keyboard pueda abrir los dispositivos (/dev/input/*). Hazlo solo en máquinas de pruebas y con consentimiento.

Ejecución (ejemplos)
Ejecutar el script real (solo en entorno controlado, Windows o VM Linux)

Con el entorno virtual activo:

python main.py


Durante la ejecución:

El script mostrará en consola las teclas detectadas (según la implementación).

Generará/actualizará log.txt con timestamp de cada pulsación.

Para detener: Ctrl + C — el programa puede escribir un resumen antes de cerrar.

Ejecutar en modo simulado (seguro para WSL / demostraciones)

Si no quieres/puedes usar keyboard, modifica temporalmente main.py (o usa el flag --simulate si tu script lo soporta) para generar eventos sintéticos. Ejemplo conceptual:

# (Código de ejemplo — no captura teclado real)
for k in ['a','b','c','1','2',' ']:
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Tecla: {repr(k)}")
    time.sleep(0.3)


Este modo permite validar formato de logs y salidas sin interceptar entradas reales.

Manejo seguro del log

No subas log.txt a repositorios públicos. Añádelo a .gitignore.

Después de las pruebas, borra log.txt inmediatamente si contiene datos sensibles.

Mantén un registro (audit trail) de las pruebas: quién autorizó, cuándo se ejecutó y por cuánto tiempo.

Ejemplo de salida
[2025-10-17 21:30:50] Tecla: a
[2025-10-17 21:30:51] Tecla: [ESPACIO]
[2025-10-17 21:30:52] Tecla: 1

Ética y legalidad

Realiza las pruebas solo en tus dispositivos o en máquinas específicamente provisionadas para laboratorio.

Obtén consentimiento por escrito si pruebas con terceras personas.

Revisa la legislación local y las políticas de tu institución. En muchos países, el registro de teclas sin autorización es delito.

Buenas prácticas (educativas)

Ejecuta el experimento en una VM con snapshot (para poder restaurar el estado).

Limita la duración de la prueba y monitorea el sistema.

Documenta: objetivo, metodología, resultados, riesgos y medidas de mitigación.

Contribuciones

Contribuciones enfocadas en aspectos defensivos, documentación, simuladores o detección son bienvenidas. Abre un issue o un pull request con claridad sobre el propósito educativo y las salvaguardas.

 Autor

Diego Ruiz — Proyecto educativo / UIDE