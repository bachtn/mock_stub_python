from unittest.mock import patch

from image_tools import load_images, save_images


@patch('image_tools.cv2.imwrite')
def test_save_images_should_not_call_cv2_imwrite_function(imwrite_mock):
    # Given
    image_list, image_name_list = load_images('images')

    # When
    save_images(image_list, image_name_list, 'images')

    # Then
    assert not imwrite_mock.called
