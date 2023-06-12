#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import getpass
import paramiko
import sys

class ssh_file_transfer:

    def __init__(self, robot_ip):

        self.robot_ip = robot_ip
        self.USERNAME = 'nao'
        self.PASSWORD = 'pepper'
        self.CLIENT = None

        try:

            # Conectamos por ssh

            self.CLIENT = paramiko.SSHClient()
            self.CLIENT.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            self.CLIENT.load_system_host_keys()
            self.CLIENT.connect( hostname = self.robot_ip , username = self.USERNAME , password = self.PASSWORD )
            print("Conectado")

        except:

            print('Error en la conexión')

            sys.exit(1)
    
    

    def getting_audio_from_pepper(self):
            
        

        """
        
        try:

            shell = self.CLIENT.invoke_shell()

            try:

                # Ejecutamos el comando remoto

                stdin, stdout, stderr = self.CLIENT.exec_command( 'ls -l' , bufsize = -1 , timeout = None , get_pty = True , environment = None)

                # Mostramos la salida estandar línea por línea

                print(stdout.read().decode())

            except:

                print('Error: al ejecutar el comando')

                sys.exit(1)

        except:

            print('Error en la conexión por ssh')

            sys.exit(1)

        # Cerramos el shell

        shell.close()

        # ------------------------------------------------------------------

        """

        remote_path = f'/home/{self.USERNAME}/recordings/chatbot/user_audio/u_audio.wav'
        output_file = '/home/andres/catkin_ws/src/tutorial/audio_files/user_audio/u_audio.wav'

        sftp_client = self.CLIENT.open_sftp()
        sftp_client.get(remote_path, output_file)

        self.CLIENT.close()


    def sending_audio_to_pepper(self):

        remote_path = f'/home/{self.USERNAME}/recordings/chatbot/chatbot_audio.wav'
        source_path = '/home/andres/catkin_ws/src/tutorial/audio_files/chatbot_audio.wav'

        sftp_client = self.CLIENT.open_sftp()
        sftp_client.put(source_path, remote_path)

        self.CLIENT.close()



if __name__ == '__main__':

    ssh = ssh_file_transfer('172.16.224.63')

    #ssh.getting_audio_from_pepper()
    ssh.sending_audio_to_pepper()