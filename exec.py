import execnet
gw = execnet.makegateway("popen//python=python2.7")
channel = gw.remote_exec("""
    import qi
    import time
    from naoqi import ALProxy
    session = qi.Session()

    try:
        session.connect("tcp://172.16.224.63:9559")
        print('Succesfull connecting')
    except:
        print('Error connecting to robot')

    #file_path1 = "~/Documents/audio/test.wav"
    file_path = "/home/nao/recordings/chatbot/user_audio/ppp.wav" #u_audio es el nombre del archivo de audio generado por grabacion desde pepper

    sample_rate = 48000
    channels = [1,1,1,1] #Only record sound of the third microphone
    leds = ALProxy("ALLeds", "172.16.224.63", 9559) 

    ar = ALProxy("ALAudioRecorder","172.16.224.63", 9559)
    ar.stopMicrophonesRecording()
    ar.startMicrophonesRecording(file_path, "wav", sample_rate, channels)
    leds.rotateEyes(0x000000FF,1,5)
    leds.on('FaceLeds')
    time.sleep(5)
    ar.stopMicrophonesRecording()
    conf = "OK"

    channel.send(conf)
""")
channel.send(None)
print (channel.receive())