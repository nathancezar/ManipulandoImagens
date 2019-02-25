from __future__ import print_function
import cv2 as cv
import numpy as np
import argparse

## ----------- Obtendo Imagem em escala de cinza  -----------

## Laço para percorrer a imagem Original, transformando cada pixel em escala de cinza
#  Formula usada: 'RGB[A] to Gray:Y←0.299⋅R+0.587⋅G+0.114⋅B'
#  Poderia ser usada função np.clip():
#  -> gray[i,j] = np.clip(0.114 * img[i,j,0]  + 0.587 * img[i,j,1] + 0.299 * img[i,j,2], 0, 255)

def grayImage() :
    for line in range(img_Original.shape[0]):
        for col in range(img_Original.shape[1]):
            img_Gray[line, col] = img_Original[line, col][0]*0.114 + img_Original[line, col][1]*0.587 + img_Original[line, col][2]*0.299    

## Alterando a Escala da imagem
#  Esta função é mais rápida que q anterior, mas utiliza funções prontas da biblioteca
#  Função não utilizada, 
def grayImageChangeScale() :
    px = np.array([[[ 0.114, 0.587,  0.299]]])
    img_Gray_2 = cv.convertScaleAbs(np.sum(img_Original*px, axis=2))

## Convert Color do OpenCV
#  A maneira mais rápida de converter a imagem para escala de cinza
#  Função não utilizada
def grayCVTColor():
    img_Gray = cv.cvtColor(img_Original, cv.COLOR_BGR2GRAY)

## ------------- Obtento Imagem Negativa  ----------------------
'''
##! Processo para obter imagem Negativa
Subitraindo 255 do valor do pixxel da imagem original,
obteremos a inversão de cor. Por exemplo: 
    255 é o valor para branco
    ao subtrair 255 fica 0, que é o valor para preto.
Desta forma temos os valores negativos de todos os pixels da imagem,
o que gera uma imagem "negativa".
'''
def negativeImage() :
    for line in range(img_Original.shape[0]):
        for col in range(img_Original.shape[1]):
            img_Negative[line, col] = 255 - img_Original[line,col]

# Obtendo uma imagem Negativa usando a função invert() da biblioteca Numpy
# Função não utilizada
def negativeImageNumpy() :
    for line in range(img_Original.shape[0]):
        for col in range(img_Original.shape[1]):
            img_Negative[line, col] = np.invert(img_Original[line,col])

# Obtendo imagem negativa usando operação direta
# Função não utilizada
def negativeImageFast() :
    img_Negative = 255 - image_Original

## ------------- Obtendo Imagem com Threshold  ------------------

max_value = 150     # Valor de Threshold pedido no Teste
max_type = 4        # Tipos de Threshold utilizados
trackbar_type = 'Tipo: 0->Binario | 1->Binario Invertido | 2->Truncado | 3->Limiar a Zero | 4->Limiar a Zero Invertido'
trackbar_value = 'Valor'
threshold_window = 'Threshold'  # Nome da Janela de Resultado


## Função que aplica um Limiar (Threshold) Binario na Imagem em escala de Cinza.
# Neste tipo de Limiar, se a intensidade do pixel for maior que o 'thresh',
# o valor do novo pixel é definido como 'maxValue', que no caso do RGB é 255 (branco),
# caso contrário, o valor do novo pixel é definido como 0 (preto).
def threshold(thresh_) :
    img_Gray = cv.cvtColor(img_Original, cv.COLOR_BGR2GRAY)     # Obtendo uma imagem em escala de cinza da imagem original
    maxValue = 255
    for line in range(img_Gray.shape[0]):
        for col in range(img_Gray.shape[1]):
            if img_Gray[line, col] > thresh_ :      
                img_Threshold[line, col] = maxValue
            else :
                img_Threshold[line, col] = 0    
           
## Janela que receberá o resultado das operações de Threshold
cv.namedWindow(threshold_window)

## Função que aplica o Threshold na imagem, usando a biblioteca OpenCV
#  A Barra de tipo serve para selecionar o tipo de Threshold desejado
#  A barra de valor Altera o valor do 'thresh' de 0 a 150
def thresholdOpenCV(val):
    img_Gray = cv.cvtColor(img_Original, cv.COLOR_BGR2GRAY)
    threshold_type = cv.getTrackbarPos(trackbar_type, threshold_window)     #Trackbar ->Tipo
    threshold_value = cv.getTrackbarPos(trackbar_value, threshold_window)   #Trackbar Valor
    _, img_Threshold2 = cv.threshold(img_Gray, threshold_value, 255, threshold_type )
    cv.imshow(threshold_window, img_Threshold2)
    '''
        Argumentos da função cv.threshold:
        img_Gray: imagem de entrada
        threshold_value: Valor em relação ao qual a operação de limiar é feita
        255: valor usado para definir os pixels escolhidos (todos)
        threshold_type: Usado para selecionar uma das 5 operações de threshold possíveis.
    '''

# Trackbar criada para selecionar o tipo de Threshold
cv.createTrackbar(trackbar_type, threshold_window , 0, max_type, thresholdOpenCV)
# Trackbar criada para selecionar o valo do Threshold
cv.createTrackbar(trackbar_value, threshold_window , 150, max_value, thresholdOpenCV)


if __name__ == '__main__':
    ##  ---------- Obtendo a imagem passada como parâmetro  --------
    parser = argparse.ArgumentParser(description='Código para o Teste de Bolsista do LabTrans')
    parser.add_argument('--input', help='Digite "--input" e o caminho para a imagem ', default='./image.jpg')
    argumento = parser.parse_args()

    # Carrega uma imagem passada como parâmetro
    img_Original = cv.imread(argumento.input)
    if img_Original is None:
        print('Não foi possível abrir a imagem', argumento.input)
        exit(0)

    # Cria uma imagem Zerada (Preto) com o mesmo tamanho, quantidade de canais
    # e tipo da imagem Original
    img_Gray = np.zeros(img_Original.shape, img_Original.dtype)

    # Chamada da função
    grayImage()

    # Salva a imagem em escala de Cinza
    cv.imwrite('Gray_Image.jpg', img_Gray)
    # Mostrar a imagem em escala de cinza na tela
    cv.imshow('Gray image', img_Gray)

    # Cria uma imagem Zerada (Preto) com o mesmo tamanho, quantidade de canais
    # e tipo da imagem Original
    img_Negative = np.zeros(img_Original.shape, img_Original.dtype)

    ## Chamada da função para obter a imagem Negativa
    negativeImage()

    ## Salvando a imagen Negativa
    cv.imwrite('Negative_Image.jpg', img_Negative)
    # Mostrar a imagem Negativa na tela
    cv.imshow('Negative Image', img_Negative)

    # Cria uma imagem Zerada (Preto) com o mesmo tamanho, quantidade de canais
    # e tipo da imagem em escala de Cisza.
    img_Threshold = np.zeros(img_Gray.shape, img_Gray.dtype)

    # Chamada da função que aplica um Threshold na imagem no valor de 150
    threshold(150)

    # Salvando a Imagem com Threshold
    cv.imwrite('Threshold_Image.jpg', img_Threshold)
    # Mostrar a imagem com Threshold na tela
    cv.imshow('Threshold Image', img_Threshold)

    # Função extra para demostrar os tipos de Threshold
    thresholdOpenCV(0)

    cv.waitKey(0)   # Ao apertar qualquer tecla o programa fecha
    cv.destroyAllWindows()
