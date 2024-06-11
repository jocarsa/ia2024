from PIL import Image
import numpy as np
from scipy.spatial.distance import cosine

def similar(lista1,lista2):
    similaridad = 0
    for i in range(0,len(lista1)):
        for j in range(0,len(lista1[i])):
            similaridad += abs(lista1[i][j] - lista2[i][j])
    return similaridad

imagen = Image.open("referencia.jpg")
escalado = imagen.resize((640,480))
pixeles = escalado.load()
izquierda = escalado.crop((0,0,320,480))
derecha = escalado.crop((321,0,640,480))
pixelesizquierda = izquierda.load()
pixelesderecha = derecha.load()

def compara(superx, supery):
    mix = superx
    miy = supery
    anchura = 4
    bloque = izquierda.crop((mix, miy, mix + anchura, miy + anchura))
    pixelesbloque = bloque.load()
    listapixeles = []
    for x in range(anchura):
        for y in range(anchura):
            listapixeles.append(pixelesbloque[x, y])

    mejorsimilaridad = 10000000000
    mejorcandidato = 0
    for desplazamientox in range(-50, 50):
        bloque2 = derecha.crop((mix + desplazamientox, miy, mix + anchura + desplazamientox, miy + anchura))
        pixelesbloque2 = bloque2.load()
        listapixeles2 = []
        for x in range(anchura):
            for y in range(anchura):
                listapixeles2.append(pixelesbloque2[x, y])



        similaridad = similar(listapixeles,listapixeles2)
        
        if similaridad < mejorsimilaridad:
            mejorsimilaridad = similaridad
            mejorcandidato = desplazamientox

    return mejorcandidato

print(compara(180, 240))
