import csv

import cv2

# Переводит csv файл со строками (всего один класс)
# Img_path;Answer
# images/rdd_India_002385.jpg;449 534 476 671 50 452 439 655
# В формат yolo

path_csv = "yami_labels/annotations.csv"
path_lables = 'yami_labels/'
path_image = 'yami_2k/'

with open(path_csv, 'r',
          encoding='utf-8', newline='') as file:
    reader = csv.reader(file)
    for i, row in enumerate(reader):
        if i == 0:
            continue
        print(row)
        row = row[0].split(';')
        image_file_name = row[0].split('/')[1]
        name_image_without_format_file = image_file_name.split('.')[0]
        print(image_file_name, name_image_without_format_file)

        image = cv2.imread(path_image + image_file_name)
        H, W, _ = image.shape
        # print(H, W)
        # cv2.imshow('f', image)
        # cv2.waitKey(0)

        coords = [int(i) for i in row[1].split()]
        coords_to_save = []
        for ind in range(0, len(coords), 4):
            x0, y0, x1, y1 = coords[ind:ind + 4]

            x_center = (x0 +(x1 - x0) / 2) / W
            y_center = (y0 + (y1 - y0) / 2) / H

            x_width = (x1 - x0) / W
            y_height = (y1 - y0) / H
            # x0 = x0 / W
            # y0 = y0 / H
            # x1 = x1 / W
            # y1 = y1 / H
            # x_center, y_center, x_width, y_height = (x1 - x0) / 2, (y1 - y0) / 2, x1 - x0, y1 - y0
            coords_to_save.append(f'0 {x_center} {y_center} {x_width} {y_height}\n')
        print(coords_to_save)
        with open(path_lables + name_image_without_format_file + '.txt', 'w') as file:
            file.writelines(coords_to_save)
