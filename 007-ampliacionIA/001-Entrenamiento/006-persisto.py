from PIL import Image

imagen = Image.open("josevicente.jpg")
cortado = imagen.crop((0,0,64,64))
pixeles = cortado.load()

stringcortado = ""
for x in range(0,64):
    for y in range(0,64):
        stringcortado += str(pixeles[x,y])

redimensionado = cortado.resize((16,16),Image.Resampling.BICUBIC)
pixeles = redimensionado.load()
stringpequeno = ""
for x in range(0,16):
    for y in range(0,16):
        stringpequeno += str(pixeles[x,y])


archivo = open("memoria.txt",'w')
archivo.write(stringpequeno+"|"+stringcortado+"\n")
archivo.close()
