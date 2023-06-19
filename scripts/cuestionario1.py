#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from __future__ import print_function

import rospy
from std_msgs.msg import String

from tutorial.srv import Cuestionario1,Cuestionario1Response
import os

def escribirArchivo(texto):
    path = os.path.abspath(
            os.path.join(os.path.dirname(__file__)))
    
    filename = os.path.join(path, '../src/auditoria.txt')
    
    with open(filename, 'a') as f:
                f.write(texto+'\n')

def handle_add_two_ints(req):

    switcher = {
        0: "Pregunta 1.  ¿Cual es su recuerdo mas vivido?",
        1: "Pregunta 2  ¿Qué es lo que menos que le gusta de usted?",
        2: "Pregunta 3  ¿Bajo qué circunstancias mentiría?",
        3: "Pregunta 4  ¿Qué recuerda de su padre?",
        4: "Pregunta 5  ¿Qué recuerda de su madre?",
        5: "Pregunta 6  ¿Cuál ha sido la mejor experiencia de su vida?",
        6: "Pregunta 7  ¿Cuál ha sido la peor experiencia de su vida?",
        7: "Pregunta 8  Si usted pudiera defraudar impuestos sin que nadie se enterara ¿Lo haría?",
        8: "Pregunta 9  Cuente una experiencia en la que haya mentido sin que nadie se enterara",
        9: "Pregunta 10  ¿Que es lo que opina sobre las aseguradoras de carros?"
        
    }
    # print("Returning [%s + %s = %s]"%(req.a, req.b, (req.a + req.b)))
    # Get a response given the specific input
    print("req----",req.request)
    response = switcher.get(req.request)
    print("Envia la pregunta solicitada ",response)
    rt = str(response)
    return str(rt)#devolvemos la respuesta de tipo string

def add_two_ints_server():
    #bot.storage.drop()
    rospy.init_node('cuestionario1_server')
    s = rospy.Service('cuestionario1', Cuestionario1, handle_add_two_ints)
    print(">>>>>>>>>>>>> Listo nodo cuestionario 1 <<<<<<<<<<<<<<<<<<<")
    rospy.spin()

if __name__ == "__main__":
    add_two_ints_server()