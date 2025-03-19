import matplotlib.pyplot as plt
import numpy as np
import urllib
import PIL

urllib.request.urlretrieve("https://github.com/CambridgeEngineering/PartIA-Computing-Examples-Papers/raw/main/images/southwing.png", 
                           "baker.png")
A = PIL.Image.open("baker.png")
display(A)
A = np.asarray(A)
plt.imshow(A, cmap='gray')
print("Image array shape (pixels): {}".format(A.shape))

G = np.array([[-1,-1,-1], [-1,8,-1], [-1,-1,-1]])
B = np.zeros(A.shape)

for i in range(1, B.shape[0] - 1):
    for j in range(1, B.shape[1] - 1):
        for k in range(3):
            for l in range(3):
                B[i,j] += G[k,l] * A[i-1+k, j-1+l]

plt.imshow(B, cmap='gray')