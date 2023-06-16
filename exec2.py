import execnet
gw = execnet.makegateway("popen//python=python2.7")
channel = gw.remote_exec("""
    import qi
    import time
    from naoqi import ALProxy
    session = qi.Session()

    session = qi.Session()

    try:
        session.connect("tcp://172.16.224.63:9559")
        print('Succesfull connecting')
    except:
        print('Error connecting to robot')

    file_path = "/home/nao/recordings/chatbot/user_audio/ppp.wav" #u_audio es el nombre del archivo de audio generado por grabacion desde pepper
    aup = ALProxy("ALAudioPlayer", "172.16.224.63", 9559)
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

    conf = "OK"

    channel.send(conf)
""")
channel.send(None)
print (channel.receive())