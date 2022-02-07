import pygame
import RPi.GPIO as GPIO
import time
from gpiozero import Button

pygame.init()

spielaktiv = True

# genutzte Farbe
ORANGE  = ( 255, 140, 0)
ROT     = ( 255, 0, 0)
GRUEN   = ( 0, 255, 0)
SCHWARZ = ( 0, 0, 0)
WEiSS   = ( 255, 255, 255)

# Fenster öffnen
pygame.display.set_mode((640, 480))

# Titel für Fensterkopf
pygame.display.set_caption("Unser erstes Pygame-Spiel")

# Konvention für Pinnummerierung festlegen (BCM bzw. Board)
GPIO.setmode(GPIO.BCM)
# Warnungen, die das Ausführen des Programms verhindern, wenn
# Ausgang bereits als OUT deklariert wurde ignorieren
GPIO.setwarnings(False)
# Pins als Ausgänge deklarieren
GPIO.setup(21, GPIO.OUT)
GPIO.setup(25, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)


    
# PWM für Richtungen mit Frequenz festlegen
uhrzeigersinn1 = GPIO.PWM(21, 50)
gegen_uhrzeigersinn1 = GPIO.PWM(25, 50)
uhrzeigersinn2 = GPIO.PWM(26, 50)
gegen_uhrzeigersinn2 = GPIO.PWM(20, 50)
# PWM mit Tastgrad 0% initialisieren
forward = Button(4)
backward = Button(17)
left = Button(6)
right = Button(5)


uhrzeigersinn1.start(0)
gegen_uhrzeigersinn1.start(0)
uhrzeigersinn2.start(0)
gegen_uhrzeigersinn2.start(0)

# Schleife Hauptprogramm
while spielaktiv:
    # Überprüfen, ob Nutzer eine Aktion durchgeführt hat
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            spielaktiv = False
            print("Spieler hat Quit-Button angeklickt")
        elif event.type == pygame.KEYDOWN:
            print("Spieler hat Taste gedrückt")
            if event.key == pygame.K_RIGHT:
                #print("Spieler hat Pfeiltaste rechts gedrückt")
                gegen_uhrzeigersinn1.ChangeDutyCycle(50)
                uhrzeigersinn2.ChangeDutyCycle(50)
                time.sleep(0.5)
                uhrzeigersinn1.stop()
                uhrzeigersinn1.start(0)
                uhrzeigersinn2.stop()
                uhrzeigersinn2.start(0)
                gegen_uhrzeigersinn1.start(0)
                gegen_uhrzeigersinn2.start(0)
            elif event.key == pygame.K_LEFT:
                #print("Spieler hat Pfeiltaste links gedrückt")
                gegen_uhrzeigersinn2.ChangeDutyCycle(50)
                uhrzeigersinn1.ChangeDutyCycle(50)
                time.sleep(0.5)
                uhrzeigersinn1.stop()
                uhrzeigersinn1.start(0)
                uhrzeigersinn2.stop()
                uhrzeigersinn2.start(0)
                gegen_uhrzeigersinn1.start(0)
                gegen_uhrzeigersinn2.start(0)
            elif event.key == pygame.K_UP:
                #print("Spieler hat Pfeiltaste hoch gedrückt")
                uhrzeigersinn1.ChangeDutyCycle(50)
                uhrzeigersinn2.ChangeDutyCycle(50)
                time.sleep(0.5)
                uhrzeigersinn1.stop()
                uhrzeigersinn2.stop()
                uhrzeigersinn1.start(0)
                uhrzeigersinn2.start(0)
                gegen_uhrzeigersinn1.start(0)
                gegen_uhrzeigersinn2.start(0)
            elif event.key == pygame.K_DOWN:
                gegen_uhrzeigersinn1.ChangeDutyCycle(50)
                gegen_uhrzeigersinn2.ChangeDutyCycle(50)
                time.sleep(0.5)
                uhrzeigersinn1.stop()
                uhrzeigersinn1.start(0)
                uhrzeigersinn2.stop()
                uhrzeigersinn2.start(0)
                gegen_uhrzeigersinn1.start(0)
                gegen_uhrzeigersinn2.start(0)
                
                #print("Spieler hat Pfeiltaste runter gedrückt")
#             elif event.key == pygame.K_SPACE:
#                 print("Spieler hat Leertaste gedrückt")
#         elif event.type == pygame.MOUSEBUTTONDOWN:
#             print("Spieler hast Maus angeklickt")
            
forward.when_pressed  = f_ward
backward.when_pressed  = b_ward
left.when_pressed  = t_left
right.when_pressed  = t_right