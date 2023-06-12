#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sunau import AUDIO_FILE_ENCODING_LINEAR_32
import qi
import os
import subprocess
import time
from naoqi import ALProxy
from ftplib import FTP

class Pepper_comunications():

    def __init__(self, robot_ip):

        self.robot_ip = robot_ip
        self.robot_port = 9559

        '''self.session = qi.Session()

        try:
            self.session.connect("tcp://" + self.robot_ip + ":" + str(self.robot_port))
            print('Succesfull connecting')
        except:
            print('Error connecting to robot')'''

    def client_to_pepper(self):
    
        session = qi.Session()

        try:
            session.connect("tcp://" + self.robot_ip + ":" + str(self.robot_port))
            print('Succesfull connecting')
        except:
            print('Error connecting to robot')

        #file_path1 = "~/Documents/audio/test.wav"
        file_path = "/home/nao/recordings/chatbot/user_audio/u_audio.wav" #u_audio es el nombre del archivo de audio generado por grabacion desde pepper

        sample_rate = 48000
        channels = [0,0,1,0] #Only record sound of the third microphone
        leds = ALProxy("ALLeds", self.robot_ip, self.robot_port) 


        ar = ALProxy("ALAudioRecorder", self.robot_ip, self.robot_port)
        ar.stopMicrophonesRecording()
        ar.startMicrophonesRecording(file_path, "wav", sample_rate, channels)
        leds.rotateEyes(0x000000FF,1,5)
        ar.stopMicrophonesRecording()
        leds.on('FaceLeds')

        #aup = ALProxy("ALAudioPlayer", self.robot_ip, self.robot_port)
        #aup.post.playFile(file_path)

        #animation_player_service = session.service("ALAnimationPlayer")

        # play an animation, this will return when the animation is finished
        #animation_player_service.run("animations/Stand/Emotions/Positive/Happy_4")
        #animation_player_service.run("animations/Stand/Emotions/Positive/Peaceful_1")
        #animation_player_service.run("animations/Stand/Gestures/But_1")
        #animation_player_service.run("animations/Stand/Gestures/Choice_1")
        #animation_player_service.run("animations/Stand/Gestures/Everything_1")
        #animation_player_service.run("animations/Stand/Gestures/Everything_3")
        #animation_player_service.run("animations/Stand/Gestures/Everything_4")
        #animation_player_service.run("animations/Stand/Gestures/Explain_1")
        #animation_player_service.run("animations/Stand/Gestures/Explain_2")
        #animation_player_service.run("animations/Stand/Gestures/Explain_3")
    
    def pepper_to_client(self):

        session = qi.Session()

        try:
            session.connect("tcp://" + self.robot_ip + ":" + str(self.robot_port))
            print('Succesfull connecting')
        except:
            print('Error connecting to robot')

        file_path = "/home/nao/recordings/chatbot/chatbot_audio.wav" #u_audio es el nombre del archivo de audio generado por grabacion desde pepper
        aup = ALProxy("ALAudioPlayer", self.robot_ip, self.robot_port)
        aup.post.playFile(file_path)

        animation_player_service = session.service("ALAnimationPlayer")

        # play an animation, this will return when the animation is finished
        #animation_player_service.run("animations/Stand/Emotions/Positive/Happy_4")
        #animation_player_service.run("animations/Stand/Emotions/Positive/Peaceful_1")
        #animation_player_service.run("animations/Stand/Gestures/But_1")
        #animation_player_service.run("animations/Stand/Gestures/Choice_1")
        #animation_player_service.run("animations/Stand/Gestures/Everything_1")
        #animation_player_service.run("animations/Stand/Gestures/Everything_3")
        #animation_player_service.run("animations/Stand/Gestures/Everything_4")
        animation_player_service.run("animations/Stand/Gestures/Explain_1")
        animation_player_service.run("animations/Stand/Gestures/Explain_2")
        animation_player_service.run("animations/Stand/Gestures/Explain_3")

if __name__ == '__main__':

    comunication = Pepper_comunications("172.16.224.63")
    print("instanciado objeto")
    #comunication.client_to_pepper()
    comunication.pepper_to_client()





