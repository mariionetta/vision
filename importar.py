import Image
img = Image.open('MOS.jpg')


cuadro = img.load()
nimagen = 'nuevo.jpg'
x = img.size[0]
y = img.size[1]

total = x * y  
for i in range (x):
    for j in range (y):
        
        px = cuadro[i , j] 
        r = px[0]
        v = px[1]
        a = px[2]
        
        prom_px = (r + v + a) /3 

        cuadro[i , j] = (prom_px, prom_px, prom_px)

img.show()

for i in range (x):
    for j in range (y):

        (r,v,a)  = cuadro[i, j]
        prom_px = (r + v + a) /3 
        if prom_px >= 25:
            prom_px = 20
            break
        elif  prom_px >= 55:
            prom_px = 50
            break
        elif prom_px >= 105:
            prom_px = 100
            break
        elif  prom_px >= 155:
            prom_px = 150
            break
        elif prom_px >= 205:
            prom_px = 200
            break
        elif  prom_px >= 255:
            prom_px = 250
            break
        elif prom_px >= 105:
            prom_px = 100
            break
        r = prom_px
        v = prom_px
        a = prom_px
        cuadro[i , j] = (r, v, a)
        
img.save(nimagen)
img.show()    
