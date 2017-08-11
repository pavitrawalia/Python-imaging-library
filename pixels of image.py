from PIL import Image
import numpy as np 
i=Image.open('Picture1.jpg')
iar=np.asarray(i)
print iar
