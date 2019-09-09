import logging
import os
from typing import List

import cv2
import numpy

WIDTH, HEIGHT = 1200, 800

logging.basicConfig(level='INFO')


# Get images
def get_image_paths_and_names(folder_path: str) -> List[str]:
    image_path_list, image_name_list = [], []
    with os.scandir(folder_path) as entries:
        for entry in entries:
            if entry.is_file() and entry.name.endswith('jpg'):
                image_path = os.path.join(folder_path, entry.name)
                image_path_list.append(image_path)
                image_name_list.append(entry.name)
    return image_path_list, image_name_list


def read_images(image_path_list: List[str]) -> numpy.ndarray:
    return [cv2.imread(image_path) for image_path in image_path_list]


def load_images(folder_path):
    logging.info(f'Loading the images of the following folder : {folder_path}')
    image_path_list, image_name_list = get_image_paths_and_names(folder_path)
    image_list = read_images(image_path_list)
    return image_list, image_name_list


# Detect faces
def resize_images(image_list: List[numpy.ndarray]) -> List[numpy.ndarray]:
    return [cv2.resize(image, (WIDTH, HEIGHT)) for image in image_list]


# Save images
def convert_to_jpeg(image: numpy.ndarray) -> numpy.ndarray:
    is_successful, jpeg_data = cv2.imencode('.jpeg', image)
    if not is_successful:
        error_message = 'Error encountered while converting image to JPG'
        logging.error(error_message)
        raise Exception(error_message)
    return jpeg_data


def save_images(image_list, image_name_list, folder):
    logging.info(f'Saving {len(image_list)} images in the following folder : {folder}')
    for image, image_name in zip(image_list, image_name_list):
        jpeg_image = convert_to_jpeg(image)
        image_path = os.path.join(folder, f'blurred_{image_name}')
        # cv2.imwrite(image_path, jmage)
        with open(image_path, 'wb') as file:
            file.write(jpeg_image)
