from PIL import Image, ImageOps
import numpy as np

def similar(lista1, lista2):
    similaridad = 0
    for i in range(len(lista1)):
        for j in range(len(lista1[i])):
            similaridad += abs(lista1[i][j] - lista2[i][j])
    return similaridad

def compara(superx, supery, anchura=4):
    bloque = izquierda.crop((superx, supery, superx + anchura, supery + anchura))
    pixelesbloque = list(bloque.getdata())
    mejorsimilaridad = float('inf')
    mejorcandidato = 0
    for desplazamientox in range(-50, 51):
        if superx + desplazamientox < 0 or superx + anchura + desplazamientox >= derecha.width:
            continue
        bloque2 = derecha.crop((superx + desplazamientox, supery, superx + anchura + desplazamientox, supery + anchura))
        pixelesbloque2 = list(bloque2.getdata())
        similaridad = similar(pixelesbloque, pixelesbloque2)
        if similaridad < mejorsimilaridad:
            mejorsimilaridad = similaridad
            mejorcandidato = desplazamientox
    return mejorcandidato

imagen = Image.open("referencia.jpg")
escalado = imagen.resize((640, 480))
izquierda = escalado.crop((0, 0, 320, 480))
derecha = escalado.crop((320, 0, 640, 480))

depth_map = np.zeros((480, 320), dtype=np.float32)

for y in range(50, 430, 5):  # Adjust step for efficiency
    for x in range(50, 270, 5):
        depth = compara(x, y)
        for dy in range(5):  # Propagate depth to a block of 5x5 pixels
            for dx in range(5):
                if 50 <= x + dx < 270 and 50 <= y + dy < 430:
                    depth_map[y + dy, x + dx] = depth

# Normalize depth map to the range [0, 255]
depth_map_normalized = (depth_map - np.min(depth_map)) / (np.max(depth_map) - np.min(depth_map)) * 255
depth_map_image = Image.fromarray(depth_map_normalized.astype(np.uint8))

# Save the depth map as a grayscale image
depth_map_image = ImageOps.grayscale(depth_map_image)
depth_map_image.save("depth_map.jpg")
depth_map_image.show()
