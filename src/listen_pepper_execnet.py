#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import execnet

def pepper_listen():

    gw = execnet.makegateway("popen//python=python2.7")
    channel = gw.remote_exec("""
        import qi
        import time
        from naoqi import ALProxy
        session = qi.Session()

        try:
            session.connect("tcp://172.16.226.67:9559")
            print('Succesfull connecting')
        except:
            print('Error connecting to robot')

        #response_number = channel.receive()
        file_path = "/home/nao/recordings/chatbot/response_1_1" #u_audio es el nombre del archivo de audio generado por grabacion desde pepper

        sample_rate = 48000
        channels = [0,0,0,1] #Only record sound of the third microphone
        leds = ALProxy("ALLeds", "172.16.226.67", 9559) 

        ar = ALProxy("ALAudioRecorder","172.16.226.67", 9559)
        ar.stopMicrophonesRecording()
        ar.startMicrophonesRecording(file_path, "wav", sample_rate, channels)
        print("Pepper listening")
        leds.rotateEyes(0x000000FF,1,10)
        leds.on('FaceLeds')
        time.sleep(5)
        ar.stopMicrophonesRecording()
        conf = "Audio recorded"

        channel.send(conf)
    """)
    #channel.send(None)
    print(channel.receive())

if __name__ == '__main__':
    pepper_listen()

