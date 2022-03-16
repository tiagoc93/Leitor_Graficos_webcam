"""
Abrir WebCam, Plotar Gráficos 3D, Baixar mp3
"""


from pytube import YouTube #pip install pytube
import moviepy.editor as me #pip install moviepy
import re
import os


#Entrada de dados
link = input('Digite o link:')
yb = YouTube(link)
caminho = input('Digite onde deseja salvar o video: ')

#Baixando...
print('Aguarde um momento')
youtube = yb.streams.filter(only_audio=True).first().download(caminho) #Baixando o audio e armazenando no caminho
print('Convertendo...')

for file in os.listdir(caminho):
    if re.search('mp4',file):
        #Converte para mp3
        mp4_caminho = os.path.join(caminho,file)
        mp3_caminho = os.path.join(caminho, os.path.splitext(file)[0]+'.mp3')
        new_file = me.AudioFileClip(mp4_caminho)
        new_file.write_audiofile(mp3_caminho)
        os.remove(mp4_caminho)
print('Processo Finalizado')

#Abrindo webcam
import cv2 #pip install opencv-python
video = cv2.VideoCapture(0, cv2.CAP_DSHOW) #Instancia um objeto para capturar a tela e passa 0 para o dispositivo padrao

while True:
    conexao,frame = video.read() #Leitura de conexao e frames
    cv2.imshow('Imagem',frame) #Apresenta a imagem
    if cv2.waitKey(1) == ord('f'): #Caso clicar na letra f, para a execução da webcam
        break

video.release() #Liberar a camera
cv2.destroyAllWindows() #Limpar a memoria

#Plotar graficos
import numpy #pip install numpy
import matplotlib.pyplot #pip install matplotlib

#pip list: apresenta uma lista de todos os modulos externos instalados

#Definição de x,y e z

x = numpy.outer(numpy.linspace(-2,2,10),numpy.ones(10))
y = x.copy().T
z = numpy.cos(x**3 +y**1)

eixo = matplotlib.pyplot.axes(projection = '3d') #Definição da projeção
eixo.plot_surface(x,y,z) #Definição da superficie
eixo.set_title('Gráfico 3D') #Definição do titulo
matplotlib.pyplot.show() #Mostrando a figura

