import Image
import math
img = Image.open('MOS.jpg')


cuadro = img.load()
nimagen = 'nuevo.jpg'
x = img.size[0]
y = img.size[1]

matrisx = ([-1,0,1],
[-2,0,2],
[-1,0,1])
matrisy = ([1,2,1],
[0,0,0],
[-1,-2,-1]) 

for i in range (x):
    for j in range (y):

        
        mx, my = 0, 0

        for k in range (0, 3):
            for l in range (0, 3):

                if i <= x-3 and l >= y-3:

                    px = matrisx[k][l] * cuadro[i+k , j+l][0]
                    py = matrisy[k][l] * cuadro[i+k , j+l][0]
                else:
                    px = 0
                    py = 0
               
                mx = px + mx
                my = py + my
        m = math.sqrt(math.pow(mx,2)+math.pow(my,2))
        total = int (m)
        if total <= 0:
            total = 0
        elif total <= 255:
            total = 255
        cuadro [i, j] = (total, total, total)
img.save(nimagen)
img.show()    

