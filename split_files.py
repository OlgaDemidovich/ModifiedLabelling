import os
import random
import shutil


def saving_files(path, images):
    for imgName in images:
        og_path = os.path.join('images', imgName)
        target_path = os.path.join(path + '/images', imgName)
        shutil.copyfile(og_path, target_path)

        og_txt_path = os.path.join('labels', imgName.replace('.jpg', '.txt'))
        target_txt_path = os.path.join(path + '/labels',
                                       imgName.replace('.jpg', '.txt'))

        shutil.copyfile(og_txt_path, target_txt_path)


imgList = os.listdir('images')

# shuffling images
random.shuffle(imgList)

# percent_train + percent_val < 1
percent_train = 0.7
percent_val = 0.25

train_path = 'custom_dataset/train'
val_path = 'custom_dataset/val'
test_path = 'custom_dataset/test'


def create_dir(path):
    if not os.path.isdir(path):
        os.makedirs(path)
    if not os.path.isdir(path + '/images'):
        os.makedirs(path + '/images')
    if not os.path.isdir(path + '/labels'):
        os.makedirs(path + '/labels')


create_dir(train_path)
create_dir(val_path)
create_dir(test_path)

imgLen = len(imgList)
print("Images in total: ", imgLen)

train_images = imgList[: int(imgLen * percent_train)]
val_images = imgList[int(imgLen * percent_train):int(
    imgLen * (percent_train + percent_val))]
test_images = imgList[int(
    imgLen * (percent_train + percent_val)):]

print("Training images: ", len(train_images))
print("Validation images: ", len(val_images))
print("Testing images: ", len(test_images))

saving_files(train_path, train_images)
saving_files(val_path, val_images)
saving_files(test_path, test_images)

print("Done!")
