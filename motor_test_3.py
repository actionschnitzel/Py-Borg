#http://raspitips.de/raspberry-pi-gleichstrommotor-mit-motortreiber-l293d-und-pulsweitenmodulation/

#coding: utf8
# Erforderliche Bibliotheken importieren
import RPi.GPIO as GPIO
import time
from gpiozero import Button
 
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

def back_forth():
        uhrzeigersinn1.ChangeDutyCycle(25)
        time.sleep(1)
        uhrzeigersinn1.stop()
        gegen_uhrzeigersinn1.ChangeDutyCycle(25)
        time.sleep(1)
        gegen_uhrzeigersinn1.stop()
        uhrzeigersinn1.start(0)
        gegen_uhrzeigersinn1.start(0)
        
def f_ward(button):
    if button.pin.number == 4:
        uhrzeigersinn1.ChangeDutyCycle(50)
        uhrzeigersinn2.ChangeDutyCycle(50)
        time.sleep(0.5)
        uhrzeigersinn1.stop()
        uhrzeigersinn2.stop()
        uhrzeigersinn1.start(0)
        uhrzeigersinn2.start(0)
        gegen_uhrzeigersinn1.start(0)
        gegen_uhrzeigersinn2.start(0)
        
def b_ward(button):
    if button.pin.number == 17:
        gegen_uhrzeigersinn1.ChangeDutyCycle(50)
        gegen_uhrzeigersinn2.ChangeDutyCycle(50)
        time.sleep(0.5)
        uhrzeigersinn1.stop()
        uhrzeigersinn1.start(0)
        uhrzeigersinn2.stop()
        uhrzeigersinn2.start(0)
        gegen_uhrzeigersinn1.start(0)
        gegen_uhrzeigersinn2.start(0)
        
def t_left(button):
    if button.pin.number == 6:
        gegen_uhrzeigersinn2.ChangeDutyCycle(50)
        uhrzeigersinn1.ChangeDutyCycle(50)
        time.sleep(0.5)
        uhrzeigersinn1.stop()
        uhrzeigersinn1.start(0)
        uhrzeigersinn2.stop()
        uhrzeigersinn2.start(0)
        gegen_uhrzeigersinn1.start(0)
        gegen_uhrzeigersinn2.start(0)
        
def t_right(button):
    if button.pin.number == 5:
        gegen_uhrzeigersinn1.ChangeDutyCycle(50)
        uhrzeigersinn2.ChangeDutyCycle(50)
        time.sleep(0.5)
        uhrzeigersinn1.stop()
        uhrzeigersinn1.start(0)
        uhrzeigersinn2.stop()
        uhrzeigersinn2.start(0)
        gegen_uhrzeigersinn1.start(0)
        gegen_uhrzeigersinn2.start(0)

forward.when_pressed  = f_ward
backward.when_pressed  = b_ward
left.when_pressed  = t_left
right.when_pressed  = t_right

#gegen_uhrzeigersinn1.ChangeDutyCycle(50)
#gegen_uhrzeigersinn2.ChangeDutyCycle(50)
