from PIL import Image
import sqlite3

def convert_to_hex(num):
    if not (0 <= num <= 255):
        raise ValueError("Input number must be between 0 and 255")
    hex_value = hex(num % 16)[2:]  # Convert to hex and remove the '0x' prefix
    return hex_value

imagen = Image.open("josevicentepequeño.jpg")

conexion = sqlite3.connect('memoria.db')
cursor = conexion.cursor()

altura,anchura = imagen.size
paso = 16
for i in range(0,anchura-16,paso):
    print("nueva fila",i)
    for j in range(0,altura-16,paso):
        
        cortado = imagen.crop((i,j,i+16,j+16))
        pixeles = cortado.load()

        stringcortado = ""
        for x in range(0,16):
            for y in range(0,16):
                stringcortado += str(pixeles[x,y])

        redimensionado = cortado.resize((16,16),Image.Resampling.BICUBIC)
        pixeles = redimensionado.load()
        stringpequeno = ""
        for x in range(0,16):
            for y in range(0,16):
                media = round((pixeles[x,y][0]+pixeles[x,y][1]+pixeles[x,y][2])/3)
                stringpequeno += convert_to_hex(media)
        print(stringpequeno)
        cursor.execute('SELECT * FROM muestras' )
        filas = cursor.fetchall()
        for fila in filas:
            print("buscando",fila[1])
        

conexion.close()
