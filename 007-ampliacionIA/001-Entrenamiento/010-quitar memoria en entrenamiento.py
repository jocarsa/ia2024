from PIL import Image
import os

try:
    os.remove("memoria.txt")
except:
    pass

imagen = Image.open("josevicente.jpg")
nombre = "josevicente.jpg"

altura,anchura = imagen.size

for i in range(0,anchura-64):
    for j in range(0,altura-64):
        print(i,j)
        cortado = imagen.crop((i,j,i+64,j+64))
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
                media = round((pixeles[x,y][0]+pixeles[x,y][1]+pixeles[x,y][2])/3)
                if media < 127:
                    stringpequeno = "0"
                else:
                    stringpequeno = "1"


        archivo = open("memoria.txt",'a')
        archivo.write(
            nombre
            +"|"
            +str(i)
            +"|"
            +str(j)
            +"|64|64|"
            +stringpequeno
            +"\n")
        archivo.close()
