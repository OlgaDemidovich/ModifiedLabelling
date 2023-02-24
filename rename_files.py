import os
import glob

file_names = glob.glob("images/*")
image_path = r'images'
label_path = r'labels'
i = 0
for file_path in file_names:
    file_name = file_path[len(image_path) + 1:]
    os.rename(os.path.join(image_path, file_name),
              os.path.join(image_path, str(i) + '.jpg'))
    os.rename(os.path.join(label_path, file_name.replace('.jpg', '.txt')),
              os.path.join(label_path, str(i) + '.txt'))
    i += 1

