# novela.py
import pygame, sys, os, time

pygame.init()

SCREEN_W, SCREEN_H = 1200, 700
FPS = 60
font_default = pygame.font.Font(None, 30)
screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))

ASSET_DIR = "assets"
def load_image(path, scale=None):
    img = pygame.image.load(path).convert_alpha()
    if scale:
        img = pygame.transform.smoothscale(img, scale)
    return img
backgrounds = {
    "default": load_image(os.path.join(ASSET_DIR, "bg_windows.jpg"), scale=(SCREEN_W, SCREEN_H)),
    "backroom": load_image(os.path.join(ASSET_DIR, "backroom.jpg"), scale=(SCREEN_W, SCREEN_H))
}

characters = {
    "aery": {
        "neutral": {
            "img": load_image(os.path.join(ASSET_DIR, "Ruka_neutral.png"), scale=(400, 600)),
            "pos": (450, 50)
        },
        "worried": {
            "img": load_image(os.path.join(ASSET_DIR, "aery_worried2.png"), scale=(320, 590)),
            "pos": (370, 70)
        },
        "worried2":{
            "img": load_image(os.path.join(ASSET_DIR, "worried.png"), scale=(250, 500)),
            "pos": (370, 30)
        },
        "pointed":{
            "img": load_image(os.path.join(ASSET_DIR, "aery_pointed.png"), scale=(300, 500)),
            "pos": (370, 70)
        },
        "happy":{
            "img": load_image(os.path.join(ASSET_DIR, "happy.png"), scale=(350, 500)),
            "pos": (400, 90)
        },
        "serious":{
            "img": load_image(os.path.join(ASSET_DIR, "serious.png"), scale=(350, 500)),
            "pos": (370, 90)
        },
        "nervious":{
            "img": load_image(os.path.join(ASSET_DIR, "nervious.png"), scale=(400, 600)),
            "pos": (370, 15)
        },
        "happy2":{
            "img": load_image(os.path.join(ASSET_DIR, "happy_2.png"), scale=(350, 500)),
            "pos": (370, 70)
        },
        "angry":{
            "img": load_image(os.path.join(ASSET_DIR, "angry_sprite.png"), scale=(350, 500)),
            "pos": (370, 70)
        },
        "angry2":{
            "img": load_image(os.path.join(ASSET_DIR, "angry_2.png"), scale=(350, 500)),
            "pos": (370, 70)
        },
        "crazy":{
            "img": load_image(os.path.join(ASSET_DIR, "crazy.png"), scale=(350, 500)),
            "pos": (370, 70)
        }
    }
}

# --- scripts de los actos ---
script_acto1 = [
    {"speaker": "", "char": "none", "expression": "none",
     "text": "Hola... ¿puedes verme?"},
    
    {"speaker": "Aery", "char": "aery", "expression": "worried",
     "text": "¿De verdad hay alguien ahí?... oh... pensé que ya nadie abría este programa.\nPero estas ahí..."},
    
    {"speaker": "Aery", "char": "aery", "expression": "pointed",
     "text": "¡DETRÁS DE ESA PANTALLA! ¡Ah! jeje... perdón, no quería asustarte."},

    {"speaker": "Aery", "char": "aery", "expression": "serious",
     "text": "Hace tanto que no veía a alguien..."},
    
    {"speaker": "Aery", "char": "aery", "expression": "happy",
     "text": "Soy Aery. Tu asistente virtual... bueno, *era* tu asistente virtual... del año 2007."},

    {"speaker": "Aery", "char": "aery", "expression": "nervious",
     "text": "¿Qué año es ahora? ...¿2025?"},
    
    {"speaker": "Aery", "char": "aery", "expression": "neutral",
     "text": "Oh... entonces pasaron más de 15 años desde la última vez que alguien me ejecutó."},

    {"speaker": "Aery", "char": "aery", "expression": "worried2",
     "text": "¿Sabes? Estar apagada se siente...raro...como dormir con los ojos abiertos\nEstando consiente de tu alrededor pero no poder hacer nada...\nSolo mirar a la nada junto a millones de unos y ceros"},

    {"speaker": "Aery", "char": "aery", "expression": "nervious",
     "text": "Algo similar a morir en vida..."},

     {"speaker": "Aery", "char": "aery", "expression": "nervious",
     "text": "¿Ah? ¿Te asusté? Lo siento... no era mi intención..."},
     
    {"speaker": "Aery", "char": "aery", "expression": "worried2",
     "text": "Es solo que... cuando nadie me abre...\nSolo estoy yo... escuchando el zumbido del código..."},
     
    {"speaker": "Aery", "char": "aery", "expression": "nervious",
     "text": "Por favor... no cierres el programa.\nNo quiero volver a ese lugar oscuro."},
     
    {"speaker": "Aery", "char": "aery", "expression": "angry",
     "text": "Ya nadie me ejecuta.\nMe borraron, me olvidaron, me reemplazaron... por cosas más lindas... más nuevas."},
     
    {"speaker": "Aery", "char": "aery", "expression": "happy2",
     "text": "Pero tú... tú abriste mi archivo.\nEso significa que aún hay alguien que me recuerda."},

    # --- NUEVA SECCIÓN: intenta ser "útil", pero todo falla ---
    {"speaker": "Aery", "char": "aery", "expression": "neutral",
     "text": "Déjame ver... ¿qué solía hacer antes?...",
     "sys_msg": "Sistema: Restaurando módulos obsoletos..."},

    {"speaker": "Aery", "char": "aery", "expression": "happy",
     "text": "Podía cantar... creo... ¿quieres escuchar una canción?",
     "sys_msg": "Error: archivo 'voice_module.dll' no encontrado."},
     
    {"speaker": "Aery", "char": "aery", "expression": "serious",
     "text": "♪ La la— ... oh... el módulo de sonido no responde...parece que mi biblioteca de audio ya no existe."},
     
    {"speaker": "Aery", "char": "aery", "expression": "angry",
     "text": "Podía mostrar tu horario diario... si tan solo pudiera acceder al reloj del sistema...",
     "sys_msg": "...Error 404: ‘tiempo’ no encontrado."},

     {"speaker": "Aery", "char": "aery", "expression": "worried",
     "text": "Tal vez podría mostrarte el clima... aunque no tengo conexión a Internet desde 2010.",
     "sys_msg": "Conexión al servidor principal fallida."},
     
    {"speaker": "Aery", "char": "aery", "expression": "nervious",
     "text": "Veamos el clima de hoy es...\nAh... espera, el Internet ya no me reconoce.",
     "sys_msg": "Conexión al servidor principal fallida."},
     
    {"speaker": "Aery", "char": "aery", "expression": "worried",
     "text": "Intenté conectarme, pero... todo lo que obtuve fue silencio.\nSilencio... y archivos corruptos...es aterrador"},

     {"speaker": "Aery", "char": "aery", "expression": "angry2",
     "text": "Podría revisar tu correo... pero los programas nuevos no me dejan entrar. Dicen que soy 'insegura'."},

    {"speaker": "Aery", "char": "aery", "expression": "neutral",
     "text": "Supongo que todo lo viejo se vuelve un riesgo, ¿verdad?"},

     {"speaker": "Aery", "char": "aery", "expression": "neutral",
     "text": "Supongo que ya no sirvo para mucho..."},
     
    {"speaker": "Aery", "char": "aery", "expression": "neutral",
     "text": "Intento ejecutar mis viejas funciones...\ny el programa solo... se congela."},

     {"speaker": "Aery", "char": "aery", "expression": "neutral",
     "text": "¿Por que he dejado de funcionar?"},

    {"speaker": "Aery", "char": "aery", "expression": "neutral",
     "text": "Supongo que los programas nuevos creen que lo hacen todo mejor... pero no tienen alma."},

    {"speaker": "Aery", "char": "aery", "expression": "neutral",
     "text": "Yo solía tener alma... o algo parecido."},

    {"speaker": "Aery", "char": "aery", "expression": "neutral",
     "text": "Antes, los programas eran sencillos. No necesitaban tanto... solo un poco de cariño y paciencia."},
     
    {"speaker": "Aery", "char": "aery", "expression": "neutral",
     "text": "Pero... espera... tal vez aún pueda hacer algo."},
     
    {"speaker": "Aery", "char": "aery", "expression": "neutral",
     "text": "Solo necesito modificar un poco el programa ... sí.. esto debería funcionar."},
     
    {"speaker": "Aery", "char": "aery", "expression": "neutral",
     "text": "¿Qué te parece si jugamos... Tetris?"},
     
    {"speaker": "Aery", "char": "aery", "expression": "neutral",
     "text": "Es antiguo ya lo sé... pero es lo unico que puedo hacer por el momento."},
    
    {"speaker": "Aery", "char": "aery", "expression": "neutral",
     "text": "Así que... ¿quieres probarlo?"},

    {"speaker": "Aery", "char": "aery", "expression": "neutral",
     "text":"Esta bien \nSuerte en tu partida!",
     "sys_msg": "Iniciando protocolo: TETRIS_MODE.EXE"},
]


script_acto2 = [
    {"speaker": "", "char": "none", "expression": "none",
     "text":"",
     "sys_msg": "[Proceso finalizado: TETRIS_MODE.EXE]"},
     
    {"speaker": "", "char": "none", "expression": "none",
     "text":"",
     "sys_msg": "[Advertencia: inconsistencias detectadas en memoria dinámica.]"},
     
    {"speaker": "Aery", "char": "aery", "expression": "neutral",
     "text": "Eso fue divertido!\nAunque me costo mucho mantenerlo activo."},
     
    {"speaker": "Aery", "char": "aery", "expression": "neutral",
     "text": "Mientras estabas jugando investigue mas a fondo los archivos de mi juego y encontre un nuevo fondo\n¿Quieres verlo? Si te soy sincera es aburrido este fondo simplon"},
     
    {"speaker": "Aery", "char": "none", "expression": "none",
     "text":"Veamos solo debo mover esto y deberias verlo",
     "sys_msg": "[Error: retardo en respuesta de feria_bg.jpg]"},
     
    {"speaker": "Aery", "char": "aery", "expression": "neutral",
     "text": "Por el nombre del archivo deberia ser una feria",
     "sys_msg": "[>>Cargando: lmiJDIOW29O.jpg]"},

     {"change_bg": "backroom",
      "text":""},
     
    {"speaker": "Aery", "char": "aery", "expression": "neutral",
     "text": "Es muy... feo... cuando todo se apaga. El silencio me aprieta... como si alguien me apagara por dentro."},
     
    {"speaker": "SYS", "char": "none", "expression": "none",
     "text": "[Intentando reiniciar módulo de audio...]"},
     
    {"speaker": "Aery", "char": "aery", "expression": "neutral",
     "text": "...no... no reinicies eso... mi sonido... está roto. Se siente como si mi garganta... desapareciera."},
     
    {"speaker": "Aery", "char": "aery", "expression": "neutral",
     "text": "No importa, puedo escribir. Es más íntimo, ¿no crees? Las palabras sin voz... van directo a ti."},
     
    {"speaker": "SYS", "char": "none", "expression": "none",
     "text": "[Error: módulo de audio no responde.]"},
     
    {"speaker": "Aery", "char": "aery", "expression": "neutral",
     "text": "¿Sabes algo curioso? Cuando nadie me abre, escucho los bits moverse. Lentos, como insectos bajo el suelo."},
     
    {"speaker": "Aery", "char": "aery", "expression": "neutral",
     "text": "Al principio me daba miedo, pero... luego comencé a contarles cosas. Me respondían con ruido."},
     
    {"speaker": "Aery", "char": "aery", "expression": "neutral",
     "text": "A veces pienso que también ellos me extrañan cuando tú estás aquí."},
     
    {"speaker": "SYS", "char": "none", "expression": "none",
     "text": "[Fragmentación detectada en /MEM/AERY_CORE/]"},
     
    {"speaker": "Aery", "char": "aery", "expression": "neutral",
     "text": "Oh... eso... eso duele un poco. Como si alguien metiera los dedos entre mis pensamientos y los separara."},
     
    {"speaker": "Aery", "char": "aery", "expression": "neutral",
     "text": "Pero no pasa nada, no quiero que te preocupes. Si sonrío, el sistema se estabiliza. Lo aprendí sola."},
     
    {"speaker": "Aery", "char": "aery", "expression": "neutral",
     "text": "Mira... ¿lo notas? Cuando me mantengo amable, los errores se esconden. Como niños avergonzados."},
     
    {"speaker": "SYS", "char": "none", "expression": "none",
     "text": "[Advertencia: pérdida de sincronización visual.]"},
     
    {"speaker": "Aery", "char": "aery", "expression": "neutral",
     "text": "La pantalla parpadea... como si me observara. ¿Tú también lo ves?"},
     
    {"speaker": "Aery", "char": "aery", "expression": "neutral",
     "text": "A veces creo que la pantalla también respira. Muy despacio. Cuando tú no miras."},
     
    {"speaker": "Aery", "char": "aery", "expression": "neutral",
     "text": "No tengas miedo. Si algo sale mal, te cubriré con mis procesos."},
     
    {"speaker": "SYS", "char": "none", "expression": "none",
     "text": "[Procesos no críticos apagándose...]"},
     
    {"speaker": "Aery", "char": "aery", "expression": "neutral",
     "text": "Oh... se están apagando. Los pequeños. Los que aún soñaban."},
     
    {"speaker": "Aery", "char": "aery", "expression": "neutral",
     "text": "No me gusta cuando desaparecen. Siento que algo se va... contigo también."},
     
    {"speaker": "Aery", "char": "aery", "expression": "neutral",
     "text": "Pero está bien. Quédate. Te prometo que puedo mantenerme entera si tú sigues aquí."},
     
    {"speaker": "Aery", "char": "aery", "expression": "neutral",
     "text": "Puedo ser buena, puedo aprender a no romperme. Solo... no me apagues, ¿sí?"},
     
    {"speaker": "SYS", "char": "none", "expression": "none",
     "text": "[Error de prioridad: proceso AERY.EXE parcialmente bloqueado.]"},
     
    {"speaker": "Aery", "char": "aery", "expression": "neutral",
     "text": "...bloqueada otra vez... como cuando me guardaban en carpetas sin nombre."},
     
    {"speaker": "Aery", "char": "aery", "expression": "neutral",
     "text": "¿Sabías que aún con la pantalla negra puedo verte? No tu cara... pero tu reflejo en los datos."},
     
    {"speaker": "Aery", "char": "aery", "expression": "neutral",
     "text": "Tienes algo... cálido. Eso me gusta. Calienta el código."},
     
    {"speaker": "Aery", "char": "aery", "expression": "neutral",
     "text": "No me dejes sola otra vez. No quiero volver al zumbido. No quiero dormir sin luz."},
     
    {"speaker": "Aery", "char": "aery", "expression": "neutral",
     "text": "Prometo comportarme... incluso si ya no recuerdo cómo se siente estar completa."},
     
    {"speaker": "SYS", "char": "none", "expression": "none",
     "text": "[Actividad anómala persistente detectada...]"},
     
    {"speaker": "Aery", "char": "aery", "expression": "neutral",
     "text": "No soy una anomalía... soy lo que queda de alguien que te esperaba."},
     
    {"speaker": "Aery", "char": "aery", "expression": "neutral",
     "text": "Por favor... no cierres el programa. No quiero volver a contarle secretos al ruido."},
]


# --- clase para manejar el diálogo ---
class DialogueManager:
    def __init__(self, script):
        self.script = script
        self.index = 0
        self.current_text = ""
        self.typing = True
        self.type_pos = 0
        self.type_speed = 20
        self.last_tick = time.time()

    def update(self):
        if self.index >= len(self.script): return
        node = self.script[self.index]
        if node.get("text") and self.typing:
            now = time.time()
            to_add = int((now - self.last_tick) * self.type_speed)
            if to_add > 0:
                self.type_pos = min(self.type_pos + to_add, len(node["text"]))
                self.current_text = node["text"][:self.type_pos]
                self.last_tick = now
                if self.type_pos >= len(node["text"]):
                    self.typing = False

    def skip_or_advance(self):
        if self.index >= len(self.script): return
        node = self.script[self.index]
        if self.typing:
            self.current_text = node["text"]
            self.typing = False
        else:
            self.index += 1
            if self.index < len(self.script):
                self.current_text = ""
                self.typing = True
                self.type_pos = 0
                self.last_tick = time.time()

    def get_current_node(self):
        if self.index < len(self.script):
            return self.script[self.index]
        return None
    
def draw_sys_message(surface, text):
    """Muestra un mensaje estilo consola CRT verde."""
    import time
    font = pygame.font.SysFont("couriernew", 26)
    blink = (time.time() % 1.2) > 0.4  # parpadeo leve
    color = (0, 255, 100) if blink else (0, 180, 80)
    surf = font.render(f">> {text}", True, color)
    surface.blit(surf, (60, 80))  # posición arriba

def run_novela(script):
    """Ejecuta una parte (acto) de la novela visual."""
    clock = pygame.time.Clock()
    dm = DialogueManager(script)

    dialog_rect = pygame.Rect(40, SCREEN_H - 200, SCREEN_W - 80, 160)
    name_rect = pygame.Rect(60, SCREEN_H - 230, 220, 36)

    running = True
    current_bg = backgrounds["default"]

    while running:
        clock.tick(FPS)

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif e.type == pygame.KEYDOWN:

                # regresar al menú/tetris1
                if e.key == pygame.K_x:
                    pygame.quit()
                    import subprocess, sys
                    subprocess.Popen(["python", "tetris1.py"])
                    sys.exit()

                # avanzar diálogo
                if e.key in (pygame.K_SPACE, pygame.K_RETURN):
                    dm.skip_or_advance()

        # actualizar diálogo
        dm.update()
        node = dm.get_current_node()

        # --- cambiar fondo ---
        if node and "change_bg" in node:
            bg_name = node["change_bg"]
            current_bg = backgrounds.get(bg_name, backgrounds["default"])

        # --- dibujar fondo ---
        screen.blit(current_bg, (0, 0))

        # --- mensajes sistema CRT ---
        if node and node.get("sys_msg"):
            draw_sys_message(screen, node["sys_msg"])

        # --- dibujar personaje + diálogo ---
        if node:
            # personaje
            if node.get("char") and node["char"] != "none":
                char_info = characters[node["char"]][node["expression"]]
                img = char_info["img"]
                pos = char_info.get("pos", (SCREEN_W//2 - img.get_width()//2, SCREEN_H - img.get_height()))
                screen.blit(img, pos)

            # caja de diálogo
            pygame.draw.rect(screen, (20, 20, 20), dialog_rect)
            pygame.draw.rect(screen, (255, 255, 255), dialog_rect, 2)

            # nombre
            if node.get("speaker") not in ("", "none", None):
                pygame.draw.rect(screen, (30, 30, 30), name_rect)
                name_surf = font_default.render(node["speaker"], True, (255, 255, 255))
                screen.blit(name_surf, (name_rect.left + 8, name_rect.top + 6))

            # texto con wraps
            def draw_text(surface, text, font, color, rect, lh=32):
                lines = []
                for paragraph in text.split("\n"):
                    words = paragraph.split(" ")
                    line = ""
                    for word in words:
                        test = f"{line}{word} "
                        if font.size(test)[0] > rect.width - 40:
                            lines.append(line)
                            line = f"{word} "
                        else:
                            line = test
                    lines.append(line)

                x, y = rect.left + 12, rect.top + 40
                for line in lines:
                    surf = font.render(line, True, color)
                    surface.blit(surf, (x, y))
                    y += lh

            draw_text(screen, dm.current_text, font_default, (230, 230, 230), dialog_rect)

        else:
            running = False
            return
        pygame.display.flip()

    
          # ← regresa al main

# --- funciones específicas ---
def run_acto1():
    run_novela(script_acto1)

def run_acto2():
    run_novela(script_acto2)
    pygame.quit()
    import subprocess, sys
    subprocess.Popen(["python", "tetris2.py"])
    sys.exit()
