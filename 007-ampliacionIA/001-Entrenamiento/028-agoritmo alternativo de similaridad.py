from PIL import Image
import sqlite3
import Levenshtein

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

imagen = Image.open("josevicentepequeño2.jpg")
altura,anchura = imagen.size
imagengrande = Image.new('RGB', (altura*4, anchura*4), 'white')

conexion = sqlite3.connect('memoria.db')
cursor = conexion.cursor()

anchuramuestra = 4

paso = 4
for i in range(0,anchura-anchuramuestra,paso):
    print("nueva fila",i)
    for j in range(0,altura-anchuramuestra,paso):
        
        cortado = imagen.crop((i,j,i+anchuramuestra,j+anchuramuestra))
        pixeles = cortado.load()

        stringcortado = ""
        for x in range(0,anchuramuestra):
            for y in range(0,anchuramuestra):
                stringcortado += str(pixeles[x,y])

        redimensionado = cortado.resize((anchuramuestra,anchuramuestra),Image.Resampling.BICUBIC)
        pixeles = redimensionado.load()
        stringpequeno = ""
        for x in range(0,anchuramuestra):
            for y in range(0,anchuramuestra):
                media = round((pixeles[x,y][0]+pixeles[x,y][1]+pixeles[x,y][2])/3)
                stringpequeno += convert_to_hex(media)
                '''
                if media < 127:
                    stringpequeno += "0"
                else:
                    stringpequeno += "1"
                '''
        cursor.execute('SELECT * FROM muestras')
        filas = cursor.fetchall()
        mejorcandidato = 10000000
        idmejorcandidato = None
        nombreimagen = None
        ximagen = None
        yimagen = None
        for fila in filas:
            suma = 0
            #print(stringpequeno,fila[1])
            suma = Levenshtein.distance(stringpequeno, fila[1])
            #for a in range(0,len(stringpequeno)):
                #suma+= abs(convert_to_decimal(stringpequeno[a])-convert_to_decimal(fila[1][a]))
                #if stringpequeno[a] == fila[1][a]:
                    #suma += 1
            if suma < mejorcandidato:
                mejorcandidato = suma
                idmejorcandidato = fila[0]
                nombreimagen = fila[2]
                ximagen = fila[3]
                yimagen = fila[4]
        '''print(
            "El mejor id tiene una suma de ",mejorcandidato,
            "y un id de ",idmejorcandidato,
            "y por lo tanto tienes que ir a la imagen",nombreimagen,
            "y coger el cuadro de 64x64 que se encuentra en x=",ximagen,
            " e y=",yimagen)'''
        abroimagengrande = Image.open("entrenamiento/"+nombreimagen)
        trozo = abroimagengrande.crop((ximagen,yimagen,ximagen+anchuramuestra*4,yimagen+anchuramuestra*4))
        imagengrande.paste(trozo,(i*4,j*4))
        abroimagengrande.close()
imagengrande.save("agrandado.jpg")        
imagengrande.close() 
conexion.close()
