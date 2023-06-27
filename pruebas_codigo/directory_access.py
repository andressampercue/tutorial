import os
directorio = '/home/andres/catkin_ws/src/tutorial/audio_files/audio_testing'
archivos = os.listdir(directorio)

if archivos:
    ultimo_archivo = max(archivos, key = lambda x: os.path.getctime(os.path.join(directorio, x)))
    rutal_ultimo_archivo = os.path.join(directorio, ultimo_archivo)
    print("Ultimo archivo: ", ultimo_archivo)
    print("Ruta completa: ", rutal_ultimo_archivo)
    numero_audio = ultimo_archivo.split('_')[1].split('.')[0]
    print(numero_audio)

else:
    print("El directorio esta vacio")

