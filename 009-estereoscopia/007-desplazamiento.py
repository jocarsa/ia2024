from PIL import Image


imagen = Image.open("referencia.jpg")
escalado = imagen.resize((640,480))
pixeles = escalado.load()
izquierda = escalado.crop((0,0,320,480))
derecha = escalado.crop((321,0,640,480))
pixelesizquierda= izquierda.load()
pixelesderecha= derecha.load()
print(pixelesizquierda[0,0])
print(pixelesderecha[0,0])

# primero tomo un bloque en la imagen de la izquierda
mix = 160
miy = 240
anchura = 4
bloque = izquierda.crop((mix,miy,mix+anchura,miy+anchura))
pixelesbloque = bloque.load()
listapixeles = []
for x in range(0,anchura):
    for y in range(0,anchura):
        listapixeles.append(pixelesbloque[x,y])
print(listapixeles)
# Ahora busco ese bloque en la imagen de la derecha
for desplazamientox in range(-20,20):
    bloque2 = derecha.crop((mix+desplazamientox,miy,mix+anchura+desplazamientox,miy+anchura))
    pixelesbloque2 = bloque2.load()
    listapixeles2 = []
    for x in range(0,anchura):
        for y in range(0,anchura):
            listapixeles2.append(pixelesbloque2[x,y])
    
    
