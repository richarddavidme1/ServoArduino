import pyfirmata
import tkinter as tk

#Movimiento del servo con los datos del control
def MoverServo(angulo):
    #Se pasa los datos al pin 9 digital para el angulo del servomotor
    pin9.write(angulo)
    #Conversion de un string a un entero
    rango=int(angulo)
    if rango >= 100:
        print("Mayor del rango establecido")
        #Encendido del led de la placa
        PlacaMega.digital[13].write(1)
    else:
        print("Menor del rango establecido")
        #Apagado del led de la placa
        PlacaMega.digital[13].write(0)

#Conexion con la placa arduino
PlacaMega= pyfirmata.Arduino('COM3')
#Activar arduino para ingreso de datos
IngresoDatos = pyfirmata.util.Iterator(PlacaMega)
#Iniciar
IngresoDatos.start()
#Pin para realizar el PWM  digitales
pin9 = PlacaMega.get_pin('d:9:s')
#Iniciar el led apagado
PlacaMega.digital[13].write(0)

#iniciar la pantalla
ventana = tk.Tk()
#Titulo de la pantalla
ventana.title("CONTROL DE SERVOMOTOR")
#Control deslizante gráfico DE 0 A 175 angulo
scale = tk.Scale(ventana, command=MoverServo,to=175,orient=tk.HORIZONTAL, length=600, label='Angulo del servomotor',bg="#76448a",font=("Arial",30))
scale.pack(anchor=tk.CENTER)
ventana.mainloop()


