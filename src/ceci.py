#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from gtts import gTTS
from pydub import AudioSegment
#Codigo para el tkinter
from tkinter import Entry,Button, Label,filedialog, ttk, Tk, Frame, PhotoImage
from PIL import Image, ImageTk
import pygame
import random
import mutagen
import tkinter as tk
from datetime import datetime

pygame.mixer.init()
pygame.mixer.init(frequency=44100)
cancion_actual = ''
direccion = ''
lista = []
variable = 'N0' #para definir si el chatbot se encuentra dentro del cuestionario(=C) o no (=N) y adiciona el numero de la pregunta en la que se encuentra el cuestionario en el caso que este
diceTexto=''
numeroPregunta = -1
global micro

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

def escribirArchivo(texto):
    path = os.path.abspath(
            os.path.join(os.path.dirname(__file__), 'auditoria.txt'))
    with open(path, 'a') as f:
                f.write(texto+'\n')

#Codigo para el tkinter metodos----------------------
def detener_efecto():
    print("detener efecto")        
    anim2.after_cancel(anim2.cancel)
    anim2.pack()

def iniciar_conversacion():#Inicia la conversacion
    #micro["state"] = "disabled"
    nexus()#llamamos al metodo del nexus que permiter iniciar el dialogo

def conversacion_texto():
    #chatTexto.configure(state='disabled')
    nexusTexto()

def abrir_archivo():
    global direccion, pos, n , cancion_actual
    pos = 0
    n = 0
    direccion = '/home/andres/catkin_ws/src/tutorial/audio_files/user_audio/u_audio.wav'    
    
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

    print(" inicia la reproduccion - el efecto")
    
    
    nombre_cancion = cancion_actual.split('/')
    nombre_cancion = nombre_cancion[-1]
    #nombre['text'] = nombre_cancion #el texto nombre de la reproduccion
    
    time = pygame.mixer.music.get_pos()
    current_time = (float(time)/float(1000)).__round__(0)    
    timeA = time/1000
    x = int (int (time)*0.001)
    #tiempo ['value'] = x # posicion de la cancion
    
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
        #detener_efecto()
        anim2.after_cancel(anim2.cancel)
        anim2.pack()
        
        if pos != n:
            pygame.mixer.music.stop()
            #nexus()#para dar el paso a que se siga conversando con el robot
        if pos==n:
            pos = 0

def iniciar():
    global cancion_actual
    
    pygame.mixer.music.load(cancion_actual)
    pygame.mixer.music.play()
    anim2.play()#envía que se inicie el gif
    iniciar_reproduccion()

#----------------------------------------------------

#Parte grafica usanto kTinker
class MyLabel(Label):
    def __init__(self, master, filename):
        im = Image.open(filename)
        seq =  []
        try:
            while 1:
                seq.append(im.copy())
                im.seek(len(seq)) # skip to next frame
        except EOFError:
            pass # we're done

        try:
            self.delay = im.info['duration']
        except KeyError:
            self.delay = 100

        first = seq[0].convert('RGBA')
        self.frames = [ImageTk.PhotoImage(first)]

        Label.__init__(self, master, image=self.frames[0])

        lut = [1] * 256        

        try:  
            lut[im.info["transparency"]] = 0
        except Exception as e: 
            print(e)

        temp = seq[0]
        for image in seq[1:]:
            mask = image.point(lut, "1")
            # point() is used to map image pixels into mask pixels
            # via the lookup table (lut), creating a mask
            # with value 0 at transparent pixels and
            # 1 elsewhere
            temp.paste(image, None, mask) #paste with mask
            frame = temp.convert('RGBA')
            self.frames.append(ImageTk.PhotoImage(frame))

        self.idx = 0

        self.cancel = self.after(1000, self.play)

    def play(self):
        self.config(image=self.frames[self.idx])
        self.idx += 1
        if self.idx == len(self.frames):
            self.idx = 0
        self.cancel = self.after(self.delay, self.play)    

class MyLabel2(Label):
    def __init__(self, master, filename):
        im = Image.open(filename)
        seq =  []
        try:
            while 1:
                seq.append(im.copy())
                im.seek(len(seq)) # skip to next frame
        except EOFError:
            pass # we're done

        try:
            self.delay = im.info['duration']
        except KeyError:
            self.delay = 100

        first = seq[0].convert('RGBA')
        self.frames = [ImageTk.PhotoImage(first)]

        Label.__init__(self, master, image=self.frames[0])

        lut = [1] * 256        

        try:  
            lut[im.info["transparency"]] = 0
        except Exception as e: 
            print(e)

        temp = seq[0]
        for image in seq[1:]:
            mask = image.point(lut, "1")
            # point() is used to map image pixels into mask pixels
            # via the lookup table (lut), creating a mask
            # with value 0 at transparent pixels and
            # 1 elsewhere
            temp.paste(image, None, mask) #paste with mask
            frame = temp.convert('RGBA')
            self.frames.append(ImageTk.PhotoImage(frame))

        self.idx = 0

        self.cancel = self.after(1000, self.play)

    def play(self):
        self.config(image=self.frames[self.idx])
        self.idx += 1
        if self.idx == len(self.frames):
            self.idx = 0
        self.cancel = self.after(self.delay, self.play)     

ventana = Tk()

ventana.title('CHATBOT CECI')
ventana.config(background = 'white')

ventana.geometry('1900x1080')

anim = MyLabel(ventana, '/home/andres/o2.gif')
anim.pack()
anim2 = MyLabel2(ventana, '/home/andres/b14.gif')
anim2.after_cancel(anim2.cancel)
anim2.pack()


def stop_it():
    anim2.after_cancel(anim2.cancel)

def start_it():
    anim2.play()
    

#Button(ventana, text='stop', command=stop_it).pack()
#Button(ventana, text='start', command=start_it).pack()
photo = PhotoImage(file = '/home/andres/micro2.png')
micro = Button(ventana, text='micro', command=iniciar_conversacion, image = photo).pack()

btn_text = tk.StringVar()
notificacion = Button(ventana, textvariable=btn_text, command=iniciar_conversacion).pack(side = tk.LEFT)
#notificacion.place(x=30, y=30)
#notificacion.pack(side=tkinter.BOTTOM)

#node = child.find('micro')
#node.grid(column = 1, row = 1)
#Button(ventana, text='texto', command=conversacion_texto).pack()


#--------------------------------------------

# NOTE: this example requires PyAudio because it uses the Microphone class

import speech_recognition as sr
import rospy
from std_msgs.msg import String
from tutorial.srv import ChatBotVariables

# This module is imported so that we can
# play the converted audio
import os


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
        #print(sr.Microphone.list_microphone_names())

        #for index, name in enumerate(sr.Microphone.list_microphone_names()):
            #print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))
        
        #with sr.Microphone(device_index=1) as source:
            #r.adjust_for_ambient_noise(source)
            #print("Di, algo")
            
            #audio = r.listen(source, phrase_time_limit = 10 )

        # recognize speech using Google Speech Recognition
        try:
            # for testing purposes, we're just using the default API key
            # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
            # instead of `r.recognize_google(audio)`

            audio = sr.AudioFile("/home/andres/catkin_ws/src/tutorial/audio_files/u_audio.wav") #read audio object and transcribe

            with audio as source:

                audio = r.record(source)  
                print("Analizando audio")                
                dice = r.recognize_google(audio)

            #dice = r.recognize_google(voz,language='es-EC')
            print("Google Speech Recognition thinks you said> " + dice)
            
            numeroPalabras = contarPalabras(dice)
            print("Numero de palabras " + str(numeroPalabras))            
            escribirArchivo(dice + " - " + str(datetime.today()))

            # Language in which you want to convert
            language = 'es' 

            if (variable!="N0"):
                if (numeroPalabras > 5):
                    respuestaChatBot = "%s"%(chatBot_client(dice+variable))#se envia una N para hacer referencia que esta en el CHAT NORMAL
                    escribirArchivo(respuestaChatBot+ " - " + str(datetime.today()))
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
                else:
                    respuestaChatBot = "La respuesta debe tener al menos 25 palabras, por favor repita"
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
            else:
                    respuestaChatBot = "%s"%(chatBot_client(dice+variable))#se envia una N para hacer referencia que esta en el CHAT NORMAL
                    escribirArchivo(respuestaChatBot+ " - " + str(datetime.today()))
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
                    myobj.save("/home/andres/catkin_ws/src/tutorial/audio_files/user_audio/chatbot_audio.mp3")

                    # files                                                                         
                    src = "chatbot_audio.mp3"
                    dst = "chatbot_audio.wav"

                    # convert wav to mp3                                                            
                    sound = AudioSegment.from_mp3(src)
                    sound.export(dst, format="wav")

                    # Playing the converted file
                    abrir_archivo()
                    iniciar()

        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
            myobj = gTTS(text="Lo siento, pero no entiendo. Puede repetir?", lang='es', slow=False)

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
        
        #diceTexto = chatTexto.get()
        diceTexto = "dice texto"

        #chatTexto.configure(state='normal')
        #chatTexto.delete(0,'end')        

        print("Lo que se envia como texto>>> " + diceTexto+variable)

        escribirArchivo(diceTexto+ " - " + str(datetime.today()))
        

        respuestaChatBot = "%s"%(chatBot_client(diceTexto+variable))#se envia una N para hacer referencia que esta en el CHAT NORMAL
        respuestaChatBot = "respuesta"+variable
        print(" Respuesta chatbot>>>>>>>>" + respuestaChatBot )

        escribirArchivo(respuestaChatBot+ " - " + str(datetime.today()))

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
    
    
    
