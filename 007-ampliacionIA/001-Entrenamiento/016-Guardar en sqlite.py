from PIL import Image
import os
import sqlite3

conexion = sqlite3.connect('memoria.db')
cursor = conexion.cursor()

def convert_to_hex(num):
    if not (0 <= num <= 255):
        raise ValueError("Input number must be between 0 and 255")
    hex_value = hex(num % 16)[2:]  # Convert to hex and remove the '0x' prefix
    return hex_value

imagen = Image.open("josevicente.jpg")
nombre = "josevicente.jpg"

altura,anchura = imagen.size
archivo = open("memoria.txt",'a')
paso = 4
for i in range(0,anchura-64,paso):
    print("nueva fila",i)
    for j in range(0,altura-64,paso):
        
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
                stringpequeno += convert_to_hex(media)
        cursor.execute('''
            INSERT INTO muestras  VALUES (NULL,?, ?,?, ?,?, ?)
        ''', (stringpequeno, nombre,i,j,64,64))
conexion.commit()
conexion.close()
