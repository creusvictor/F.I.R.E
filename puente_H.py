#! /usr/bin/env python
import RPi.GPIO as GPIO
import os
import time
#Define nombre de las entradas del puente H
ena = 12
in1 = 29
in2 = 31

enb = 26
in3 = 33
in4 = 35
#configura los pines segun el microprocesador Broadcom
GPIO.setmode(GPIO.BOARD)
#configura los pines como salidas
GPIO.setup(ena,GPIO.OUT)
GPIO.setup(enb,GPIO.OUT)
GPIO.setup(in1, GPIO.OUT)
GPIO.setup(in2, GPIO.OUT)
GPIO.setup(in3, GPIO.OUT)
GPIO.setup(in4, GPIO.OUT)
#Define las salidas PWM q
pwm_a = GPIO.PWM(ena,500)
pwm_b = GPIO.PWM(enb,500)
#inicializan los PWM con un duty Cicly de cero
pwm_a.start(0)
pwm_b.start(0)
# funciones de sentido de giro de los motores
def Giro_Favor_Reloj_MotorA():
	GPIO.output(in1,False)
	GPIO.output(in2,True)

def Giro_Contra_Reloj_MotorA():
	GPIO.output(in1,True)
	GPIO.output(in2,False)

def Giro_Favor_Reloj_MotorB():
	GPIO.output(in3,False)
	GPIO.output(in4,True)

def Giro_Contra_Reloj_MotorB():
	GPIO.output(in3,True)
	GPIO.output(in4,False)

def Parar_Motores():
	GPIO.output(in1,False)
	GPIO.output(in2,False)
	GPIO.output(in3,False)
	GPIO.output(in4,False)
#limpia la pantalla
os.system('clear')
print("Elija la direccion w,a,s,d  y q para parar")
print("CTRL-C para salir")
print
try:
	while True:
		cmd = raw_input("inserte el comando ")
		cmd = cmd.lower()
		motor = cmd[0]
		velocidad ="100"

		if motor == "w":
			Giro_Favor_Reloj_MotorA()
			Giro_Favor_Reloj_MotorB()
			print("motor forward, vel="+velocidad)
			pwm_a.ChangeDutyCycle(int(velocidad))
			pwm_b.ChangeDutyCycle(int(velocidad))
			print
		elif motor == "q":
			velocidad="0"
                        Parar_Motores()
                        print("motor stoped, vel="+velocidad)
                     	pwm_a.ChangeDutyCycle(int(velocidad))
                        pwm_b.ChangeDutyCycle(int(velocidad))
                        print
		elif motor == "a":
                        Giro_Contra_Reloj_MotorA()
                        Giro_Favor_Reloj_MotorB()
                        print("motor left, vel="+velocidad)
                        pwm_a.ChangeDutyCycle(int(velocidad))
                        pwm_b.ChangeDutyCycle(int(velocidad))
                        print
		elif motor == "s":
                        Giro_Contra_Reloj_MotorA()
                        Giro_Contra_Reloj_MotorB()
                        print("motor backward, vel="+velocidad)
                        pwm_a.ChangeDutyCycle(int(velocidad))
                        pwm_b.ChangeDutyCycle(int(velocidad))
                        print
		elif motor == "d":
                        Giro_Favor_Reloj_MotorA()
                        Giro_Contra_Reloj_MotorB()
                        print("motor forward, vel="+velocidad)
                   	pwm_a.ChangeDutyCycle(int(velocidad))
                        pwm_b.ChangeDutyCycle(int(velocidad))
                        print

		else:
			print
			print("comando no reconocido")
			print
except KeyboardInterrupt:
	pwm_a.stop()
	pwm_b.stop()
	GPIO.cleanup()
	os.system('clear')
	print
	print("Programa Terminado por el usuario")
	print
	exit()


