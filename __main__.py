from blur_faces_tools import detect_faces_in_images, blur_faces_in_images
from image_tools import load_images, save_images

IMAGE_FOLDER = 'images'


def blur_faces_usecase():
    image_list, image_name_list = load_images(IMAGE_FOLDER)
    face_boxes_batch = detect_faces_in_images(image_list)
    blurred_images = blur_faces_in_images(image_list, face_boxes_batch)
    save_images(blurred_images, image_name_list, IMAGE_FOLDER)


if __name__ == '__main__':
    blur_faces_usecase()
