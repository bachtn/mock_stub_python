from unittest.mock import patch

from image_tools import load_images, save_images, convert_to_jpeg


@patch('image_tools.cv2.imwrite')
def test_save_images_should_not_call_cv2_imwrite_function(imwrite_mock):
    # Given
    image_list, image_name_list = load_images('images')

    # When
    save_images(image_list, image_name_list, 'images')

    # Then
    assert not imwrite_mock.called


@patch('image_tools.cv2.imencode')
def test_convert_to_jpeg_calls_cv2_imencode_method(imencode_mock):
    # Given
    image_list, image_name_list = load_images('images')
    target_image = image_list[0]
    imencode_mock.return_value = (True, target_image)

    # When
    convert_to_jpeg(target_image)

    # Then
    imencode_mock.assert_called_once_with('.jpeg', target_image)
