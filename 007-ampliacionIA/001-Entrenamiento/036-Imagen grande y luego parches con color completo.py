from PIL import Image
import sqlite3


imagen = Image.open("josevicentepequeño.jpg")
anchura,altura = imagen.size
imagengrande = Image.new('RGB', (anchura*4, altura*4), 'white')

imagenpequeñaperogrande = imagen.resize(imagengrande.size)
imagengrande.paste(imagenpequeñaperogrande,(0,0))

conexion = sqlite3.connect('memoria.db')
cursor = conexion.cursor()

anchuramuestra = 4
paso = 4
total = pow((anchura-anchuramuestra)/paso,2)
contador = 0



for i in range(0,anchura-anchuramuestra,paso):
    print("nueva fila",i)
    for j in range(0,altura-anchuramuestra,paso):
        contador+=1
        print((contador/total)*100,"%")
        cortado = imagen.crop((i,j,i+anchuramuestra,j+anchuramuestra))
        pixeles = cortado.load()

        lista = []
        for x in range(0,anchuramuestra):
            for y in range(0,anchuramuestra):
                media = round((pixeles[x,y][0]+pixeles[x,y][1]+pixeles[x,y][2])/3)
                lista.append(pixeles[x,y])
                
        cursor.execute('SELECT * FROM muestras')
        filas = cursor.fetchall()
        mejorcandidato = 10000000
        idmejorcandidato = None
        nombreimagen = None
        ximagen = None
        yimagen = None
        for fila in filas:
            suma = 0
            listadb = eval(fila[1])
            for i in range(0,len(lista)):
                suma += abs(lista[i][0] - listadb[i][0])
                suma += abs(lista[i][1] - listadb[i][1])
                suma += abs(lista[i][2] - listadb[i][2])
            if suma < mejorcandidato:
                suma = mejorcandidato
                idmejorcandidato = fila[0]
                nombreimagen = fila[2]
                ximagen = fila[3]
                yimagen = fila[4]
            
            abroimagengrande = Image.open("entrenamiento/"+nombreimagen)
            trozo = abroimagengrande.crop((ximagen,yimagen,ximagen+anchuramuestra*4,yimagen+anchuramuestra*4))
            imagengrande.paste(trozo,(ximagen,yimagen))
            abroimagengrande.close()
imagengrande.save("agrandado.jpg")        
imagengrande.close() 
conexion.close()
