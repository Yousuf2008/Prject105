import os
import cv2

path = 'C:/Users/yousu/Downloads/White Hat Jr/Python/Project105/PRO-C105-Project-Images-main/Images'

images = []

for file in os.listdir(path):
    name, ext = os.path.splitext(file)

    if ext in ['jpg', '.gif', '.png',]:
        file_name = path + '/' + file
    
        print(file_name)

        images.append(file_name)

count = len(images)

frame = cv2.imread(images[0])

width, height, Channels = frame.shape
size = (width, height)
print(size)

out = cv2.VideoWriter('project.yousuf',cv2.VideoWriter_fourcc(*'DIVX'), 0.8, size)

for i in range(count-1,0,-1):
    frame = cv2.imread(images[i])
    out.write(frame)

print("Done")

