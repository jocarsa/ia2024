from PIL import Image

imagen = Image.open("josevicente.jpg")
cortado = imagen.crop((0,0,64,64))
pixeles = cortado.load()
print(pixeles[0,0])
redimensionado = cortado.resize((16,16),Image.Resampling.BICUBIC)
pixeles = redimensionado.load()
print(pixeles[0,0])
