#!/usr/bin/env python3

from __future__ import print_function
from chatterbot import ChatBot
import rospy
from std_msgs.msg import String

from tutorial.srv import ChatbotSpecific,ChatbotSpecificResponse
import rospy
from chatterbot.trainers import ChatterBotCorpusTrainer
# Create a new instance of a ChatBot
bot = ChatBot(
        'Example Bot',
            storage_adapter='chatterbot.storage.SQLStorageAdapter',
            logic_adapters=[
                {
                    'import_path': 'chatterbot.logic.BestMatch',
                    'default_response': 'Lo siento, pero no entiendo. Puede repetir',
                    'maximum_similarity_threshold': 0.75
                }    
            ]
        )

trainer = ChatterBotCorpusTrainer(bot)

trainer.train(
            "chatterbot.corpus.spanish"
            
        )

def handle_add_two_ints(req):
    # print("Returning [%s + %s = %s]"%(req.a, req.b, (req.a + req.b)))
    # Get a response given the specific input
    print("req----",req.request)
    response = bot.get_response(req.request)
    print("La respuesta especific >>>> ",response)
    rt = str(response)
    return str(rt)#devolvemos la respuesta de tipo string

def add_two_ints_server():
    #bot.storage.drop()
    rospy.init_node('chatbotSpecific_server')
    s = rospy.Service('chatbotSpecific', ChatbotSpecific, handle_add_two_ints)
    print("Listo nodo cuestionario.")
    rospy.spin()

if __name__ == "__main__":
    add_two_ints_server()