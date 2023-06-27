#! /usr/bin/env python
# -*- encoding: UTF-8 -*-

"""Example: Demonstrates how to  to record a video file on the robot"""

import qi
import argparse
import sys
import time


def main(session):
    """
    This example demonstrates how to use the ALVideoRecorder module to record a
    video file on the robot.
    """
    # Get the service ALVideoRecorder.

    vid_recorder_service = session.service("ALVideoRecorder")

    # This records a 320*240 MJPG video at 10 fps.
    # Note MJPG can't be recorded with a framerate lower than 3 fps.
    vid_recorder_service.setResolution(1)
    vid_recorder_service.setFrameRate(10)
    vid_recorder_service.setVideoFormat("MJPG")
    vid_recorder_service.startRecording("/home/nao/recordings/cameras", "myvideo")

    time.sleep(5)

    # Video file is saved on the robot in the
    # /home/nao/recordings/cameras/ folder.
    videoInfo = vid_recorder_service.stopRecording()

    print("Video was saved on the robot: ", videoInfo[1])
    print("Num frames: ", videoInfo[0])


if __name__ == "__main__":

    session = qi.Session()
    try:
        session.connect("tcp://" + "172.16.226.67" + ":" + "9559")
    except RuntimeError:
        print ("Can't connect to Naoqi at ip \"" + "172.16.226.67" + "\" on port " + "9559" +".\n"
               "Please check your script arguments. Run with -h option for help.")
        sys.exit(1)
    main(session)