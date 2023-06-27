#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import execnet

def pepper_video():

    gw = execnet.makegateway("popen//python=python2.7")
    channel = gw.remote_exec("""
        import qi
        import argparse
        import sys
        import time

        session = qi.Session()

        try:
            session.connect("tcp://172.16.226.67:9559")
            print('Succesfull connecting')
        except:
            print('Error connecting to robot')
            
        # This example demonstrates how to use the ALVideoRecorder module to record a video file on the robot.
        
        # Get the service ALVideoRecorder.

        vid_recorder_service = session.service("ALVideoRecorder")
        vid_recorder_service.stopRecording()

        # This records a 320*240 MJPG video at 10 fps.
        # Note MJPG can't be recorded with a framerate lower than 3 fps.
        vid_recorder_service.setResolution(1)
        vid_recorder_service.setFrameRate(10)
        vid_recorder_service.setVideoFormat("MJPG")
        vid_recorder_service.startRecording("/home/nao/recordings/cameras", "myvideo_2")

        time.sleep(10)

        # Video file is saved on the robot in the
        # /home/nao/recordings/cameras/ folder.
        videoInfo = vid_recorder_service.stopRecording()

        print("Video was saved on the robot: ", videoInfo[1])
        print("Num frames: ", videoInfo[0])
        channel.send("video recorded")

    """)
    #channel.send(None)
    print (channel.receive())

if __name__ == '__main__':
    pepper_video()