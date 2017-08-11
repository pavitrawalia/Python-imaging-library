from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
i=Image.open('Picture2.jpg')
iar=np.asarray(i)

plt.imshow(iar)
plt.show()
