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

bloque = izquierda.crop((0,0,15,15))
pixelesbloque = bloque.load()
listapixeles = []
for x in range(0,15):
    for y in range(0,15):
        listapixeles.append(pixelesbloque[x,y])
print(listapixeles)
