#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from gtts import gTTS
from pydub import AudioSegment
#Codigo para el tkinter
from tkinter import Entry,Button, Label,filedialog, ttk, Tk, Frame, PhotoImage
import pygame
import random
import mutagen

pygame.mixer.init()
pygame.mixer.init(frequency=44100)
cancion_actual = ''
direccion = ''
lista = []
variable = 'N0' #para definir si el chatbot se encuentra dentro del cuestionario(=C) o no (=N) y adiciona el numero de la pregunta en la que se encuentra el cuestionario en el caso que este
diceTexto=''
numeroPregunta = -1

def escribirArchivo(texto):
    path = os.path.abspath(
            os.path.join(os.path.dirname(__file__), 'auditoria.txt'))
    with open(path, 'a') as f:
                f.write(texto+'\n')
#Codigo para el tkinter metodos----------------------
def detener_efecto():
    barra1['value'] = 50
    barra2['value'] = 60
    barra3['value'] = 70
    barra4['value'] = 80
    barra5['value'] = 90
    barra6['value'] = 100
    barra7['value'] = 90
    barra8['value'] = 80
    barra9['value'] = 70
    barra10['value'] = 60
    barra11['value'] = 60
    barra12['value'] = 70
    barra13['value'] = 80
    barra14['value'] = 90
    barra15['value'] = 100
    barra16['value'] = 90
    barra17['value'] = 80
    barra18['value'] = 70
    barra19['value'] = 60
    barra20['value'] = 50

def iniciar_conversacion():#Inicia la conversacion
    nexus()#llamamos al metodo del nexus que permiter iniciar el dialogo

def conversacion_texto():
    chatTexto.configure(state='disabled')
    nexusTexto()

def abrir_archivo():
    global direccion, pos, n , cancion_actual
    pos = 0
    n = 0
    direccion = '/home/tb2/audio.wav'
    
    n = len (direccion)
    print (direccion+ " abre el sample")
    cancion_actual = direccion
    
    nombre_cancion = cancion_actual.split('/')
    nombre_cancion = nombre_cancion[-1]
    print (" --- " + nombre_cancion)
for i in range (50,200,100):
    lista.append(i)
def iniciar_reproduccion():
    #print(" inicia la reproduccion")
    global cancion_actual, direccion, pos, b, actualizar
    barra1['value'] = random.choice(lista)
    barra2['value'] = random.choice(lista)
    barra3['value'] = random.choice(lista)
    barra4['value'] = random.choice(lista)
    barra5['value'] = random.choice(lista)
    barra6['value'] = random.choice(lista)
    barra7['value'] = random.choice(lista)
    barra8['value'] = random.choice(lista)
    barra9['value'] = random.choice(lista)
    barra10['value'] = random.choice(lista)
    barra11['value'] = random.choice(lista)
    barra12['value'] = random.choice(lista)
    barra13['value'] = random.choice(lista)
    barra14['value'] = random.choice(lista)
    barra15['value'] = random.choice(lista)
    barra16['value'] = random.choice(lista)
    barra17['value'] = random.choice(lista)
    barra18['value'] = random.choice(lista)
    barra19['value'] = random.choice(lista)
    barra20['value'] = random.choice(lista)
    
    nombre_cancion = cancion_actual.split('/')
    nombre_cancion = nombre_cancion[-1]
    #nombre['text'] = nombre_cancion #el texto nombre de la reproduccion
    
    time = pygame.mixer.music.get_pos()
    current_time = (float(time)/float(1000)).__round__(0)    
    timeA = time/1000
    x = int (int (time)*0.001)
    tiempo ['value'] = x # posicion de la cancion
    
    y = float (int(10)*0.1)
    pygame.mixer.music.set_volume(y)
    #nivel['text'] = int(y*100)

    audio = mutagen.File(cancion_actual)
    #print("audio>>>>>> "+ audio.info)
    log = audio.info.length
    minutos, segundos = divmod(log, 60)
    
    minutos, segundos = int(minutos), float(segundos)
    tt= minutos * 60 + (segundos)
    #tiempo['maximum'] = tt #tiempo total de la cancion

    #texto['text'] = str(minutos) + ":" + str(segundos) #el texto de la duracion de la reproduccion 1
    #print("tiempo total ")
    #print(tt)    
    actualizar = ventana.after(100, iniciar_reproduccion)
    
    if  pygame.mixer.music.get_busy()==False:
        ventana.after_cancel(actualizar)
        #texto['text'] = "00:00" #el texto de la duracion de la reproduccion 2
        detener_efecto()
        
        if pos != n:
            pygame.mixer.music.stop()
            #nexus()#para dar el paso a que se siga conversando con el robot
        if pos==n:
            pos = 0

def iniciar():
    global cancion_actual
    
    pygame.mixer.music.load(cancion_actual)
    pygame.mixer.music.play()
    iniciar_reproduccion()

#----------------------------------------------------

#Parte grafica usanto kTinker
ventana = Tk()
ventana.title('CHATBOT NEXUS')
ventana.config(background = 'white')
ventana.resizable(0,0)
ventana.geometry('500x700')

estilo = ttk.Style()
estilo.theme_use('clam')
estilo.configure("Vertical.TProgressbar", foreground ='green2', background = 'green2', troughcolor ='black',
    bordercolor = 'black', lightcolor = 'green2', darkcolor = 'green2')

frame0 = Frame (ventana, bg ='black', width=600, height=300)
frame0.grid(column=0, row=0, sticky='nsew')

frame1 = Frame (ventana, bg ='black', width=600, height=250)
frame1.grid(column=0, row=1, sticky='nsew')

frame2 = Frame (ventana, bg ='black', width=600, height=50)
frame2.grid(column=0, row=2, sticky='nsew')

#barras extras para dar espacio desde el margen
barra101= ttk.Progressbar(frame1, orient='vertical', length=300, maximum=300, style="Vertical.TProgressbar")
barra101.grid(column = 0, row = 0, padx = 1)
barra102= ttk.Progressbar(frame1, orient='vertical', length=300, maximum=300, style="Vertical.TProgressbar")
barra102.grid(column = 1, row = 0, padx = 1)
barra103= ttk.Progressbar(frame1, orient='vertical', length=300, maximum=300, style="Vertical.TProgressbar")
barra103.grid(column = 2, row = 0, padx = 1)
#---------------------------------------------

barra1= ttk.Progressbar(frame1, orient='vertical', length=300, maximum=300, style="Vertical.TProgressbar")
barra1.grid(column = 3, row = 0, padx = 1)
barra2= ttk.Progressbar(frame1, orient='vertical', length=300, maximum=300, style="Vertical.TProgressbar")
barra2.grid(column = 4, row = 0, padx = 1)
barra3= ttk.Progressbar(frame1, orient='vertical', length=300, maximum=300, style="Vertical.TProgressbar")
barra3.grid(column = 5, row = 0, padx = 1)
barra4= ttk.Progressbar(frame1, orient='vertical', length=300, maximum=300, style="Vertical.TProgressbar")
barra4.grid(column = 6, row = 0, padx = 1)
barra5= ttk.Progressbar(frame1, orient='vertical', length=300, maximum=300, style="Vertical.TProgressbar")
barra5.grid(column = 7, row = 0, padx = 1)
barra6= ttk.Progressbar(frame1, orient='vertical', length=300, maximum=300, style="Vertical.TProgressbar")
barra6.grid(column = 8, row = 0, padx = 1)
barra7= ttk.Progressbar(frame1, orient='vertical', length=300, maximum=300, style="Vertical.TProgressbar")
barra7.grid(column = 9, row = 0, padx = 1)
barra8= ttk.Progressbar(frame1, orient='vertical', length=300, maximum=300, style="Vertical.TProgressbar")
barra8.grid(column = 10, row = 0, padx = 1)
barra9= ttk.Progressbar(frame1, orient='vertical', length=300, maximum=300, style="Vertical.TProgressbar")
barra9.grid(column = 11, row = 0, padx = 1)
barra10= ttk.Progressbar(frame1, orient='vertical', length=300, maximum=300, style="Vertical.TProgressbar")
barra10.grid(column = 12, row = 0, padx = 1)
barra11= ttk.Progressbar(frame1, orient='vertical', length=300, maximum=300, style="Vertical.TProgressbar")
barra11.grid(column = 13, row = 0, padx = 1)
barra12= ttk.Progressbar(frame1, orient='vertical', length=300, maximum=300, style="Vertical.TProgressbar")
barra12.grid(column = 14, row = 0, padx = 1)
barra13= ttk.Progressbar(frame1, orient='vertical', length=300, maximum=300, style="Vertical.TProgressbar")
barra13.grid(column = 15, row = 0, padx = 1)
barra14= ttk.Progressbar(frame1, orient='vertical', length=300, maximum=300, style="Vertical.TProgressbar")
barra14.grid(column = 16, row = 0, padx = 1)
barra15= ttk.Progressbar(frame1, orient='vertical', length=300, maximum=300, style="Vertical.TProgressbar")
barra15.grid(column = 17, row = 0, padx = 1)
barra16= ttk.Progressbar(frame1, orient='vertical', length=300, maximum=300, style="Vertical.TProgressbar")
barra16.grid(column = 18, row = 0, padx = 1)
barra17= ttk.Progressbar(frame1, orient='vertical', length=300, maximum=300, style="Vertical.TProgressbar")
barra17.grid(column = 19, row = 0, padx = 1)
barra18= ttk.Progressbar(frame1, orient='vertical', length=300, maximum=300, style="Vertical.TProgressbar")
barra18.grid(column = 20, row = 0, padx = 1)
barra19= ttk.Progressbar(frame1, orient='vertical', length=300, maximum=300, style="Vertical.TProgressbar")
barra19.grid(column = 21, row = 0, padx = 1)
barra20= ttk.Progressbar(frame1, orient='vertical', length=300, maximum=300, style="Vertical.TProgressbar")
barra20.grid(column = 22, row = 0, padx = 1)

#Ubicamos las barras de una manera inicial
barra1['value'] = 50
barra2['value'] = 60
barra3['value'] = 70
barra4['value'] = 80
barra5['value'] = 90
barra6['value'] = 100
barra7['value'] = 90
barra8['value'] = 80
barra9['value'] = 70
barra10['value'] = 60
barra11['value'] = 60
barra12['value'] = 70
barra13['value'] = 80
barra14['value'] = 90
barra15['value'] = 100
barra16['value'] = 90
barra17['value'] = 80
barra18['value'] = 70
barra19['value'] = 60
barra20['value'] = 50

estilo1 = ttk.Style()
estilo1.theme_use('clam')

estilo1.configure("Horizontal.TProgressbar", foreground='red', background ='black', troughcolor='DarkOrchid1',
                                                                bordercolor ='#970BD9', lightcolor='#970BD9', darkcolor='black')

tiempo = ttk.Progressbar(frame2, orient ='horizontal', length=390, mode ='determinate', style="Horizontal.TProgressbar")
#         ttk.Progressbar(frame2, orient ='horizontal', lenght=390, mode ='determinate', style="Horizontal.TProgressbar")

tiempo.grid(row=0, columnspan=8, padx=5)
texto = Label(frame2, bg='black', fg='green2', width=5)
texto.grid(row=0, column=8)

nombre = Label(frame2, bg='black', fg='red', width=55)
nombre.grid(column =0, row=0, columnspan=8, padx=5)

cantidad = Label(frame2, bg='black', fg='green2')
cantidad.grid(column = 8, row=1)

imagenOjos = PhotoImage( file = '/home/tb2/ojos1.png')
lblImagen = Label(frame0, image = imagenOjos).place(x=0,y=0)

imagenMicro = PhotoImage( file = '/home/tb2/micro.png')

botonMicrofono = Button(frame2, bg = 'blue', command = iniciar_conversacion, image = imagenMicro)
botonMicrofono.grid(column=6, row=2, pady=10)

style = ttk.Style()
style.configure('Horizontal.TScale',bordercolor='green2', troughcolor='black', background='green2', foreground='green2',
    lightcolor='green2', darkcolor='black')
    
#nivel = Label(frame2, bg='black', fg='green2', width=3)
#nivel.grid(column=8, row=2)

#componente para ingresar por chat la conversacion
chatTexto = Entry(frame2)
chatTexto.grid(column=2, row=2, pady=10)
diceTexto = chatTexto.get()#obtenemos el valor de la caja de texto

#componente para enviar la respuesta de lo ingresado a traves de texto
imagenSend = PhotoImage( file = '/home/tb2/send.png')
botonEnviarTexto = Button(frame2, bg = 'green', command = conversacion_texto, image = imagenSend)
botonEnviarTexto.grid(column=3, row=2, pady=10)

#--------------------------------------------

# NOTE: this example requires PyAudio because it uses the Microphone class

import speech_recognition as sr
import rospy
from std_msgs.msg import String
from tutorial.srv import ChatBotVariables

# This module is imported so that we can
# play the converted audio
import os

def contarPalabras(linea):
        simbolos = ['¿','?','.','.',';',':','¡','!']
        numpalabras = 0
        
            
        for simbolo in simbolos:
            linea = linea.replace(simbolo,' ')
        palabras = linea.split()
        for palabra in palabras:            
            numpalabras += 1                    
        print('Principal El texto contiene %s palabras' %numpalabras)
        return numpalabras

#para el nodo servidor del cuestionario
def chatBot_client(x):
    print("Ingresa al cliente para el chatBotS")    
    rospy.wait_for_service('chatBotS')
    try:
        respuestaCuestionario = rospy.ServiceProxy('chatBotS', ChatBotVariables)
        resp1 = respuestaCuestionario(x)
        return resp1.response
    except rospy.ServiceException as e:
        print("Service chatBot call failed: %s"%e)

def nexus():    
        
        global variable #para manejar la variable que determina si nos encontramos dentro o fuera del chatbot
        # obtain audio from the microphone
        r = sr.Recognizer()
        print(sr.Microphone.list_microphone_names())

        for index, name in enumerate(sr.Microphone.list_microphone_names()):
            print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))

        with sr.Microphone(device_index=10) as source:
            #r.adjust_for_ambient_noise(source)
            print("Di, algo")
            audio = r.listen(source, phrase_time_limit = 5 )

        # recognize speech using Google Speech Recognition
        try:
            # for testing purposes, we're just using the default API key
            # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
            # instead of `r.recognize_google(audio)`
            print("Analizando")
            dice = r.recognize_google(audio,language='es-MX')
            print("Google Speech Recognition thinks you said> " + dice)
            escribirArchivo(dice)
            respuestaChatBot = "%s"%(chatBot_client(dice+variable))#se envia una N para hacer referencia que esta en el CHAT NORMAL
            escribirArchivo(respuestaChatBot)
            with open('auditoria', 'w') as f:
                f.write('file contents\n')

            print(respuestaChatBot+ " >>>>>>>>")

            numeroPregunta= int(respuestaChatBot[len(respuestaChatBot)-1])
            estaCues= respuestaChatBot[len(respuestaChatBot)-2]
            respuestaChatBot= respuestaChatBot[:len(respuestaChatBot)-2]

            if (estaCues=="N"):#para ver si esta en el cuestionario
                        variable = "N0"
            else:
                numeroPregunta = numeroPregunta+1
                variable = "C"+str(numeroPregunta)
                if numeroPregunta == 10:
                   variable = "N1"
            

            # Language in which you want to convert
            language = 'es'

            # Passing the text and language to the engine,
            # here we have marked slow=False. Which tells
            # the module that the converted audio should
            # have a high speed
            print("audio que envia a grabar "+respuestaChatBot)
            myobj = gTTS(text=respuestaChatBot, lang=language, slow=False)
            
            # Saving the converted audio in a mp3 file named
            myobj.save("audio.mp3")

            # files                                                                         
            src = "audio.mp3"
            dst = "audio.wav"

            # convert wav to mp3                                                            
            sound = AudioSegment.from_mp3(src)
            sound.export(dst, format="wav")

            # Playing the converted file
            abrir_archivo()
            iniciar()
            

        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
            myobj = gTTS(text="Lo siento, pero no entiendo. Puede repetir", lang='es', slow=False)

            # Saving the converted audio in a mp3 file name
            myobj.save("audio.mp3")
            
            # files                                                                         
            src = "audio.mp3"
            dst = "audio.wav"

            # convert wav to mp3                                                            
            sound = AudioSegment.from_mp3(src)
            sound.export(dst, format="wav")

            # Playing the converted file
            abrir_archivo()
            iniciar()#Iniciamos la animacion (interfaz grafica)            
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))


def nexusTexto():    
        
        global variable #para manejar la variable que determina si nos encontramos dentro o fuera del chatbot
        global diceTexto #para manejar la variable que contiene el texto ingresado por la caja de texto
        # obtain el texto desde el teclado
        #diceTexto = "es lo que se manda desde la caja de texto"
        diceTexto = chatTexto.get()
       

        chatTexto.configure(state='normal')
        chatTexto.delete(0,'end')        
        
        numeroPalabras = contarPalabras(diceTexto)
        #print("Numero de palabras " + numeroPalabras)
        #print("Lo que se envia como texto>>> " + diceTexto+variable + " numero "+ numeroPalabras)

        escribirArchivo(diceTexto)
        

        respuestaChatBot = "%s"%(chatBot_client(diceTexto+variable))#se envia una N para hacer referencia que esta en el CHAT NORMAL
        print(" Respuesta chatbot>>>>>>>>" + respuestaChatBot )

        escribirArchivo(respuestaChatBot)

        estaCues= respuestaChatBot[len(respuestaChatBot)-2]
        numeroPregunta= int(respuestaChatBot[len(respuestaChatBot)-1])
        respuestaChatBot= respuestaChatBot[:len(respuestaChatBot)-2]

        if (estaCues=="N"):#para ver si esta en el cuestionario
            variable = "N0"
        else:
            numeroPregunta = numeroPregunta+1
            variable = "C"+str(numeroPregunta)
            if numeroPregunta == 10:
                variable = "N1"

        # Language in which you want to convert
        language = 'es'

        # Passing the text and language to the engine,
        # here we have marked slow=False. Which tells
        # the module that the converted audio should
        # have a high speed
        print("audio que envia a grabar "+respuestaChatBot)
        myobj = gTTS(text=respuestaChatBot, lang=language, slow=False)
            
        # Saving the converted audio in a mp3 file named
        myobj.save("audio.mp3")

        # files                                                                         
        src = "audio.mp3"
        dst = "audio.wav"

        # convert wav to mp3                                                            
        sound = AudioSegment.from_mp3(src)
        sound.export(dst, format="wav")

        # Playing the converted file
        abrir_archivo()
        iniciar()         


if __name__ == '__main__':
    ventana.mainloop()
    