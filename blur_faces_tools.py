import logging
from typing import List

import cv2
import face_recognition
import numpy

from image_tools import resize_images

logging.basicConfig(level='INFO')

IMAGE_FOLDER = 'images'
WIDTH, HEIGHT = 1200, 800
GAUSSIAN_KERNEL_SIZE = (345, 345)
X_STANDARD_DEVIATION = 0


# Detect faces
def rescale_face_boxes(face_boxes, shape):
    rescaled_faces = [
        [int(top * shape[0] / HEIGHT), int(right * shape[1] / WIDTH),
         int(bottom * shape[0] / HEIGHT), int(left * shape[1] / WIDTH)] \
        for top, right, bottom, left in face_boxes]
    return rescaled_faces


def detect_faces_in_images(image_list):
    logging.info(f'Detecting faces in {len(image_list)} images')
    resized_image_list = resize_images(image_list)
    rescaled_face_boxes_batch = face_recognition.batch_face_locations(
        resized_image_list, number_of_times_to_upsample=1)
    # face_boxes_batch = [face_recognition.face_locations(resized_image) for resized_image in resized_image_list]
    image_shape_list = [image.shape for image in image_list]
    face_boxes_batch = [rescale_face_boxes(face_boxes, image_shape) for face_boxes, image_shape in
                        zip(rescaled_face_boxes_batch, image_shape_list)]
    return face_boxes_batch


# Blur faces
def crop_faces(image: numpy.ndarray, face_boxes) -> List[numpy.ndarray]:
    return [image[top:bottom, left:right] for top, right, bottom, left in face_boxes]


def blur_faces_in_image(image: numpy.ndarray, face_crops: List[numpy.ndarray], face_boxes) -> numpy.ndarray:
    blurred_image = image.copy()
    blurred_faces = [cv2.GaussianBlur(face_crop, GAUSSIAN_KERNEL_SIZE, X_STANDARD_DEVIATION) \
                     for face_crop in face_crops]
    for blurred_face, (top, right, bottom, left) in zip(blurred_faces, face_boxes):
        blurred_image[top:bottom, left:right] = blurred_face
    return blurred_image


def blur_faces_in_images(image_list: List[numpy.ndarray], face_boxes_batch) -> List[numpy.ndarray]:
    logging.info(f'Blurring faces in images')
    blurred_image_list = []
    for image, face_boxes in zip(image_list, face_boxes_batch):
        if len(face_boxes) > 0:
            face_crops = crop_faces(image, face_boxes)
            blurred_image = blur_faces_in_image(image, face_crops, face_boxes)
        else:
            blurred_image = image
        blurred_image_list.append(blurred_image)
    return blurred_image_list
