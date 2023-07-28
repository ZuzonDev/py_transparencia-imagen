# Importamos la librería 'pillow'
# (después de instalarla con 'pip install pillow').
from PIL import Image

# Abrimos la imagen en una variable.
imagen=Image.open('imagen.jpg')

# Convertimos la imagen en escala de grises (4 canales).
if imagen.mode != 'RGBA':
    imagen = imagen.convert('RGBA')

# Guardamos el ancho y el alto de la imagen en sendas variables.
ancho, alto = imagen.size

# Cargamos la matriz de píxeles
pixeles = imagen.load()

# Sustituimos el valor de A (255 por defecto, sin transparencia) 
# por el inverso del valor medio de RGB.

for x in range (ancho):
    for y in range (alto):
        r, g, b, a = pixeles[x,y]
        a = int(255-((r+g+b)/3))
        pixeles[x,y] = (r, g, b, a)

# Guardamos la nueva imagen en un archivo PNG.
imagen.save("imagen_trans.png")

#Mostramos la nueva imagen.
imagen.show()