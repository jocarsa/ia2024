from PIL import Image
import os
import sqlite3

conexion = sqlite3.connect('memoria.db')
cursor = conexion.cursor()

cursor.execute('''
                DELETE FROM muestras  
            ''')
conexion.commit()

def convert_to_hex(num):
    if not (0 <= num <= 255):
        raise ValueError("Input number must be between 0 and 255")
    hex_value = hex(num % 16)[2:]  # Convert to hex and remove the '0x' prefix
    return hex_value

anchuraorigen = 16
anchuradestino = 4

carpeta = "entrenamiento"
for archivo in os.listdir(carpeta):
    imagen = Image.open("entrenamiento/"+archivo)
    nombre = archivo

    altura,anchura = imagen.size
    archivo = open("memoria.txt",'a')
    paso = 4
    for i in range(0,anchura-anchuraorigen,paso):
        print("nueva fila",i)
        for j in range(0,altura-anchuraorigen,paso):
            
            cortado = imagen.crop((i,j,i+anchuraorigen,j+anchuraorigen))
            pixeles = cortado.load()

            stringcortado = ""
            for x in range(0,anchuraorigen):
                for y in range(0,anchuraorigen):
                    stringcortado += str(pixeles[x,y])

            redimensionado = cortado.resize((anchuradestino,anchuradestino),Image.Resampling.BICUBIC)
            pixeles = redimensionado.load()
            stringpequeno = ""
            for x in range(0,anchuradestino):
                for y in range(0,anchuradestino):
                    media = round((pixeles[x,y][0]+pixeles[x,y][1]+pixeles[x,y][2])/3)
                    #stringpequeno += convert_to_hex(media)
                    #stringpequeno += convert_to_hex(pixeles[x,y][0])
                    
                    if media < 127:
                        stringpequeno += "0"
                    else:
                        stringpequeno += "1"
                    
            cursor.execute('''
                INSERT INTO muestras  VALUES (NULL,?, ?,?, ?,?, ?)
            ''', (stringpequeno, nombre,i,j,anchuraorigen,anchuraorigen))
conexion.commit()
conexion.close()
