import rawpy 
import imageio
import os

dirName = 'C:/Users/VikramSingh/DeskXXXXXtop/Sarnath/'
imagesNames = os.listdir(dirName)
targetFolder = 'C:/Users/VikramSingh/DesXXXXXXXXktop/SarnathCopy/'

for image in imagesNames:
     path = dirName+image
    #  print(path)
    #  print(image.split(".")[0])
     imgName = image.split(".")[0]
     with rawpy.imread(path) as raw:
        rgb = raw.postprocess()
     imageio.imsave(targetFolder+imgName+'.jpg', rgb)
