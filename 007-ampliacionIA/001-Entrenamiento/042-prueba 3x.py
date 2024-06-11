import numpy as np
from PIL import Image
import sqlite3
import time

# Get the start time
start_time = time.time()

# Open and resize the image
imagen = Image.open("josevicentepequeño2.jpg")
anchura, altura = imagen.size
imagengrande = Image.new('RGB', (anchura * 4, altura * 4), 'white')
imagenpequeñaperogrande = imagen.resize(imagengrande.size)
imagengrande.paste(imagenpequeñaperogrande, (0, 0))

# Load the alpha mask
alpha_mask = Image.open("alpha.png")

# Connect to the database
conexion = sqlite3.connect('memoria.db')
cursor = conexion.cursor()

# Get all rows from the database
cursor.execute('SELECT * FROM muestras')
filas = cursor.fetchall()

# Convert the database data to a list of NumPy arrays
db_data = [(fila[0], np.array(eval(fila[1])), fila[2], fila[3], fila[4]) for fila in filas]
#print(db_data)
anchuramuestra = 3
paso = 1
total = ((anchura - anchuramuestra) // paso) ** 2
contador = 0

for i in range(0, anchura - anchuramuestra, paso):
    print("nueva fila", i, (contador / total) * 100, "%")
    for j in range(0, altura - anchuramuestra, paso):
        contador += 1

        # Crop the patch from the image
        cortado = imagen.crop((i, j, i + anchuramuestra, j + anchuramuestra))
        pixeles = np.array(cortado).reshape(-1, 3)

        # Use broadcasting to calculate the sum of absolute differences efficiently
        diffs = [np.sum(np.abs(pixeles - db_pixeles)) for _, db_pixeles, _, _, _ in db_data]
        mejorcandidato = np.argmin(diffs)
        idmejorcandidato, _, nombreimagen, ximagen, yimagen = db_data[mejorcandidato]
        
        with Image.open("entrenamiento/" + nombreimagen) as abroimagengrande:
            trozo = abroimagengrande.crop((ximagen, yimagen, ximagen + 16, yimagen + 16))
            
            # Ensure the alpha mask is the same size as the piece being pasted
            alpha_resized = alpha_mask.resize(trozo.size)
            
            # Paste with the alpha mask
            imagengrande.paste(trozo, (i * 4, j * 4), alpha_resized)

# Save the final image
imagengrande.save("agrandado.jpg")
imagengrande.close()
conexion.close()

# Get the end time
end_time = time.time()

# Calculate the time taken
time_taken = end_time - start_time
print(f"Time taken to execute the script: {time_taken} seconds")
