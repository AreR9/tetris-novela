# main.py
import subprocess
import sys
import time
import pygame
import novela   # importa el módulo completo (no sólo funciones)

def run_tetris(filename="tetris1.py"):
    subprocess.run([sys.executable, filename])

def main():
    print("=== INICIANDO ACTO 1 ===")
    novela.run_acto1()

    # minimizamos/ocultamos la ventana de la novela
    try:
        pygame.display.iconify()
    except Exception:
        # iconify puede fallar en algunos entornos; ignoramos el fallo
        pass

    # pequeña pausa para que la ventana tenga tiempo de minimizarse
    time.sleep(0.15)

    print("\n=== INICIANDO TETRIS ===")
    run_tetris("tetris2.py")   # corre tetris1.py en proceso separado

    # cuando tetris termine, restauramos/reasignamos la pantalla dentro del módulo novela
    # (no modificamos archivos de novela.py, sólo reasignamos su variable global `screen`)
    try:
        # si pygame sigue inicializado, sólo re-creamos el display Surface
        novela.screen = pygame.display.set_mode((novela.SCREEN_W, novela.SCREEN_H))
        pygame.display.set_caption("Novela + Tetris")
    except Exception:
        # si por alguna razón pygame fue cerrado, inicializamos de nuevo y creamos pantalla
        pygame.init()
        novela.screen = pygame.display.set_mode((novela.SCREEN_W, novela.SCREEN_H))
        pygame.display.set_caption("Novela + Tetris")

    # opcional: forzamos una actualización rápida para que la ventana aparezca limpia
    novela.screen.fill((0,0,0))
    pygame.display.flip()
    time.sleep(0.15)

    print("\n=== INICIANDO ACTO 2 ===")
    novela.run_acto2()   # ejecuta acto 2 (usa la screen reasignada)

    run_tetris("tetris2.py")

    print("\n=== FIN ===")

if __name__ == "__main__":
    main()
