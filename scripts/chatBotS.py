#!/usr/bin/env python3
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import rospy
from std_msgs.msg import String
from tutorial.srv import *

from chatterbot.trainers import ChatterBotCorpusTrainer
from tutorial.srv import Cuestionario1, ChatBotVariables, DeteccionMentira, ChatbotSpecific

#para el nodo servidor del cuestionario
def add_two_ints_client(x):
    
    rospy.wait_for_service('cuestionario1')
    try:
        respuestaCuestionario = rospy.ServiceProxy('cuestionario1', Cuestionario1)
        resp1 = respuestaCuestionario(x)
        return resp1.response
    except rospy.ServiceException as e:
        print("Service cuestionario 1 call failed: %s"%e)

#para el nodo servidor de detectior de la mentira
def deteccion_mentira_client(x):
    
    rospy.wait_for_service('detectartMentira')
    try:
        respuestaDetectorMentira = rospy.ServiceProxy('detectartMentira', DeteccionMentira)
        resp1 = respuestaDetectorMentira(x)
        #print("respuesta desde nodo-> ", resp1)
        return resp1.respuesta
    except rospy.ServiceException as e:
        print("Service detector mentira call failed: %s"%e)

#para el nodo servidor de chatbotSpecific
def chatbot_specific(x):
    
    rospy.wait_for_service('chatbotSpecific')
    try:
        respuestachatbotSpecific = rospy.ServiceProxy('chatbotSpecific', ChatbotSpecific)
        resp1 = respuestachatbotSpecific(x)
        #print("respuesta desde nodo-> ", resp1)
        return resp1.response
    except rospy.ServiceException as e:
        print("Service chatbot specific call failed: %s"%e)



def chatb(req):
        print('NEXUS-BOT INGRESA: ')
        estaEnElCuestionario = False 
        #numeroPregunta=1        
        
        peticionGeneral = req.request #guarda mi pregunta hecha en ceci.py
        numeroPregunta = int(peticionGeneral[len(peticionGeneral)-1]) #extrae numero pregunta
        estaCues= peticionGeneral[len(peticionGeneral)-2] #guarda letra del ultimo para ver si esta en el custionario la pregunta
        peticionGeneral= peticionGeneral[:len(peticionGeneral)-2] #extrae pregunta sin numero ni letra finales

        if (estaCues=="N"): #para ver si esta en el cuestionario
            estaEnElCuestionario = False
            print('NO ESTA EN EL CUESTIONARIO')
        else:
            estaEnElCuestionario = True
            print('ESTA EN EL CUESTIONARIO')
        
        
        if estaEnElCuestionario:
            
            deteccion_mentira_client(peticionGeneral) #ingresa a la funcion la pregunta

            responseGeneral = chatbot_specific(peticionGeneral)            
            response = str(responseGeneral)
            response1 = "salir"        
            print('ESTA EN EL CUESTIONARIO Y ES LA NUMERO '+str(numeroPregunta))
            if peticionGeneral == response1:
                estaEnElCuestionario=False
                print("Has salido del cuestionario 1")                
                rt = str("Has salido del cuestionario 1"+"N"+str(numeroPregunta))
                return str(rt)#devolvemos la respuesta de tipo string
            else:
                if numeroPregunta == 10:
                    estaEnElCuestionario=False
                    rt = str("Has terminado el cuestionario 1"+"N"+str(0))
                    return str(rt)#devolvemos la respuesta de tipo string
                else:
                    # pide otra pregunta del cuestionario    
                    #numeroPregunta=numeroPregunta+1
                    print("Se pide la pregunta "+str(numeroPregunta))  
                    respuestaCuestionario = "%s"%(add_two_ints_client(numeroPregunta))                
                    print(respuestaCuestionario)
                    #>>>>>
                    estaEnElCuestionario=True
                    rt = str(respuestaCuestionario)+"C"+str(numeroPregunta)
                    return str(rt)#devolvemos la respuesta de tipo string
            
        else:
            if numeroPregunta==1:
                deteccion_mentira_client(peticionGeneral)
                rt = str("Has terminado el cuestionario 1"+"N"+str(0))
                return str(rt)#devolvemos la respuesta de tipo string
            else:
                print('no ESTA EN EL CUESTIONARIO 1')
                responseGeneral = chatbot_specific(peticionGeneral)
                    
                print('NEXUS-BOT: ',responseGeneral)
                
                response = str(peticionGeneral)
                response1 = "cuestionario Uno"
                response2 = "cuestionario 1"   
                        
                if response == response1 or response == response2:
                    print("<<<<<<<<<<<<<<< Bienvenido al cuestionario 1 >>>>>>>>>>>>>>>>>>>>")
                    pregunta = add_two_ints_client(0)
                    print("%s"%(add_two_ints_client(0)))
                    rt = str("Cuestionario uno. "+pregunta+ "C"+str(0))
                    return str(rt)#devolvemos la respuesta de tipo string
                    estaEnElCuestionario = True 
                else:
                    estaEnElCuestionario = False
                    rt = str(response+'N0')
                    return str(rt)#devolvemos la respuesta de tipo string

            
                
            
def chatBot_server():
    #bot.storage.drop()
    rospy.init_node('chatBotSrv')
    s = rospy.Service('chatBotS', ChatBotVariables, chatb)
    print(">>>>>>>>>>>>>>>>>>>> Listo nodo ChatBotS. <<<<<<<<<<<<<<<<<<<<<<<")
    rospy.spin()        

if __name__ == '__main__':
    chatBot_server()
