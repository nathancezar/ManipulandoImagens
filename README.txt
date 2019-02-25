README

 - O exercicio foi resolvido utilizando a linguagem python, conforme pedido, com o auxílio das
 bibliotecas: OpenCV (visão computacional) e Numpy (calculos com matrizes).

 - Para executar o programa(Linux): 
 	- Caso a imagem esteja no memso diretorio do arquivo:
 		-> $ python3 ManipulandoImagens.py
 	- Caso queira carregar uma imagem de outro local:
 		-> $ python3 threshold.py --input ./Diretorio/da/imagem
 		-> $ python3 threshold.py --input ./image.jpg

 - O Programa abrirá 4 janelas:
 	- Gray Image: contendo a imagem em escala de cinza;
 	- Negative Image: contendo a imagem negativa
 	- Threshold Image: contendo a imagem com efeito Threshold Binário
	- Threshold: Janela que demonstra, usando a barra 'Tipo', o resultado obtido
		aplicando-se diferentes tipos de Limiar na imagem (Binario, Binario Invertido,
		Truncado, Limiar a Zero, Limiar a Zero Invertido)

 - A função utilizada para obter os resultados da quarta janela usa a função cv.threshold,
	da biblioteca OpenCV, e não foi construida da forma pedida no exercício. A mesma foi feita
	feita apenas por curiosidade.

 - O programa irá salvar as 3 imagens geradas (Gray_Image.jpg, Negative_Image.jpg e Threshold_Image.jpg)
	no mesmo diretório do arquivo.
 
 - Para encerrar o programa basta apertar qualquer tecla ou fechar as janelas.
