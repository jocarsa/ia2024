from PIL import Image
import numpy as np
from scipy.spatial.distance import cosine

def calculate_similarity(list1, list2):
    similarities = []
    for vec1, vec2 in zip(list1, list2):
        similarities.append(1 - cosine(vec1, vec2))
    return similarities

imagen = Image.open("referencia.jpg")
escalado = imagen.resize((640,480))
pixeles = escalado.load()
izquierda = escalado.crop((0,0,320,480))
derecha = escalado.crop((321,0,640,480))
pixelesizquierda= izquierda.load()
pixelesderecha= derecha.load()
#print(pixelesizquierda[0,0])
#print(pixelesderecha[0,0])

# primero tomo un bloque en la imagen de la izquierda
mix = 160
miy = 240
anchura = 8
bloque = izquierda.crop((mix,miy,mix+anchura,miy+anchura))
pixelesbloque = bloque.load()
listapixeles = []
for x in range(0,anchura):
    for y in range(0,anchura):
        listapixeles.append(pixelesbloque[x,y])
#print(listapixeles)
# Ahora busco ese bloque en la imagen de la derecha
mejorsimilaridad = 0
mejorcandidato = 0
for desplazamientox in range(-50,50):
    bloque2 = derecha.crop((mix+desplazamientox,miy,mix+anchura+desplazamientox,miy+anchura))
    pixelesbloque2 = bloque2.load()
    listapixeles2 = []
    for x in range(0,anchura):
        for y in range(0,anchura):
            listapixeles2.append(pixelesbloque2[x,y])
    similarity_indices = calculate_similarity(listapixeles, listapixeles2)
    overall_similarity_index = np.mean(similarity_indices)
    #print("para el desplazamiento",desplazamientox,"la similaridad es",overall_similarity_index)
    if overall_similarity_index > mejorsimilaridad:
        mejorsimilaridad = overall_similarity_index
        mejorcandidato = desplazamientox

print("El desplazamiento es de: ",mejorcandidato)
    
    
    
