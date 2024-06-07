from PIL import Image
import sqlite3


imagen = Image.open("josevicentepequeño.jpg")
anchura,altura = imagen.size
imagengrande = Image.new('RGB', (anchura*4, altura*4), 'white')

conexion = sqlite3.connect('memoria.db')
cursor = conexion.cursor()

anchuramuestra = 4

paso = 4
for i in range(0,anchura-anchuramuestra,paso):
    print("nueva fila",i)
    for j in range(0,altura-anchuramuestra,paso):
        
        cortado = imagen.crop((i,j,i+anchuramuestra,j+anchuramuestra))
        pixeles = cortado.load()

        stringpequeno = ""
        for x in range(0,anchuramuestra):
            for y in range(0,anchuramuestra):
                #media = round((pixeles[x,y][0]+pixeles[x,y][1]+pixeles[x,y][2])/3)
                #stringpequeno += convert_to_hex(media)
                stringpequeno += hex(pixeles[x,y][0] % 16)[2:]
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
            for a in range(0,len(stringpequeno)):
                suma+= abs(int(stringpequeno[a],16)-int(fila[1][a],16))
               
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
        imagengrande.paste(trozo,(ximagen,yimagen))
        abroimagengrande.close()
imagengrande.save("agrandado.jpg")        
imagengrande.close() 
conexion.close()
