<div align="center">

# 🎮 Aery: Tetris + Novela Visual

### Una asistente virtual olvidada desde 2007 te pide que no cierres el programa

<br>

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pygame](https://img.shields.io/badge/Pygame--CE-2E7D32?style=for-the-badge&logo=python&logoColor=white)
![Género](https://img.shields.io/badge/Género-Terror_psicológico-8B0000?style=for-the-badge)
![Status](https://img.shields.io/badge/Proyecto-Universitario-blueviolet?style=for-the-badge)

<br>

<img src="capturas/imagen_2026-11-24_213331374.png" alt="Aery" width="80%">

</div>

---

## 📖 Historia

Abres un programa antiguo y una voz te saluda: **Aery**, tu asistente virtual del año 2007, que lleva más de quince años apagada. Intenta ser útil (cantar, mostrar el clima, revisar tu correo), pero todos sus módulos fallan.

Para compensarlo te propone jugar **Tetris**. Pero mientras juegas, el sistema empieza a mostrar errores y Aery se vuelve cada vez más extraña...

> *"Por favor... no cierres el programa."*

## 📸 Capturas

<div align="center">

### 💬 Novela visual
<img src="capturas/imagen_2026-11-24_213331374.png" alt="Novela visual" width="80%">

<br><br>

### 🧱 Partida de Tetris
<img src="capturas/imagen_2026-11-24_213508310.png" alt="Partida de Tetris" width="80%">

<br><br>

### 👾 Escenas y mensajes del sistema
<img src="capturas/imagen_2026-11-24_213518409.png" alt="Escenas" width="80%">

</div>

---

## ✨ Características

| | Característica |
|:---:|:---|
| 📖 | Novela visual en **2 actos** con efecto de texto escribiéndose |
| 🎭 | Aery con **11 expresiones** distintas (feliz, nerviosa, enojada, seria...) |
| 🖥️ | Mensajes de sistema estilo **consola CRT** verde con parpadeo |
| 🌫️ | Cambio de escenario a los *backrooms* durante la historia |
| 🧱 | **2 fases de Tetris** integradas en la narrativa |

## 🔄 Flujo del juego

```mermaid
flowchart LR
    A[📖 Acto 1] --> B[🧱 Tetris 1]
    B --> C[📖 Acto 2]
    C --> D[🧱 Tetris 2]
```

## 🛠️ Tecnologías

- **Python 3.12+**
- **Pygame / Pygame-CE**: gráficos, eventos y fuentes
- **Subprocess**: cada fase de Tetris corre como proceso independiente, orquestado desde `main.py`

## 🚀 Cómo ejecutarlo

```bash
# 1. Clonar el repositorio
git clone https://github.com/AreR9/tetris-novela.git
cd tetris-novela

# 2. Instalar dependencias
py -m pip install -r requirements.txt

# 3. Jugar
py main.py
```

> 💡 Ejecuta siempre `main.py` desde la carpeta del proyecto.

## 🎯 Controles

### Novela

| Tecla | Acción |
|:---:|:---|
| `Espacio` / `Enter` | Avanzar el diálogo (o completar el texto en pantalla) |
| `X` | Saltar directo al Tetris 1 |

### Tetris

| Tecla | Acción |
|:---:|:---|
| ⬅️ ➡️ | Mover pieza |
| ⬆️ | Rotar |
| ⬇️ | Bajar más rápido |

> ⚠️ Ajusta la tabla de Tetris a tus controles reales.

## 📁 Estructura

```
tetris-novela/
├── 📂 assets/           → sprites de Aery, bloques y fondos
├── 📂 capturas/         → imágenes del README
├── 📄 main.py           → punto de entrada y orquestador
├── 📄 novela.py         → motor de diálogos y guion de los actos
├── 📄 tetris1.py        → primera fase de Tetris
├── 📄 tetris2.py        → segunda fase de Tetris
├── 📄 requirements.txt
└── 📄 README.md
```

---
