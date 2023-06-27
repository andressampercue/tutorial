#! /usr/bin/env python3
# -*- encoding: UTF-8 -*-

import subprocess

scripts_paths = ("/home/andres/catkin_ws/src/tutorial/src/listen_pepper_execnet.py", "/home/andres/catkin_ws/src/tutorial/src/video_pepper_execnet.py")

ps = [subprocess.Popen(["python3", script]) for script in scripts_paths]
exit_codes = [p.wait() for p in ps]

if not any(exit_codes):
    print("Todos los procesos terminaroin con éxito")
else:
    print("Algunos procesos terminaron de forma inesperada.")