from PIL import Image, ImageOps
import numpy as np

def similar(block1, block2):
    return np.sum(np.abs(block1 - block2))

def compara(superx, supery, anchura=8):
    bloque = np.array(izquierda.crop((superx, supery, superx + anchura, supery + anchura)))
    mejorsimilaridad = float('inf')
    mejorcandidato = 0
    for desplazamientox in range(-50, 51):
        if superx + desplazamientox < 0 or superx + anchura + desplazamientox >= derecha.width:
            continue
        bloque2 = np.array(derecha.crop((superx + desplazamientox, supery, superx + anchura + desplazamientox, supery + anchura)))
        similaridad = similar(bloque, bloque2)
        if similaridad < mejorsimilaridad:
            mejorsimilaridad = similaridad
            mejorcandidato = desplazamientox
    return mejorcandidato

imagen = Image.open("referencia2.jpeg")
escalado = imagen.resize((640, 480))
izquierda = escalado.crop((0, 0, 320, 480))
derecha = escalado.crop((320, 0, 640, 480))
for i in [8,16,32,64]:
    depth_map = np.zeros((480, 320), dtype=np.float32)
    paso = i  # Increase step for larger blocks
    block_size = i

    for y in range(0, 480 - block_size, paso):
        for x in range(0, 320 - block_size, paso):
            depth = compara(x, y, block_size)
            depth_map[y:y + block_size, x:x + block_size] = depth

    # Normalize depth map to the range [0, 255]
    depth_map_normalized = (depth_map - np.min(depth_map)) / (np.max(depth_map) - np.min(depth_map)) * 255

    # Invert the grayscale values
    depth_map_inverted = 255 - depth_map_normalized

    # Convert to an image
    depth_map_image = Image.fromarray(depth_map_inverted.astype(np.uint8))

    # Save the depth map as a grayscale image
    depth_map_image = ImageOps.grayscale(depth_map_image)
    depth_map_image.save("depth_map_inverted.jpg")
    depth_map_image.show()
