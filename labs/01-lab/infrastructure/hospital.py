import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os

def draw_hospital():
    cwd = os.getcwd()  # Get the current working directory (cwd)
    files = os.listdir(cwd)
    img = mpimg.imread(cwd+"/labs/01-lab/images/hospital.jpeg")
    imgplot = plt.imshow(img)
    plt.show()
    return
