from PIL import Image
import sqlite3

def convert_to_hex(num):
    if not (0 <= num <= 255):
        raise ValueError("Input number must be between 0 and 255")
    hex_value = hex(num % 16)[2:]  # Convert to hex and remove the '0x' prefix
    return hex_value

def convert_to_decimal(hex_str):
    if len(hex_str) != 1 or not (hex_str.isdigit() or (hex_str.lower() in "abcdef")):
        raise ValueError("Input must be a single hexadecimal character (0-9, a-f)")

    decimal_value = int(hex_str, 16)  # Convert from hex to decimal
    return decimal_value

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
        cursor.execute('SELECT * FROM muestras')
        filas = cursor.fetchall()
        mejorcandidato = 100000000
        idmejorcandidato = None
        for fila in filas:
            suma = 0
            for a in range(0,len(stringpequeno)):
                suma+= abs(convert_to_decimal(stringpequeno[a])-convert_to_decimal(fila[1][a]))
            if suma < mejorcandidato:
                mejorcandidato = suma
                idmejorcandidato = fila[0]
        print("El mejor id tiene una suma de ",mejorcandidato,"y un id de ",idmejorcandidato)
        

conexion.close()
