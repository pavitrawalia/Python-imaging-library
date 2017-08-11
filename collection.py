from PIL import Image
import numpy as np
import time
import matplotlib.pyplot as plt

def threshold(imageArray):
    blanceAr=[]
    newAr=imageArray

    for eachRow in imageArray:
        for eachPix in eachRow:
            print eachPix

            time.sleep(5)
            
i=Image.open('Picture1.jpg')
iar=np.array(i)

i2=Image.open('Picture2.jpg')
iar2=np.array(i2)

i3=Image.open('Picture3.jpg')
iar3=np.array(i3)

i4=Image.open('Picture4.jpg')
iar4=np.array(i4)




fig=plt.figure()
ax1=plt.subplot2grid((8,6),(0,0), rowspan=4, colspan=3)
ax2=plt.subplot2grid((8,6),(4,0), rowspan=4, colspan=3)
ax3=plt.subplot2grid((8,6),(0,3), rowspan=4, colspan=3)
ax4=plt.subplot2grid((8,6),(4,3), rowspan=4, colspan=3)

ax1.imshow(iar)
ax2.imshow(iar2)
ax3.imshow(iar3)
ax4.imshow(iar4)

plt.show()
