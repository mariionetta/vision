import Image

img = Image.open('MOS.jpg')


cuadro = img.load()
nimagen = 'nuevo.jpg'
x = img.size[0]
y = img.size[1]

total = x * y  
#Escala de grises 
for i in range (x):
    for j in range (y):
        
        px = cuadro[i , j] 
        r = px[0]
        v = px[1]
        a = px[2]
        
        prom_px = (r + v + a) /3 

        cuadro[i , j] = (prom_px, prom_px, prom_px)

img.show()
#Realiza el Umbral
for i in range (x):
    for j in range (y):

        (r,v,a)  = cuadro[i, j]
        intensidad = r
        if intensidad >= 125:
            intensidad = 0
        else:
            intensidad = 255
        r = intensidad
        v = intensidad
        a = intensidad
        cuadro[i , j] = (r, v, a)
        
img.save(nimagen)
img.show()    

